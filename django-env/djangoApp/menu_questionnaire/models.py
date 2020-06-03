from django.db import models

# Create your models here.
class Etudiant(models.Model):
    pseudo = models.CharField(max_length=25, unique=True, null=False)
    password = models.CharField(max_length=10, null=False)



"""
class Questionnaire(models.Model):
    nom = models.CharField(max_length=50, default='')
    dateCreation = models.DateTimeField(null=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self

class Question(models.Model):
    libelle = models.TextField(null=False)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self

class Reponse(models.Model):
    libelle = models.TextField(null=False)
    point = models.IntegerField(null=False, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self

class QuestionReponse(models.Model):
    dateReponse = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    reponse = models.ForeignKey(Reponse,   on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self

"""
