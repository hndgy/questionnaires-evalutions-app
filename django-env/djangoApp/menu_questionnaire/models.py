from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=25, unique=True, null=False)
    prenom = models.CharField(max_length=25, unique=True, null=False)
    num = models.BigIntegerField()
    role = models.CharField(max_length=50, null=True, default="etudiant")
    password = models.CharField(max_length=15, null=True)


class Questionnaire(models.Model):
    libelle = models.CharField(max_length=50, null=False)
    prof = models.ForeignKey(Utilisateur, on_delete=models.PROTECT, related_name="%(class)s_create_utilisateur", null=True)
    listRepondant = models.ManyToManyField(Utilisateur)
    question = models.ForeignKey("Question", on_delete=models.PROTECT, null=True, related_name="%(class)s_first_question")


class Question(models.Model):
    libelle = models.CharField(max_length=100, null=False)
    FK_Questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT, null = True, related_name="%(class)s_questionnaire_associe")
    list_reponse = models.CharField(max_length=100, null=True)
    question = models.ForeignKey("Question", on_delete=models.PROTECT, null=True, related_name='+')

class Reponse(models.Model):
    listReponse = models.CharField(null=True, max_length=100)
    FK_Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.PROTECT, null=False)
    FK_Question = models.ForeignKey(Question, on_delete=models.PROTECT, null=False)



