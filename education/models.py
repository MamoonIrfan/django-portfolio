from django.db import models


class Education(models.Model):

    qualification = models.CharField(max_length=100)

    institute = models.CharField(max_length=200)

    year = models.CharField(max_length=50)

    result = models.CharField(max_length=100)

    def __str__(self):
        return self.qualification