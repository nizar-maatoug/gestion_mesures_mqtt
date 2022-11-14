from django.db import models

# Create your models here.

class Grandeur(models.Model):
    nom=models.CharField(max_length=60)
    unite=models.CharField(max_length=30)
    valeurMin=models.FloatField()
    valeurMax=models.FloatField()

    def __str__(self):
        return f"Grandeur: {self.nom} Unité: {self.unite} valeurs entre {self.valeurMin} et {self.valeurMax}"

class Mesure(models.Model):
    valeur=models.FloatField()
    datePrise=models.DateTimeField()
    grandeur=models.ForeignKey(Grandeur, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mesure: {self.valeur} at {self.datePrise}"
