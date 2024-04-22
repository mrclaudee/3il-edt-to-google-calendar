from django.urls import path

from .views import edt, edt_list

urlpatterns = [
    path('edt/', edt_list, name='edt-index'),
    path('edt/<str:id_groupe>/', edt, name='edt-group'),
]

