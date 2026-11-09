from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/cuentas/', include('cuentas.urls')),
    path('api/catalogo/', include('catalogo.urls')),
    path('api/pedidos/', include('pedidos.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/ubicaciones', include('ubicaciones.urls'))
]
