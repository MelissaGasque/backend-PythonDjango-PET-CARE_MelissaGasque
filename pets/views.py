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
        print(group_data)
        traits_data = serializer.validated_data.pop("traits")
        group = Group.objects.create(**group_data)
        pet = Pet.objects.create(**serializer.validated_data, group=group)
        trait_obj = []
        for caracteristica in traits_data:
            trait = Trait.objects.create(**caracteristica)
            trait_obj.append(trait)
        pet.traits.set(trait_obj)
        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        pet = Pet.objects.all()
        # logica paginação
        result_page = self.paginate_queryset(pet, req, view=self)
        serializer = PetSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data) 