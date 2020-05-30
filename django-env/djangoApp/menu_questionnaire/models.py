from django.db import models

# Create your models here.
class Reponse(models.Model):
    libelle = models.TextField(null=False)
    point = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.libelle

class Question(models.Model):
    libelle = models.TextField(null=False)
    reponse = models.ManyToManyField(Reponse)

    def __str__(self):
        return self.libelle

class Questionnaire(models.Model):
    nom = models.CharField(max_length=50, default='')
    listQuestion = models.ManyToManyField(Question)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    pseudo = models.CharField(max_length=25, unique=True, null=False)
    password = models.CharField(max_length=25, unique=True, null=False)
    TableauEtu = models.ManyToManyField(Questionnaire, through='ReponseEtudiant')

    def __str__(self):
        return self.pseudo

class ReponseEtudiant(models.Model):
    FK_Question = models.ForeignKey(Question, on_delete = models.PROTECT)
    FK_Questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    FK_Etudiant = models.ForeignKey(Etudiant, on_delete = models.PROTECT)
    ReponseEtu = models.TextField(null=True)
