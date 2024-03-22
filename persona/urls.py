#Utilizar vistas basadas en clases (CBV)

from django.urls import path
from persona.api.views import RegistrarPersonaViews

urlpatterns = [
    # Ruta para crear un nuevo usuario
    path('persona/registrar', RegistrarPersonaViews.as_view(), name='persona-registrar'),
]