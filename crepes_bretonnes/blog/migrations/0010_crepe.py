# Generated by Django 3.0.4 on 2020-03-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_commentaire_cours_eleve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crepe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_recette', models.CharField(max_length=255)),
                ('prix', models.IntegerField()),
            ],
        ),
    ]
