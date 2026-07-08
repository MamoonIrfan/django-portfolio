from django.db import models


class Skill(models.Model):

    CATEGORY_CHOICES = [

        ("Programming Languages", "Programming Languages"),

        ("Web Development", "Web Development"),

        ("Database", "Database"),

        ("Computer Science Skills", "Computer Science Skills"),

        ("Tools", "Tools"),

    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name