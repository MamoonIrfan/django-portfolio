from django.shortcuts import render
from .models import Experience
from bio.models import Bio


def experience(request):

    experiences = Experience.objects.all()

    for exp in experiences:
        exp.points = [
            line.strip()
            for line in exp.description.split("\n")
            if line.strip()
        ]

    experience_letter = Experience.objects.exclude(
        experience_letter=""
    ).exclude(
        experience_letter=None
    ).first()

    bio = Bio.objects.first()

    return render(request, "experience.html", {

        "experiences": experiences,

        "experience_letter": experience_letter,

        "bio": bio,

    })