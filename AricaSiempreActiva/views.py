from datetime import date, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect 
from .models import Evento
from .forms import SuscriptorForm

# Create your views here.
def home(request):
    hoy = date.today()
    limite = hoy + timedelta(days=60)
    eventos = Evento.objects.filter(fecha__gte=hoy, fecha__lte=limite).order_by('fecha')[:3]
    form = SuscriptorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por suscribirte!')
            return redirect('home')
        else:
            messages.error(request, 'Ese correo no es válido o ya está suscrito.')
    return render(request, 'AricaSiempreActiva/home.html', {'eventos': eventos, 'form': form})