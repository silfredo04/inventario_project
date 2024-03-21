#Utilizar vistas basadas en clases (CBV)

from django.urls import path
from inventario.api.views import ProductoListView, ProductoCreateView, ProductoRetrieveView, ProductoUpdateView, ProductoDestroyView

urlpatterns = [
    # Ruta para listar todos los productos
    path('productos/', ProductoListView.as_view(), name='producto-list'),

    # Ruta para crear un nuevo producto
    path('productos/crear/', ProductoCreateView.as_view(), name='producto-create'),

    # Ruta para obtener detalles de un producto específico
    path('productos/<int:pk>/', ProductoRetrieveView.as_view(), name='producto-detail'),

    # Ruta para actualizar un producto específico
    path('productos/<int:pk>/actualizar/', ProductoUpdateView.as_view(), name='producto-update'),

    # Ruta para eliminar un producto específico
    path('productos/<int:pk>/eliminar/', ProductoDestroyView.as_view(), name='producto-delete'),
]

#Utilizar conjuntos de vistas (ViewSet)
""" from rest_framework.routers import DefaultRouter
from inventario.api.views import ProductoViewsets

router = DefaultRouter()
router.register('productos', ProductoViewsets, basename='producto')

urlpatterns = router.urls """

