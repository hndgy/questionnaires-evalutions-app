from rest_framework import viewsets
from .serializers import UtilisateurSerializer, UtilisateurMiniSerializer
from .models import Utilisateur
from rest_framework.response import Response


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def list(self, request, *args, **kwargs):
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurMiniSerializer(utilisateurs, many=True)
        return Response(serializer.data)
