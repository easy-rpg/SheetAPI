from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from campanha.views import CampanhaViewSet, ArcoViewSet


router = routers.DefaultRouter()
router.register('campanhas', CampanhaViewSet)
router.register('arcos', ArcoViewSet)

schema_view = get_swagger_view(title='LocationTracker API')

urlpatterns = [
    path('', schema_view),
    path('router/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]