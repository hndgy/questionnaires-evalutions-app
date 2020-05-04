from django.shortcuts import render
from django.http import JsonResponse
from menu_questionnaire import models
from menu_questionnaire import serializers
from rest_framework import viewsets

class QuestionnaireViews(viewsets.ModelViewSet):
    """
    retourne la liste des Questionnaires
    """
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializers

class QuestionViews(viewsets.ModelViewSet):
    """
    retourne la liste des question
    """
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializers

class ReponseViews(viewsets.ModelViewSet):
    """
    retourne les reponses en base
    """
    queryset = models.Reponse.objects.all()
    serializer_class = serializers.ReponseSerializers
