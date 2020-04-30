from django.db import models

# Create your models here.
class Etudiant(models.Model):
    pseudo = models.CharField(max_length=25, unique=True, null=False)
    password = models.TextField(null=False)

    def __str__(self):
        return self.pseudo

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


class QuestionReponse(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete= models.PROTECT, null=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True)
    reponse = models.ForeignKey(Reponse,   on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self
