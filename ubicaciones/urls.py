from rest_framework.routers import DefaultRouter

from .views import PaisViewSet, RegionViewSet

router = DefaultRouter()
router.register(r"paises", PaisViewSet)
router.register(r"regiones", RegionViewSet)

urlpatterns = router.urls
