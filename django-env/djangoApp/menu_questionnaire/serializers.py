from rest_framework import serializers
from menu_questionnaire import models

class QuestionnaireSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = ('id', 'url', 'nom', 'listQuestion')
        depth = 1

            # def update(self, instance, validated_data):
            # instance.username = validated_data.get('username', instance.username)
            # instance.tagline = validated_data.get('tagline', instance.tagline)
            #
            # instance.save()
            #
            # password = validated_data.get('password', None)
            # confirm_password = validated_data.get('confirm_password', None)
            #
            # if password and confirm_password and password == confirm_password:
            #     instance.set_password(password)
            #     instance.save()
            #
            # update_session_auth_hash(self.context.get('request'), instance)
            #
            # return instance

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
