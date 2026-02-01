
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from myapp.models import Word
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        word_text = request.POST.get("word")

        # Save user (demo purpose)
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"password": "plain-password"}
        )

        # Save password (demo)
        Word.objects.create(user=user, word=word_text)

        # Detect device
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown Device")

        return render(request, "welcome.html", {
            "username": username,
            "device": user_agent
        })

    return render(request, "index.html")

def logout_view(request):
    
    return redirect('login')


def dashboard_view(request):
    users = User.objects.all().order_by("-id")
    return render(request, "dashboard.html", {"users": users})


def user_link_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "user_page.html", {"user": user})
