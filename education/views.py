from django.shortcuts import render
from .models import Education
from bio.models import Bio


def education(request):

    educations = Education.objects.all()

    bio = Bio.objects.first()

    return render(request, "education.html", {

        "educations": educations,

        "bio": bio,

    })