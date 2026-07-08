from django.db import models


class Bio(models.Model):

    name = models.CharField(max_length=100)

    job_title = models.CharField(max_length=100)

    profile_picture = models.ImageField(upload_to="profile/")

    description = models.TextField()

    career_objective = models.TextField()

    degree = models.CharField(max_length=100)

    university = models.CharField(max_length=200)

    country = models.CharField(max_length=100)

    email = models.EmailField()

    university_email = models.EmailField()

    phone = models.CharField(max_length=20, blank=True)

    github = models.URLField()

    linkedin = models.URLField()

    resume = models.FileField(upload_to="resume/")

    def __str__(self):
        return self.name


class Achievement(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    certificate = models.ImageField(upload_to="achievements/")

    def __str__(self):
        return self.title


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name