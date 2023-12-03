from rest_framework import serializers
from .models import Proyects

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyects
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)