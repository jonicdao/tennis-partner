from django.db import models

# Create your models here.

LEVEL_CHOICES = [
    ('1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5', '5.0', '5.5', '6.0')
]

class Partner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=254)
    description = models.TextField(default = "I'm a great player")

    class Meta:
        verbose_name = ("partner")
        verbose_name_plural = ("partners")

    def __str__(self):
        return self.last_name