import os
from datetime import datetime

from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def index(request):
    return render(request, "sharelockr/index.html", context={'google_id': os.getenv('GOOGLE_ID_CLIENT')})

