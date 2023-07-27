from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Children(models.Model):
    classes_choix = (
        ('Petite Section', 'Petite Section'),
        ('Moyenne Section', 'Moyenne Section'),
        ('Grande Section', 'Grande Section'),
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=100)
    phone_parent = models.CharField(max_length=20)
    email_parent = models.EmailField()
    address = models.CharField(max_length=50)
    date_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    classes = models.CharField(max_length=15, choices=classes_choix)

    def __str__(self):
        return f"{self.nom} - {self.prenom}"

class Note(models.Model):
    classes_choix = (
        ('Petite Section', 'Petite Section'),
        ('Moyenne Section', 'Moyenne Section'),
        ('Grande Section', 'Grande Section'),
    )

    children = models.ForeignKey(Children, on_delete=models.CASCADE)
    classes = models.CharField(max_length=15, choices=classes_choix, editable=False)
    Dessin = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    Ecriture = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    Chant = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Ajoutez default=0.0 ici
    Cumule = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, editable=False)

    def calculer_moyenne(self):
        return (self.Dessin + self.Ecriture + self.Chant) / 3

    def save(self, *args, **kwargs):
        self.Cumule = self.calculer_moyenne()
        super(Note, self).save(*args, **kwargs)

    def set_classes(self):
        if self.children:
            self.classes = self.children.classes

@receiver(pre_save, sender=Note)
def update_classes(sender, instance, **kwargs):
    instance.set_classes()

class Message(models.Model):
    nom_prenom = models.CharField(max_length=100)
    email = models.EmailField()
    objet = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.nom_prenom