# Generated by Django 3.0.5 on 2020-05-30 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_questionnaire', '0013_auto_20200504_2010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionnaireQuestion',
            new_name='ReponseEtudiant',
        ),
    ]