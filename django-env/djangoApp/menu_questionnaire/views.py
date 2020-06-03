from rest_framework import viewsets
from .serializers import EtudiantSerializer, EtudiantMiniSerializer
from .models import Etudiant
from rest_framework.response import Response


class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

    def list(self, request, *args, **kwargs):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantMiniSerializer(etudiants, many=True)
        return Response(serializer.data)