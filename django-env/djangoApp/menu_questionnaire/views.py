from rest_framework import viewsets
from .serializers import UtilisateurSerializer, UtilisateurMiniSerializer, QuestionnaireSerializers, \
    QuestionSerializers, ReponseSerializers
from .models import Utilisateur, Questionnaire, Question, Reponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from menu_questionnaire import serializers


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def list(self, request, *args, **kwargs):
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurMiniSerializer(utilisateurs, many=True)
        return Response(serializer.data)


class QuestionnaireViews(viewsets.ModelViewSet):
    """
    retourne la liste des Questionnaires
    """
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializers

    def list(self, request, *args, **kwargs):
        questionnaires = Questionnaire.objects.all()
        serializer = UtilisateurMiniSerializer(questionnaires, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_get_question_views(request, idG):
    try:
        question = Question.objects.get(id=idG)
    except Question.DoesNotExist:
        return Response(data={"error : cette question n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionSerializers(question)
        return Response(serializer.data)


@api_view(['GET'])
def api_get_questionnaire_views(request, idQ):
    try:
        questionnaire = Questionnaire.objects.get(id=idQ)
    except Questionnaire.DoesNotExist:
        return Response(data={"error : ce questionnaire n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionnaireSerializers(questionnaire)
        return Response(serializer.data)


class QuestionViews(viewsets.ModelViewSet):
    """
    retourne la liste des question
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializers


@api_view(['POST'])
def api_create_utilisateur_views(request):
    if request.method == "POST":
        serializer = serializers.UtilisateurSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_reponse_views(request):
    if request.method == "POST":
        print(request.data)
        serializer = serializers.ReponseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_put_questionnaire_views(request, idQ):
    questionnaire = Questionnaire.objects.get(id=idQ)
    if request.method == "PUT":
        serializer = serializers.QuestionnaireSerializers(questionnaire, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['sucess'] = 'bien modifié'
            return Response(data=data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_creer_reponse_views(request, idQ, idU):
    question = Question.objects.get(id=idQ)
    utilisateur = Utilisateur.objects.get(id=idU)
    if request.method == "POST":
        serializer = serializers.ReponseSerializers(question, utilisateur, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['sucess'] = 'bien ajouté'
            return Response(data=data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
