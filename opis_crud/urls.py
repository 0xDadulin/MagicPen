# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ulepszone-teksty/', views.ulepszony_tekst_list, name='ulepszony_tekst_list'),
    path('ulepszony-tekst/<int:tekst_id>/', views.ulepszony_tekst_detail, name='ulepszony_tekst_detail'),
    path('ulepszony-tekst/update/<int:tekst_id>/', views.ulepszony_tekst_update, name='ulepszony_tekst_update'),
]
