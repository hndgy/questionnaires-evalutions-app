from django.contrib import admin
from .models import Utilisateur, Questionnaire, Question, Reponse

admin.site.register(Utilisateur)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Reponse)
