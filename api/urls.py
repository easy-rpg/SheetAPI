from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import UserViewSet
from campanha.views import CampanhaViewSet, ArcoViewSet
from core.views import ClasseViewset
from personagem.views import PersonagemViewSet, PersonagemClasseViewSet, PersonagemModeloViewSet, \
    PersonagemAtributoViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('campanha', CampanhaViewSet)
router.register('arco', ArcoViewSet)
router.register('classe', ClasseViewset)
router.register('personagem', PersonagemViewSet)
router.register('personagem_classe', PersonagemClasseViewSet)
router.register('personagem_modelo', PersonagemModeloViewSet)
router.register('personagem_atributo', PersonagemAtributoViewSet)

schema_view = get_swagger_view(title='RPG Sheet API')

urlpatterns = [
    path('', schema_view),
    path('router/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
