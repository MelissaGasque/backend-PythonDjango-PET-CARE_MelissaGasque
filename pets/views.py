from django.forms import model_to_dict
from rest_framework.views import Request, Response, APIView, status
from .serializers import PetSerializer


class PetView(APIView):
    def post(self, req: Request) -> Response:
        pet = PetSerializer(data=req.data)
        pet.is_valid(raise_exception=True)
        return Response(model_to_dict(pet), status.HTTP_201_CREATED)
