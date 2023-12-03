from proyects.models import Proyects
from rest_framework import viewsets, permissions
from .serializers import ProyectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerializer