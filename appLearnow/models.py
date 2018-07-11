from django.db import models

# Create your models here.

# >>> 8 crear instancias de objetos para una base de datos sencillas

class learNow(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text