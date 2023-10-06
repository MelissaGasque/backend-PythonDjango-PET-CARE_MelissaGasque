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
