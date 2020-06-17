# Generated by Django 3.0.5 on 2020-06-15 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('num', models.CharField(default='', max_length=8, unique=True)),
                ('role', models.CharField(default='etudiant', max_length=25)),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('password', models.CharField(max_length=25)),
                ('id_admin', models.BooleanField(default=False)),
                ('id_active', models.BooleanField(default=True)),
                ('id_staff', models.BooleanField(default=False)),
                ('id_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('listRepondant', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('prof', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='questionnaire_create_utilisateur', to=settings.AUTH_USER_MODEL)),
                ('question', models.ManyToManyField(blank=True, to='menu_questionnaire.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReponseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.TextField(blank=True)),
                ('FK_Question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Question')),
                ('FK_Questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Questionnaire')),
                ('FK_Utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='FK_Questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='question_questionnaire_associe', to='menu_questionnaire.Questionnaire'),
        ),
        migrations.AddField(
            model_name='question',
            name='bonne_reponse',
            field=models.ManyToManyField(blank=True, related_name='question_liste_de_bonne_reponse', to='menu_questionnaire.Reponse'),
        ),
        migrations.AddField(
            model_name='question',
            name='list_reponse',
            field=models.ManyToManyField(blank=True, related_name='question_liste_de_reponse', to='menu_questionnaire.Reponse'),
        ),
    ]
