from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Productos.views import TipoAPI, ProductoAPI


#localhost:8000/productos/api/crud/tipo

router = DefaultRouter()
router.register('tipo', TipoAPI)
router.register('producto', ProductoAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]