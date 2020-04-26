from django.shortcuts import render
from django.http import JsonResponse
from menu_questionnaire.models import Questionnaire
from django.core import serializers

# Create your views here.

def QuestionnaireList(request):
    """
    Retourne liste de Questionnaire
    """
    data = Questionnaire.objects.all()
    serialize_data = serializers.serialize('python', data)
    return JsonResponse(serialize_data, safe=False)
