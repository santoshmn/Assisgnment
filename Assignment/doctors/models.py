from django.db import models



# Create your models here.

class Doctor(models.Model):
    Name = models.CharField(max_length=1000)
    Specialty = models.CharField(max_length=500)
    Years_of_Experience = models.IntegerField()
    Photo = models.ImageField()
    Availability= models.DateTimeField()



    def __str__(self):
        return self.Name


