from django.shortcuts import render
from django.http import JsonResponse
from menu_questionnaire.models import Questionnaire
from django.core import serializers

# Create your views here.

def QuestionnaireList(request):
    """
    Retourne liste de Questionnaire
    """
    print(Questionnaire)
    data = serializers.serialize('json', Questionnaire)
    return JsonResponse({"Evaluation" : data})
