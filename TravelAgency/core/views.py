from django.shortcuts import render
from .models import Banners,BannerPrincipalInicio,Testimonios,BannerPrincipalBlog
from viajes.models import Paquete,Pais
from blog.models import Post,Category
from noticias.models import NoticiaHome

#Modifica la noticia de la pagina de inicio
n = NoticiaHome.objects.get(pk=1)

#Muestra 3 paquetes ordenados por la fecha de creación(el más reciente)
d = Paquete.objects.order_by('-created').all()[:6]

#Muestra los testimonios
t = Testimonios.objects.all()

#Muestra solo 8 blogs en la pagina de inicio
posts = Post.objects.order_by('-created').all()[:8]

#Muestra solo 3 categorias
cat = Category.objects.all()[:3] 

paises = Pais.objects.all()
bannerHome = Banners.objects.get(id=1)
bnBlog =  BannerPrincipalBlog.objects.get(id=1)
todosdestinos = Paquete.objects.all()



def home(request):
	textoBanner = BannerPrincipalInicio.objects.get(id=1)
	return render(request,'core/home.html' ,{
		'banners':bannerHome,
		'bannerPrincipal':textoBanner,
		'testimonios':t,
		'posts':posts,
		'destinos':d,
		'paises':paises,
		'todosdestinos':todosdestinos, 
		'noticia':n
		})

def about(request):
	return render(request,'core/about.html',{'banners':bannerHome})





