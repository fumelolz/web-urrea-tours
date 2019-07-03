from django.shortcuts import render
from .models import Banners,BannerPrincipalInicio,Testimonios,BannerPrincipalBlog
from viajes.models import Paquete 
from blog.models import Post,Category
from noticias.models import NoticiaHome

n = NoticiaHome.objects.get(pk=1)

d = Paquete.objects.order_by('-created').all()[:3]
t = Testimonios.objects.all()
posts = Post.objects.order_by('-created').all()[:8]
cat = Category.objects.all()[:3]

bn = Banners.objects.get(id=1)
bnBlog =  BannerPrincipalBlog.objects.get(id=1)



def home(request):
	bn1 = BannerPrincipalInicio.objects.get(id=1)
	return render(request,'core/home.html' ,{
		'banners':bn,
		'bannerPrincipal':bn1,
		'testimonios':t,
		'posts':posts,
		'destinos':d,
		'noticia':n
		})

def about(request):
	return render(request,'core/about.html',{'banners':bn})





