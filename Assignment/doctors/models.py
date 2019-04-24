from django.db import models


class Doctor(models.Model):
    Name = models.CharField(max_length=1000)
    Specialty = models.CharField(max_length=500)
    Years_of_Experience = models.IntegerField()
    Photo = models.ImageField()

    def __str__(self):
        return self.Name


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Avail_Date = models.DateField()
    Avail_Time = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.doctor, self.Avail_Date)




