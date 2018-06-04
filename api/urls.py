from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import UserViewSet
from campanha.views import CampanhaViewSet, ArcoViewSet
from core.views import ClasseViewset
from personagem.views import PersonagemViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('campanhas', CampanhaViewSet)
router.register('arcos', ArcoViewSet)
router.register('classes', ClasseViewset)
router.register('personagems', PersonagemViewSet)

schema_view = get_swagger_view(title='LocationTracker API')

urlpatterns = [
    path('', schema_view),
    path('router/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]