from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, MarcaViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"productos", ProductoViewSet)

urlpatterns = router.urls
