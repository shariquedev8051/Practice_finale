from django.db import models
from django.urls import reverse

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

class Adress(models.Model):

    

    class Meta:
        verbose_name = _("adress")
        verbose_name_plural = _("adresss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("adress_detail", kwargs={"pk": self.pk})
