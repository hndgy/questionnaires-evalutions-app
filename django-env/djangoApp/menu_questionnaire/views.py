from django.shortcuts import render
from django.http import JsonResponse
from menu_questionnaire import models
from menu_questionnaire import serializers
from rest_framework import viewsets


class QuestionnaireViews(viewsets.ReadOnlyModelViewSet):
    """
    retourne la liste des Questionnaires
    """
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializers

class QuestionViews(viewsets.ReadOnlyModelViewSet):
    """
    retourne la liste des question
    """
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializers
