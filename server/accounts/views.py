from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.

class UserApiView(APIView):

    def get(self, request):
        serializer = UserSerializer
        return Response(serializer.data)