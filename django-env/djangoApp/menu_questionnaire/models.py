from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    nom = models.CharField(max_length = 50, default='')

    def __str__(self):
        return self.nom

class Reponse(models.Model):
    libelle = models.TextField(null=False)
    point = models.IntegerField(null = True)

    def __str__(self):
        return self.libelle

class Question(models.Model):
    libelle = models.TextField(null=False)
    Reponse = models.ForeignKey(Reponse, on_delete=models.PROTECT)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT, default='')

    def __str__(self):
        return self.libelle
