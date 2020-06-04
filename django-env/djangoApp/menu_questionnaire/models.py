from django.db import models
# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=25, unique=True, null=False)
    prenom = models.CharField(max_length=25, unique=True, null=False)
    num = models.CharField(max_length=8, unique=True, null = False, default="")
    role = models.CharField(max_length=25, unique=True, null = False, default="etudiant")
    password = models.CharField(max_length=25,unique=True, null = False )

    def __str__(self):
        return self.nom

class Questionnaire(models.Model):
    libelle = models.CharField(max_length=50, null = False)
    prof = models.ForeignKey(Utilisateur, on_delete = models.PROTECT, related_name="%(class)s_create_utilisateur", null = True)
    listRepondant = models.ForeignKey(Utilisateur, on_delete = models.PROTECT,related_name="%(class)s_liste_utilisateur", null = True)
    question = models.ForeignKey("Question", on_delete= models.PROTECT, null = True, related_name="%(class)s_first_question")

    def __str__(self):
        return self.libelle

class Question(models.Model):
    libelle = models.CharField(max_length= 100, null=False)
    FK_Questionnaire = models.ForeignKey(Questionnaire, on_delete = models.PROTECT, null = True, related_name="%(class)s_questionnaire_associe")
    list_reponse = models.CharField(max_length = 100, null = True)
    question = models.ForeignKey("Question", on_delete = models.PROTECT, null = True, related_name='+')

    def __str__(self):
        return self.libelle

class Reponse(models.Model):
    listReponse = models.CharField(null=True, max_length = 100)
    FK_Utilisateur = models.ForeignKey(Utilisateur, on_delete = models.PROTECT, null = False)
    FK_Question = models.ForeignKey(Question, on_delete = models.PROTECT, null = False)

    def __str__(self):
        return self.libelle
