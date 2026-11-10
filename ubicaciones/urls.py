from rest_framework.routers import DefaultRouter

from .views import PaisViewSet

router = DefaultRouter()
router.register(r"paises", PaisViewSet)

urlpatterns = router.urls
