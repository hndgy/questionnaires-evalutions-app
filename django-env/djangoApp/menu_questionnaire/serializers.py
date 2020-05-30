from rest_framework import serializers
from menu_questionnaire import models
from django.contrib.auth import update_session_auth_hash
from menu_questionnaire.models import ReponseEtudiant

class QuestionnaireSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = ('id', 'url', 'nom', 'listQuestion')
        depth = 1

class QuestionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'url', 'libelle', 'reponse')
        depth = 1

class ReponseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Reponse
        fields = ('id', 'libelle', 'point')
        depth = 1


class ReponseEtudiantSerializers(serializers.Serializer):
    class Meta:
        model = ReponseEtudiant
        fields = ('FK_Question', 'FK_Questionnaire', 'FK_Etudiant', 'ReponseEtu')

    def create(self, validated_data):
        reponseEtu = ReponseEtu(
            FK_Question = validated_data['FK_Question'],
            FK_Questionnaire = validated_data['FK_Questionnaire'],
            FK_Etudiant = validated_data['FK_Etudiant'],
            ReponseEtu = validated_data['ReponseEtu']
        )
        reponseEtu.save()
        return ReponseEtu

class EtudiantSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Etudiant
        fields = ('pseudo', 'password', 'TableauEtu')

    def create(self, validated_data):
        etudiant = models.Etudiant.objects.create(**validated_data)
        return etudiant

    def update(self, instance, validated_data):
        instance.pseudo = validated_data.get('pseudo', instance.pseudo)
        instance.password = validated_data.get('password', instance.password)
        instance.TableauEtu = validated_data.get('TableauEtu', instance.TableauEtu)
        instance.save()

        return instance
