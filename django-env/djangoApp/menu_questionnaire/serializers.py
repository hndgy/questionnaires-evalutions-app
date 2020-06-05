from rest_framework import serializers
from .models import Utilisateur, Questionnaire, Question, Reponse

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'nom', 'prenom', 'num', 'role', 'password')

class UtilisateurMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'nom', 'prenom')

class QuestionnaireSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'libelle', 'prof', 'listRepondant', 'question')

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'libelle', 'FK_Questionnaire', 'list_reponse', 'question')

class ReponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = ('id', 'FK_Question', 'FK_Utilisateur', 'listReponse')
