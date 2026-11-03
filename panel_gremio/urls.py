from django.urls import path
from . import views

urlpatterns = [
    path("", views.ActividadListView, name='listar_gremio'),
    path("crear/", views.ActividadCreateView, name='crear_gremio'),
    path("actualizar/<int:id>/", views.ActividadUpdateView, name='actualizar_gremio'),
]
