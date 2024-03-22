from persona.models import Persona
from persona.api.serializer import PersonaSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class RegistrarPersonaViews(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers

    def create(self, request, *args, **kwargs):
        try:
            # Verificar si algún campo está vacío
            for key, value in request.data.items():
                if not value:
                    return Response({"titulo": f"El campo '{key}' no puede estar vacío"}, status=status.HTTP_400_BAD_REQUEST)

            # Verificar si ya existe una persona con el mismo documento o correo
            documento = request.data.get('documento')
            correo = request.data.get('correo')

            if Persona.objects.filter(documento=documento).exists():
                return Response({"titulo": "Ya existe una persona con este documento"})

            if Persona.objects.filter(correo=correo).exists():
                return Response({"titulo": "Ya existe una persona con este correo electrónico"})

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={"titulo": "Creado con éxito", "persona": serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response(data={"titulo": f"Error al crear el persona: {str(ve)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"titulo": f"Error al crear el persona: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



