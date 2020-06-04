from django.shortcuts import render
from rest_framework.response import Response
from menu_questionnaire.models import Questionnaire, Utilisateur, Question, Reponse
from menu_questionnaire import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

class QuestionnaireViews(viewsets.ModelViewSet):
    """
    retourne la liste des Questionnaires
    """
    queryset = Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializers


@api_view(['GET'])
def api_get_question_views(request, idG):
    try:
        question = Question.objects.get(id = idG)
    except Question.DoesNotExist:
        return Response(data = {"error : cette question n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionSerializers(question)
        return Response(serializer.data)

@api_view(['GET'])
def api_get_questionnaire_views(request, idQ):
    try:
        questionnaire = Questionnaire.objects.get(id = idQ)
    except Questionnaire.DoesNotExist:
        return Response(data = {"error : ce questionnaire n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
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
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_create_reponse_views(request):
    if request.method == "POST":
        serializer = serializers.ReponseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
