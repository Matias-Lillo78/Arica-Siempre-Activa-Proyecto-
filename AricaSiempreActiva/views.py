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

def quienes_somos(request):
    equipo = [
        {'iniciales': 'GB', 'nombre': 'Gigliola Bongiorno Farias', 'cargo': 'Ejecutiva de Competitividad', 'institucion': 'Corfo'},
        {'iniciales': 'FR', 'nombre': 'Franco Rojas Carreño', 'cargo': 'Coordinador', 'institucion': 'Programa “Arica Siempre Activa”'},
        {'iniciales': 'JM', 'nombre': 'Javiera Martínez', 'cargo': 'Profesional de Apoyo', 'institucion': 'Programa “Arica Siempre Activa”'},
    ]

    grupos = [
        {
            'titulo': 'Sector Público',
            'aliados': [
                {'nombre': 'Municipalidad de Arica', 'logo': 'muni-arica.png'},
                {'nombre': 'Municipalidad de Camarones', 'logo': 'muni-camarones.png'},
                {'nombre': 'Corporación Municipal Costa Chinchorro', 'logo': 'costa-chinchorro.png'},
                {'nombre': 'Sernatur', 'logo': 'sernatur.png'},
                {'nombre': 'Corporación Municipal Chinchorro', 'logo': 'corp-chinchorro.png'},
                {'nombre': 'Chinchorro Marka', 'logo': 'chinchorro-marka.png'},
            ],
        },
        {
            'titulo': 'Sector Privado',
            'aliados': [
                {'nombre': 'Cámara de Turismo y Comercio Camarones', 'logo': 'camara-camarones.png'},
                {'nombre': 'Cámara de Comercio, Industria, Servicios y Turismo de Arica', 'logo': 'camara-arica.png'},
                {'nombre': 'Orange Travel', 'logo': 'orange-travel.png'},
                {'nombre': 'Lynn Tour', 'logo': 'lynn-tour.png'},
                {'nombre': 'Raíces Andinas', 'logo': 'raices-andinas.png'},
                {'nombre': 'Turismo Chogña', 'logo': 'turismo-chogna.png'},
                {'nombre': 'Norte Outdoor', 'logo': 'norte-outdoor.png'},
                {'nombre': 'TRA Eventos Deportivos', 'logo': 'tra.png'},
                {'nombre': 'Todo Arica Tours', 'logo': 'todo-arica.png'},
                {'nombre': 'Arica Convention Bureau', 'logo': 'arica-convention.png'},
                {'nombre': 'CapTour Qhapaq Ñan', 'logo': 'captour.png'},
                {'nombre': 'Ubiavis Birdwatching', 'logo': 'ubiavis.png'},
                {'nombre': 'Guías de Turismo Arica y Parinacota', 'logo': 'guias.png'},
                {'nombre': 'Escuela de Surf Arica', 'logo': 'escuela-surf.png'},
                {'nombre': 'Sport XV', 'logo': 'sport-xv.png'},
                {'nombre': 'Unión Flopos', 'logo': 'union-flopos.png'},
            ],
        },
        {
            'titulo': 'Comunidad',
            'aliados': [
                {'nombre': 'Arica Activa Fundación', 'logo': 'arica-activa.png'},
                {'nombre': 'Tortu Arica ONG', 'logo': 'tortu-arica.png'},
                {'nombre': 'Observadores de Aves Arica y Parinacota', 'logo': 'observadores-aves.png'},
                {'nombre': 'Salvemos Chinchorro', 'logo': 'salvemos-chinchorro.png'},
                {'nombre': 'ONG AUPM', 'logo': 'ong-aupm.png'},
                {'nombre': 'Comité Ambiental Comunal', 'logo': 'comite-ambiental.png'},
            ],
        },
    ]

    comite = [
        {'nombre': 'Corfo', 'logo': 'corfo.png', 'url': 'https://www.corfo.cl', 'dominio': 'corfo.cl'},
        {'nombre': 'Sernatur', 'logo': 'sernatur.png', 'url': 'https://www.sernatur.cl', 'dominio': 'sernatur.cl'},
        {'nombre': 'Municipalidad de Arica', 'logo': 'muni-arica.png', 'url': 'https://www.muniarica.cl', 'dominio': 'muniarica.cl'},
        {'nombre': 'Municipalidad de Camarones', 'logo': 'muni-camarones.png', 'url': 'https://www.municamarones.cl', 'dominio': 'municamarones.cl'},
        {'nombre': 'Costa Chinchorro', 'logo': 'costa-chinchorro.png', 'url': 'https://www.costachinchorro.cl', 'dominio': 'costachinchorro.cl'},
        {'nombre': 'Orange Travel', 'logo': 'orange-travel.png', 'url': 'https://www.orangetravel.cl', 'dominio': 'orangetravel.cl'},
        {'nombre': 'Guías de Turismo Arica y Parinacota', 'logo': 'guias.png', 'url': 'https://facebook.com/guiasdearicayparinacota', 'dominio': 'Facebook'},
        {'nombre': 'Observadores de Aves', 'logo': 'observadores-aves.png', 'url': 'https://humedaldearica.cl/', 'dominio': 'humedaldearica.cl'},
    ]

    return render(request, 'AricaSiempreActiva/quienes_somos.html', {
        'equipo': equipo,
        'grupos': grupos,
        'comite': comite,
    })