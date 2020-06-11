# Generated by Django 3.0.5 on 2020-06-10 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25, unique=True)),
                ('prenom', models.CharField(max_length=25, unique=True)),
                ('num', models.CharField(default='', max_length=8, unique=True)),
                ('role', models.CharField(default='etudiant', max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ReponseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.CharField(max_length=100)),
                ('FK_Question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Question')),
                ('FK_Questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Questionnaire')),
                ('FK_Utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='listRepondant',
            field=models.ManyToManyField(to='menu_questionnaire.Utilisateur'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='prof',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='questionnaire_create_utilisateur', to='menu_questionnaire.Utilisateur'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='question',
            field=models.ManyToManyField(to='menu_questionnaire.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='FK_Questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='question_questionnaire_associe', to='menu_questionnaire.Questionnaire'),
        ),
        migrations.AddField(
            model_name='question',
            name='list_reponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu_questionnaire.Reponse'),
        ),
    ]
