# Generated by Django 3.0.5 on 2020-06-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_questionnaire', '0003_auto_20200604_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='listRepondant',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='listRepondant',
            field=models.ManyToManyField(to='menu_questionnaire.Utilisateur'),
        ),
    ]