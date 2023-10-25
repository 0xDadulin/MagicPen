from django.urls import path
from .views import signup, login_view, logout_view,generuj_opis,toggle_ulubiony,aktualizuj_opis,profil,landing

urlpatterns = [
    path('generator', generuj_opis,name='generuj-opis'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('toggle-ulubiony/<int:pk>/', toggle_ulubiony, name='toggle-ulubiony'),
    path('aktualizuj-opis/<int:pk>/', aktualizuj_opis, name='aktualizuj-opis'),
    path('profil/', profil, name='profil'),
    path('',landing,name='landing')

]