from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('admin/', admin.site.urls),
    path('gremio/', include('panel_gremio.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)