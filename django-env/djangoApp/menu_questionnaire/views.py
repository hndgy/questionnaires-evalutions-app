from django.shortcuts import render
from django.http import JsonResponse
from menu_questionnaire.models import Questionnaire
from django.core import serializers

# Create your views here.

def QuestionnaireList(request):
    """
    Retourne liste de Questionnaire
    """
    data = []
    for elem in Questionnaire.objects.all():
        data.append(elem.nom)
    return JsonResponse({"QCM" : data})
