from rest_framework import serializers
from .models import Etudiant

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ('id', 'pseudo', 'password')

class EtudiantMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ('id', 'pseudo')