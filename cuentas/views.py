
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario


def registro_usuario(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        rol = request.POST.get('rol')

        if rol not in ['turista', 'gremio']:
            messages.error(request, 'Selecciona un tipo de cuenta válido.')
            return redirect('registro')

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese nombre de usuario ya existe.')
            return redirect('registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ese correo ya está registrado.')
            return redirect('registro')

        try:
            validate_password(password)
        except ValidationError as error:
            for mensaje in error.messages:
                messages.error(request, mensaje)
            return redirect('registro')

        usuario = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        PerfilUsuario.objects.create(
            usuario=usuario,
            rol=rol
        )

        login(request, usuario)
        return redirect('/')

    return render(request, 'cuentas/registro.html')


def login_usuario(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            # Administrador principal
            if usuario.is_superuser:
                return redirect('/admin/')

            # Comprobar el rol del usuario
            try:
                rol = usuario.perfil.rol
            except PerfilUsuario.DoesNotExist:
                rol = 'turista'

            if rol == 'moderador':
                return redirect('panel_moderador')

            elif rol == 'gremio':
                return redirect('panel_gremio')

            else:
                return redirect('panel_turista')

        messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'cuentas/login.html')

def cerrar_sesion(request):

    logout(request)
    return redirect('/')



@login_required
def panel_moderador(request):

    if not hasattr(request.user, 'perfil'):
        return redirect('/')

    if request.user.perfil.rol != 'moderador':
        return redirect('/')

    return render(request, 'cuentas/panel_moderador.html')


@login_required
def panel_gremio(request):

    if not hasattr(request.user, 'perfil'):
        return redirect('/')

    if request.user.perfil.rol != 'gremio':
        return redirect('/')

    return render(request, 'cuentas/panel_gremio.html')


@login_required
def panel_turista(request):

    if not hasattr(request.user, 'perfil'):
        return redirect('/')

    if request.user.perfil.rol != 'turista':
        return redirect('/')

    return render(request, 'cuentas/panel_turista.html')