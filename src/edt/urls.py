from django.urls import path

from .views import edt, home

urlpatterns = [
    path('edt/<str:id_groupe>/', edt, name='edt-index'),
    path('home/', home, name='edt-home'),
]

