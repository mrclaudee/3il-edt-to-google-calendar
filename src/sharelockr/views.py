import os

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from dotenv import load_dotenv

load_dotenv()


def index(request):
    return render(request, "sharelockr/index.html", context={'google_id': os.getenv('GOOGLE_ID_CLIENT')})


def logout_view(request):
    logout(request)
    return redirect('index')
