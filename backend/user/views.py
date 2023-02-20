from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import UserSerializer, AuthTokenSerializer
from user.models import User

# Create your views here.

# la peticion tiene que tener email, password y name

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ListaUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer 
    queryset = User.objects.all()

# la peticion tiene que tener email y password
class CreateTokenView(ObtainAuthToken):
    """Vista para crear un token"""
    serializer_class = AuthTokenSerializer

# la peticion tiene que tener token en el header y ser get.
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
