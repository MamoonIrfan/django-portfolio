from django.db import models


class Experience(models.Model):

    job_title = models.CharField(max_length=150)

    company = models.CharField(max_length=200)

    duration = models.CharField(max_length=100)

    description = models.TextField()

    experience_letter = models.ImageField(
        upload_to="experience/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.job_title