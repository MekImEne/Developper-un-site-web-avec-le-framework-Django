from django.db import models
from django.utils import timezone
from django.contrib import admin

from crepes_bretonnes.blog.views import renommage


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.titre


class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom


class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre',
                                      related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")

    def __str__(self):
        return self.nom


class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom


class Document(models.Model):
    nom = models.CharField(max_length=100)
    doc = models.FileField(upload_to=renommage, verbose_name="Document")