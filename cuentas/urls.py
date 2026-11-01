from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),

    path('panel/moderador/', views.panel_moderador, name='panel_moderador'),
    path('panel/gremio/', views.panel_gremio, name='panel_gremio'),
    path('panel/turista/', views.panel_turista, name='panel_turista'),
]