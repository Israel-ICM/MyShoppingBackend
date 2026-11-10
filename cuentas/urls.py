from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"clientes", ClienteViewSet)

urlpatterns = router.urls
