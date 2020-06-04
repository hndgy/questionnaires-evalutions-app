from rest_framework import serializers
from menu_questionnaire.models import Questionnaire, Utilisateur, Question, Reponse
from django.contrib.auth import update_session_auth_hash

class QuestionnaireSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'libelle', 'prof', 'listRepondant', 'question')

class UtilisateurSerializers(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'nom', 'prenom', 'num', 'role', 'password']

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'libelle', 'FK_Questionnaire', 'list_reponse', 'question')

class ReponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = ('id', 'FK_Question', 'FK_Utilisateur', 'listReponse')
