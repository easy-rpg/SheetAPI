from rest_framework.serializers import ModelSerializer
from .models import Classe


class ClasseSerializer(ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'
