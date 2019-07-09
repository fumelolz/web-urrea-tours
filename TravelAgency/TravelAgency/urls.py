from django.contrib import admin
from django.conf import settings 
from django.urls import path, include

urlpatterns = [
    #Url Para el sitio de administrador
    path('admin/', admin.site.urls),
    #Url Donde estan el home, about
    path('', include('core.urls')),
    #Url del blog
    path('',include('blog.urls')),
    #Url de contact
    path('',include('contact.urls')),
    #Url de viajes
    path('',include('viajes.urls')),
]

if settings.DEBUG:
	from django.conf.urls.static import static 
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

