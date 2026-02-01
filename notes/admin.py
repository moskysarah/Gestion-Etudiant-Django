from django.contrib import admin
from .models import Etudiant, Cours, Note

# Evite d'enregistrer deux fois avec try/except
for model in (Etudiant, Cours, Note):
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
