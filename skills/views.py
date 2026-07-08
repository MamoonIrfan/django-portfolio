from django.shortcuts import render
from .models import Skill
from bio.models import Bio


def skills(request):

    programming_languages = Skill.objects.filter(category="Programming Languages")

    web_development = Skill.objects.filter(category="Web Development")

    database = Skill.objects.filter(category="Database")

    computer_science_skills = Skill.objects.filter(category="Computer Science Skills")

    tools = Skill.objects.filter(category="Tools")

    bio = Bio.objects.first()

    return render(request, "skills.html", {

        "programming_languages": programming_languages,

        "web_development": web_development,

        "database": database,

        "computer_science_skills": computer_science_skills,

        "tools": tools,

        "bio": bio,

    })