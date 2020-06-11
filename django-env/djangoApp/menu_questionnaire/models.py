from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import UserManager, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,num,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not num:
            raise ValueError('Users must have a num')

        user = self.model(
            num= num,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, num, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            num = num,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=25, unique=False, null=False)
    prenom = models.CharField(max_length=25, unique=False, null=False)
    num = models.CharField(max_length=8, unique=True, null = False, default="")
    role = models.CharField(max_length=25, unique=False, null = False, default="etudiant")
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    password = models.CharField(max_length=25,unique=False, null = False )
    id_admin = models.BooleanField(default = False)
    id_active = models.BooleanField(default = True)
    id_staff = models.BooleanField(default = False)
    id_superuser = models.BooleanField(default = False)

    objects = UserManager()


    USERNAME_FIELD = 'num'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return self.nom

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Questionnaire(models.Model):
    libelle = models.CharField(max_length=50, null = False)
    prof = models.ForeignKey(Utilisateur, on_delete = models.PROTECT, related_name="%(class)s_create_utilisateur", null = False, default ="")
    listRepondant = models.ManyToManyField(Utilisateur)
    question = models.ManyToManyField("Question", blank = True)


class Reponse(models.Model):
    reponse = models.TextField(max_length= 100, null=False)

    def __str__(self):
        return self.reponse

class Question(models.Model):
    libelle = models.TextField(null=False)
    FK_Questionnaire = models.ForeignKey(Questionnaire, on_delete = models.PROTECT, null = True, related_name="%(class)s_questionnaire_associe")
    list_reponse = models.ManyToManyField(Reponse, blank = True, related_name="%(class)s_liste_de_reponse")
    bonne_reponse = models.ManyToManyField(Reponse, blank = True, related_name="%(class)s_liste_de_bonne_reponse")

    def __str__(self):
        return self.libelle

class ReponseUser(models.Model):
    FK_Questionnaire = models.ForeignKey(Questionnaire, on_delete = models.PROTECT, null = True)
    reponse = models.TextField(blank = True)
    FK_Utilisateur = models.ForeignKey(Utilisateur, on_delete = models.PROTECT, null = True)
    FK_Question = models.ForeignKey(Question, on_delete = models.PROTECT, null = True)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
