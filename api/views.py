from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer, UserSerializer, PasswordSerializer
from .permissions import IsUserOrRead


class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            u = User(username=serializer.data['username'], first_name=serializer.data['first_name'], last_name=serializer.data['last_name'], email=serializer.data['email'])
            u.set_password(serializer.data['password'])
            u.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=HTTP_200_OK, headers=headers)
        return Response(status=HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um usuário
    list:
        Retorna todos os usuários
    delete:
        Remove um usuário existente
    partial_update:
        Atualiza um ou mais campos de um usuário existente
    update:
        Atualiza um usuário
    """
    permission_classes = [
        IsAuthenticated, IsUserOrRead
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get', 'put', 'patch']

    @action(methods=['get'], detail=False)
    def me(self, request):
        """
        Retorna o usuario autenticado
        """
        return Response(self.serializer_class(request.user).data, status=HTTP_200_OK)

    @action(methods=['patch'], detail=True, serializer_class=PasswordSerializer)
    def set_password(self, request, pk=None):
        """
        Altera a senha do usuario autenticado
        """
        user = request.user
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=HTTP_401_UNAUTHORIZED)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response("Success", status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)