from rest_framework.routers import DefaultRouter

from .views import MovimientoStockViewSet, LoteInventarioViewSet

router = DefaultRouter()
router.register(r"movimientos-stock", MovimientoStockViewSet)
router.register(r"lotes-inventario", LoteInventarioViewSet)

urlpatterns = router.urls
