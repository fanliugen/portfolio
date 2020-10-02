from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(max_length=100)
    # class Meta:
    #     verbose_name = "Gallery"
    #     verbose_name_plural = "Gallerys"

    # def __str__(self):
    #     pass
