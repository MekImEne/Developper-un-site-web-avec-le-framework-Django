# Generated by Django 3.0.4 on 2020-03-20 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article2_image_lieu_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestoProxy',
            fields=[
            ],
            options={
                'ordering': ['nom'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.restaurant',),
        ),
    ]
