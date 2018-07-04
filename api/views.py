from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from django.contrib.auth.models import User
from .serializers import UserSerializer, PasswordSerializer
from .permissions import IsUserOrRead


class UserViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um usuário
    list:
        Retorna todos os usuários
    create:
        Cria um novo usuário
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

    http_method_names = ['get', 'post', 'put', 'patch']

    @action(methods=['get'], detail=False)
    def me(self, request):
        """
        Retorna o usuario autenticado
        """
        return Response(self.serializer_class(request.user).data, status=HTTP_200_OK)

    @action(methods=['post'], detail=False, serializer_class=PasswordSerializer)
    def set_password(self, request):
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