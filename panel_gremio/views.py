from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActividadForm
from django.contrib import messages
from .models import Actividad

def ActividadCreateView(request):
    form = ActividadForm(request.POST or None, request.FILES or None) 
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "actividad creada")
            return redirect('listar_gremio')  
    return render(request, 'panel_gremio/actividad_gremio_form.html', {'accion':'Crear', 'form':form})

def ActividadListView(request):
    return render(request, 'panel_gremio/actividad_gremio_list.html', {'actividades':Actividad.objects.all()})

def ActividadUpdateView(request, id):

    actividad = get_object_or_404(Actividad, pk=id)
   
    form = ActividadForm(request.POST or None, request.FILES or None,  instance=actividad) 
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad actualizado")
            return redirect('listar_gremio')  
    return render(request, 'panel_gremio/actividad_gremio_form.html', {'accion':'Actualizar', 'form':form})

