""" from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer


class ProductoViewsets(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer """

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer
from rest_framework.exceptions import ValidationError

class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        try:
            """ queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True) """
            queryset = Producto.objects.filter(estado=1)
            if not queryset.exists():
                return Response({"titulo": "No se encontro ningun producto."}, status=status.HTTP_302_FOUND)
            serializer = ProductoSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message": f"Error al obtener la lista de productos: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductoCreateView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Verificar si algún campo está vacío
            for key, value in request.data.items():
                if not value:
                    return Response({"titulo":f"El campo '{key}' no puede estar vacío"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={"titulo": "Creado con éxito", "producto": serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response(data={"titulo": f"Error al crear el producto: {str(ve)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"titulo": f"Error al crear el producto: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductoRetrieveView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            queryset = Producto.objects.filter(id=pk, estado=1)
            if not queryset.exists():
                return Response({"titulo": "No se encontro ningun producto relacionado con el id relacionado."}, status=status.HTTP_302_FOUND)
            serializer = ProductoSerializer(queryset, many=True)
            """ producto = self.get_object()
                serializer = self.get_serializer(producto) """
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"titulo": f"Error al recuperar el producto: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductoUpdateView(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"titulo": f"Error al actualizar el producto: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductoDestroyView(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(data={"message": "Producto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(data={"message": f"Error al eliminar el producto: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
