from rest_framework import serializers
from menu_questionnaire.models import Questionnaire, Utilisateur, Question, ReponseUser, Reponse
from django.contrib.auth import update_session_auth_hash
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class QuestionnaireSerializers(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ('id', 'libelle', 'prof', 'listRepondant', 'question')

class QuestionnaireGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'libelle', 'prof', 'listRepondant', 'question_value')

    question_value = serializers.SerializerMethodField('get_question_value')

    def get_question_value(self, obj):
        data=[]
        for elem in obj.question.all():
            b=[]
            for e in elem.list_reponse.all():
                print('ici')
                b.append({"id" : e.id, "reponse": e.reponse})
            a = {"id" : elem.id, "libelle" : elem.libelle, "list_reponse" : b}
            data.append(dict(a))
        return data

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('nom', 'prenom', 'num', 'role', 'password')
        extra_kwargs = {
                'password' : {'write_only' : True }
        }
    def save(self):
        utilisateur = Utilisateur(
            nom = self.validated_data['nom'],
            prenom = self.validated_data['prenom'],
            num = self.validated_data['num'],
            role = self.validated_data['role'],
        )
        password = self.validated_data['password']
        utilisateur.set_password(password)
        utilisateur.save()
        return utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'nom', 'prenom', 'num', 'role')

class ReponseUserGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReponseUser
        fields = ('id', 'FK_Question_id', 'FK_Utilisateur_id', 'reponse', 'FK_Questionnaire_id')

class ReponseUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReponseUser
        fields = ('id', 'FK_Question', 'FK_Utilisateur', 'reponse', 'FK_Questionnaire')

class ReponseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reponse
        fields = ('id', 'reponse')

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'libelle', 'FK_Questionnaire', 'list_reponse', 'bonne_reponse')

class QuestionGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'libelle', 'FK_Questionnaire', 'list_reponse', 'bonne_reponse', 'reponse_value')

    reponse_value = serializers.SerializerMethodField('get_reponse_value')

    def get_reponse_value(self, obj):
        data={}
        for elem in obj.list_reponse.all():
            data[elem.id] = elem.reponse
        return data


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })
