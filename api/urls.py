from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, CreateUserView
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
    path('', include(router.urls)),
    path('create_user/', CreateUserView.as_view()),
    path('auth/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('ui-auth/', include('rest_framework.urls'))
]
