from django.shortcuts import render, redirect
from .models import Bio, Achievement, ContactMessage


def home(request):

    bio = Bio.objects.first()

    return render(request, "index.html", {
        "bio": bio
    })


def about(request):

    bio = Bio.objects.first()

    return render(request, "about.html", {
        "bio": bio
    })


def achievements(request):

    achievements = Achievement.objects.all()

    bio = Bio.objects.first()

    return render(request, "achievements.html", {

        "achievements": achievements,

        "bio": bio,

    })


def contact(request):

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact")

    bio = Bio.objects.first()

    return render(request, "contact.html", {
        "bio": bio
    })