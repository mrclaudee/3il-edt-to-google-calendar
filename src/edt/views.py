from edt.utils.api import extract_edt

from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("<h2>Login from edt app.</h2>")


def edt_list(request):
    return render(request, "edt/edt-list.html")


def edt(request, id_groupe):
    items = extract_edt(id_groupe)
    return HttpResponse(items)
