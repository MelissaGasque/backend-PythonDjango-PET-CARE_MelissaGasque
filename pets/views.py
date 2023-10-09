from rest_framework.views import Response, APIView, Request, status
from .serializers import PetSerializer
from .models import Pet
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination


class PetView(APIView, PageNumberPagination):
    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        group_data = serializer.validated_data.pop("group")
        traits_data = serializer.validated_data.pop("traits")

        try:
            group = Group.objects.get(
                scientific_name__iexact=group_data["scientific_name"]
            )
        except Group.DoesNotExist:
            group = Group.objects.create(**group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group)

        for caracteristica in traits_data:
            try:
                trait = Trait.objects.get(name__iexact=caracteristica["name"])
            except Trait.DoesNotExist:
                trait = Trait.objects.create(**caracteristica)
            pet.traits.add(trait)

        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        pet = Pet.objects.all()
        # logica paginação
        result_page = self.paginate_queryset(pet, req, view=self)
        serializer = PetSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)


class PetDetailView(APIView):
    def get(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            {"detail": "Not found."}, status.HTTP_404_NOT_FOUND
        serializer = PetSerializer(found_pet)
        return Response(serializer.data,  status.HTTP_200_OK)

    def delete(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
            found_pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pet.DoesNotExist:
            return Response(
                {"detail": "Not found."}, status.HTTP_404_NOT_FOUND
            )
        
    def patch(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(
                {"detail": "Not found."}, status.HTTP_404_NOT_FOUND
            )

        serializer = PetSerializer(data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)

        for key, value in serializer.validated_data.items():
            setattr(found_pet, key, value)  # found_pet[k] = v
        found_pet.save()

        serializer = PetSerializer(found_pet)
        return Response(serializer.data, status.HTTP_200_OK)
