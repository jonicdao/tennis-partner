from django.db import models

# Create your models here.

class Partner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.CharField(max_length=5)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=254)
    description = models.TextField(default = "I'm a great player")

    class Meta:
        verbose_name = ("partner")
        verbose_name_plural = ("partners")

    def __str__(self):
        return self.last_name