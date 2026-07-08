from django.shortcuts import render
from .models import Project
from bio.models import Bio


def projects(request):

    academic_projects = Project.objects.filter(category="Academic")

    professional_projects = Project.objects.filter(category="Professional")

    personal_projects = Project.objects.filter(category="Personal")

    bio = Bio.objects.first()

    return render(request, "projects.html", {

        "academic_projects": academic_projects,

        "professional_projects": professional_projects,

        "personal_projects": personal_projects,

        "bio": bio,

    })