from rest_framework import viewsets

from .models import Contenedor
from .serializers import ContenedorSerializer

#Use viewsets.ModelViewSet cuando va a permitir todas o la mayoría de las operaciones CRUD en un modelo.
class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer