from django.db.models import Model, OneToOneField, ImageField, CharField, PROTECT
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your models here.
class Usuario(Model):
    perfil_user = OneToOneField(User, on_delete=PROTECT)
    # foto = ImageField(upload_to='', null=True, blank=True)

    @staticmethod
    def get_usuario_from_user(user):
        return get_object_or_404(Usuario, perfil_user=user)

    def __str__(self):
        return self.perfil_user.username