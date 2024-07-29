from django.db import models

# Create your models here.


class Texts(models.Model):

    name = models.CharField(verbose_name="Name", max_length=100)
    text = models.CharField(verbose_name="Text", max_length=4000)
    translation = models.CharField(verbose_name="Translation", max_length=4000)

    def __str__(self):
        return self.name + " " + self.text + " " + self.translation