from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [

        ("Academic", "Academic"),

        ("Professional", "Professional"),

        ("Personal", "Personal"),

    ]

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="projects/",
         blank = True,
         null = True
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        blank=True
    )

    github_link = models.URLField(
        blank=True
    )

    demo_link = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.title
