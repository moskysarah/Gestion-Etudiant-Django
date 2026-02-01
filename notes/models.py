from django.db import models

# =========================
# MODELE ETUDIANT
# =========================
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.prenom} {self.nom}"


# =========================
# MODELE COURS
# =========================
class Cours(models.Model):
    nom = models.CharField(max_length=100)
    coefficient = models.FloatField(default=1.0) 

    def __str__(self):
        return self.nom


# =========================
# MODELE NOTE
# =========================
class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    valeur = models.FloatField()

    def __str__(self):
        return f"{self.etudiant} - {self.cours} : {self.valeur}"
