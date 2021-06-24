from django.db import models

# Create your models here.
class FirstModel(models.Model):
    box_1 = models.CharField(max_length=300)
    box_2 = models.CharField(max_length=300)
    box_3 = models.CharField(max_length=300)
    box_4 = models.CharField(max_length=300)

    def __str__(self):
        return self.box_1
