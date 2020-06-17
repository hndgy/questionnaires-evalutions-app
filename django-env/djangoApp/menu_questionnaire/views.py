from rest_framework.response import Response
from menu_questionnaire.models import Questionnaire, Utilisateur, Question, ReponseUser, Reponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from menu_questionnaire import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            print(serializer.data)
            utilisateur = serializer.save()
            data['sucess']= "Vous etes correctement enregistré."
            data['id'] = utilisateur.id
            token = Token.objects.get(user=utilisateur).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_question_views(request, idG):
    try:
        question = Question.objects.get(id = idG)
    except Question.DoesNotExist:
        return Response(data = {"success" : "cette question n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        print(question.list_reponse)
        serializer = serializers.QuestionGetSerializers(question)
        print(serializer)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_Utilisateur_views(request, idG):
    try:
        question = Question.objects.get(id = idG)
    except Question.DoesNotExist:
        return Response(data = {"success" : "cette question n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionSerializers(question)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_questionnaire_views(request, idQ):
    try:
        questionnaire = Questionnaire.objects.get(id = idQ)
    except Questionnaire.DoesNotExist:
        return Response(data = {"success" : "ce questionnaire n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionnaireGetSerializers(questionnaire)
        return Response(serializer.data)


class QuestionViews(viewsets.ModelViewSet):
    """
    retourne la liste des question
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializers

@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_save_reponseUser_views(request):
    if request.method == "POST":
        questionnaire = Questionnaire.objects.get(id = request.data[0]['FK_Questionnaire'])
        user = Utilisateur.objects.get(id = request.data[0]['FK_Utilisateur'])
        questionnaire.listRepondant.add(user)
        for elem in request.data:
            serializer = serializers.ReponseUserSerializers(data=elem)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)
        return Response(data = {"sucess" : "les reponses ont été correctement enregistré"}, status = status.HTTP_201_CREATED)
    return Response(data={"error" : "mauvaise requete"}, status= status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_put_questionnaire_views(request, idQ):
    try:
        questionnaire = Questionnaire.objects.get(id = idQ)
    except Questionnaire.DoesNotExist:
        return Response({"sucess" : "ce questionnaire n'existe pas"})
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        serializer = serializers.QuestionnaireSerializers(questionnaire, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_Etudiant_views(request, num, password):
    try:
        etudiant = Utilisateur.objects.get(num = num, password = password)
    except Utilisateur.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.UtilisateurSerializer(etudiant)
        print(serializer.data['prenom'])
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_update_question_views(request, idQ):
    try:
        question = Question.objects.get(id = idQ)
    except Utilisateur.DoesNotExist:
        return Response({"sucess" : "cet utilisateur n'existe pas"})
    user = request.user
    print(user)
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        serializer = serializers.QuestionSerializers(question, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['sucess']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(data = {"success" : "information non valide"} , status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_delete_question_views(request, idQ):
    try:
        question = Question.objects.get(id = idQ)
    except Question.DoesNotExist:
        return Response(data = {"success" : "cet question n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "DELETE":
        operation = question.delete()
        data={}
        if operation :
            data['sucess']= 'bien supprimé'
        else:
            data['sucess'] = 'suppression echoué'
        return Response(data)


@api_view(['DELETE'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_delete_questionnaire_views(request, idQ):
    try:
        questionnaire = Questionnaire.objects.get(id = idQ)
    except Questionnaire.DoesNotExist:
        return Response(data = {"success" : "ce questionnaire n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "DELETE":
        operation = questionnaire.delete()
        data={}
        if operation :
            data['sucess']= 'bien supprimé'
        else:
            data['sucess'] = 'suppression echoué'
        return Response(data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_type_question_views(request, idQ):
    try:
        question = Question.objects.get(id = idQ)
    except Utilisateur.DoesNotExist:
        return Response(data = {"success" : "cet question n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionSerializers(question)
        data={}
        count = 0
        print(serializer.data['list_reponse'])
        for cle in serializer.data['list_reponse']:
            count += 1
        if count > 1:
            data["sucess"]= "multiple"
        elif count == 1:
            data["sucess"] = "fermé"
        else:
            data["sucess"] = "ouverte"
        return Response(data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_create_reponse_views(request):
    if request.method == "POST":
        serializer = serializers.ReponseSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_utilisateur_reponse(request, idQ, idU):
    try:
        reponserUser = ReponseUser.objects.get(FK_Utilisateur = idU, FK_Questionnaire=idQ)
    except Utilisateur.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'a pas encore répondu a ce questionnaire"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.QuestionSerializers(question)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_reponse_views(request, idR):
    try:
        reponse = Reponse.objects.get(id = idR)
        print(reponse)
    except Reponse.DoesNotExist:
        return Response(data = {"success" : "cette reponse n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.ReponseSerializers(reponse)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_Etudiant_views(request, num, password):
    try:
        etudiant = Utilisateur.objects.get(num = num, password = password)
    except Utilisateur.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = serializers.UtilisateurSerializer(etudiant)
        return Response(serializer.data)

@api_view(['GET'])
def api_get_questionnaire_all_views(request):
    try:
        questionnaire = Questionnaire.objects.all()
    except Questionnaire.DoesNotExist:
        return Response(data = {"success" : "il n'y a pas de questionnaire en base"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data= []
        for elem in questionnaire:
            serializer = serializers.QuestionnaireSerializers(elem)
            data.append(serializer.data)
        return Response(data)


@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_put_reponse_views(request, idR):
    try:
        reponse = Reponse.objects.get(id = idR)
    except Reponse.DoesNotExist:
        return Response({"sucess" : "cette reponse n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        serializer = serializers.ReponseSerializers(reponse, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_delete_reponse_views(request, idQ):
    try:
        reponse = Reponse.objects.get(id = idQ)
    except Reponse.DoesNotExist:
        return Response(data = {"success" : "cette reponse n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "DELETE":
        operation = reponse.delete()
        data={}
        if operation :
            data['sucess']= 'bien supprimé'
        else:
            data['sucess'] = 'suppression echoué'
        return Response(data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_utilisateur_reponse(request, idU, idQ):
    try:
        reponse = ReponseUser.objects.filter(FK_Utilisateur_id = idU, FK_Questionnaire_id = idQ).values()
    except Reponse.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'a pas répondu a ce questionnaire ou n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        print("ici")
        if not reponse:
            return Response(data = {"error" : "cette utilisateur n'a jamais participé a ce questionnaire"},status= status.HTTP_400_BAD_REQUEST)
        else:
            for elem in reponse:
                serializer = serializers.ReponseUserGetSerializers(reponse)
                return Response(serializer.data)
    return Response(data = {"error" : "mauvaise requete"},status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_delete_reponse_views(request, idU):
    try:
        utilisateur = Utilisateur.objects.get(id = idU)
    except Utilisateur.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "DELETE":
        operation = utilisateur.delete()
        data={}
        if operation :
            data['sucess']= 'bien supprimé'
        else:
            data['sucess'] = 'suppression echoué'
        return Response(data)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_utilisateur_question_reponse(request, idU, idQ, idQu):
    try:
        reponse = ReponseUser.objects.filter(FK_Utilisateur = idU, FK_Questionnaire = idQ, FK_Question=idQu).values()
    except Reponse.DoesNotExist:
        return Response(data = {"success" : "cet utilisateur n'a pas répondu a ce questionnaire ou n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if request.method == "GET":
        data = {}
        cnt = 0
        for cle in reponse:
            cnt+=1
            serializer = serializers.ReponseUserGetSerializers(cle)
            data['reponse'+str(cnt)] = serializer.data
        print(serializer.data)
        return Response(data)

@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_update_user_views(request, idU):
    try:
        reponse = Utilisateur.objects.get(id = idU)
    except Reponse.DoesNotExist:
        return Response({"sucess" : "cet utilisateur n'existe pas"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        serializer = serializers.UtilisateurSerializer(reponse, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_create_questionnaire_views(request):
    if request.method == "POST":
        serializer = serializers.QuestionnaireSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_create_question_views(request):
    if request.method == "POST":
        list_question = []
        for elem in request.data:
            list_reponse = []
            bonne_reponse = []
            for e in elem['list_reponse']:
                for u in elem['bonne_reponse']:
                    if e == u:
                        serializer = serializers.ReponseSerializers(data={'reponse' : u})
                        if serializer.is_valid():
                            serializer.save()
                            list_reponse.append(serializer.data['id'])
                            bonne_reponse.append(serializer.data['id'])
                    else:
                        serializer = serializers.ReponseSerializers(data={'reponse' : e})
                        if serializer.is_valid():
                            serializer.save()
                            list_reponse.append(serializer.data['id'])
            elem['list_reponse'] = list_reponse
            elem['bonne_reponse'] = bonne_reponse
            serializer = serializers.QuestionSerializers(data=elem)
            if serializer.is_valid():
                serializer.save()
                list_question.append(serializer.data['id'])
        questionnaire = Questionnaire.objects.get(id = request.data[0]['FK_Questionnaire'])
        loop = Questionnaire.objects.get(id = request.data[0]['FK_Questionnaire']).question.all()
        for elem in loop:
            list_question.append(elem.id)
        print(list_question)
        serializer = serializers.QuestionnaireUpdateSerializers(questionnaire, data = {"question" : list_question})
        if serializer.is_valid():
            print('ici')
            print(serializer)
            serializer.save()
        return Response(data = {"succes" : "donnée correctement ajouté et liste de question du questionnaire actualisé"}, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_put_question_questionnaire_views(request, idQuest, idQ):
    try:
        question = Question.objects.get(id = idQuest, FK_Questionnaire = idQ)
    except Question.DoesNotExist:
        return Response({"sucess" : "cette question n'est pas associé au questionnaire indiqué"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        serializer = serializers.QuestionSerializers(question, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    return Response(data = {"succes" : "erreur de requête"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_add_question_questionnaire_views(request, idQuest, idQ):
    user = request.user
    if user.role != "professeur":
        return Response({"succes" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "PUT":
        list_question = []
        questionnaire = Questionnaire.objects.get(id = idQ)
        question = Questionnaire.objects.get(id = idQ).question
        for elem in question.all():
            if elem.id == int(idQuest):
                return Response({"succes" : "Cette question est déjà associé a ce questionnaire."})
            list_question.append(elem.id)
        list_question.append(idQuest)
        serializer = serializers.QuestionnaireUpdateSerializers(questionnaire, data = {"question" : list_question})
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success']= 'bien modifié'
            return Response(data = data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    return Response(data = {"succes" : "erreur de requête"}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_delete_question_questionanire_views(request, idQuest, idQ):
    try:
        question = Question.objects.get(id = idQuest, FK_Questionnaire = idQ)
    except Question.DoesNotExist:
        return Response(data = {"success" : "cette question n'existe pas ou n'est pas associé aux questionnaires indiqués"}, status= status.HTTP_404_NOT_FOUND)
    user = request.user
    if user.role != "professeur":
        return Response({"success" : "Vous n'avez pas la permission de modifier ceci."})
    if request.method == "DELETE":
        operation = question.delete()
        data={}
        if operation :
            data['sucess']= 'bien supprimé'
        else:
            data['sucess'] = 'suppression echoué'
        return Response(data)
