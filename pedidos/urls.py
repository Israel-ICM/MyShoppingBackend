from rest_framework.routers import DefaultRouter

from .views import PedidoViewSet, DetallePedidoViewSet

router = DefaultRouter()
router.register(r"pedidos", PedidoViewSet)
router.register(r"detalles-pedido", DetallePedidoViewSet)

urlpatterns = router.urls
