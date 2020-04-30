from rest_framework import serializers
from menu_questionnaire import models

class QuestionnaireSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = ('nom', 'listQuestion')
        depth = 1

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'
        depth = 1
