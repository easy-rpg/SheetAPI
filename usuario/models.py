from django.db.models import Model, OneToOneField, ImageField, PROTECT
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from .utils import get_usuario_upload_path


class PerfilUsuario(Model):
    user = OneToOneField(User, on_delete=PROTECT, related_name='perfil')
    foto = ImageField(upload_to=get_usuario_upload_path, null=True, blank=True)

    @staticmethod
    def get_usuario_from_user(user):
        return get_object_or_404(PerfilUsuario, user=user)

    def __str__(self):
        assert isinstance(self.user, User)
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = PerfilUsuario.objects.get(user=self.user)
                self.pk = p.pk
            except PerfilUsuario.DoesNotExist:
                pass

        super(PerfilUsuario, self).save(*args, **kwargs)


def create_usuario(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        usuario = PerfilUsuario(user=user)
        usuario.save()


post_save.connect(create_usuario, sender=User)