from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from core.models import Banners 
from .models import Paquete
from noticias.models import NoticiaDestinos
from django.core.paginator import Paginator 

n = NoticiaDestinos.objects.get(pk=1)

ofertas =  Paquete.objects.filter(oferta=1).all()[:6]

bn = Banners.objects.get(id=1)

def packageAll(request):
	destinosw = Paquete.objects.order_by('-created').all()
	paginator = Paginator(destinosw,6)

	page = request.GET.get('page')

	dest = paginator.get_page(page)

	return render(request,"viajes/packages.html",
		{
		'banners':bn,
		'destinos':dest,
		'noticia': n,
		'ofertas':ofertas
		})

def packageInter(request):
	dest = Paquete.objects.filter(categories__id=2).order_by('-created').all()

	paginator = Paginator(dest,6)

	page = request.GET.get('page')

	dest = paginator.get_page(page)
	return render(request,"viajes/inter.html",
		{
		'banners':bn,
		'destinos':dest,
		'noticia': n
		})
def packageNacio(request):
	dest = Paquete.objects.filter(categories__id=1).order_by('-created').all()

	paginator = Paginator(dest,6)

	page = request.GET.get('page')

	dest = paginator.get_page(page)
	return render(request,"viajes/nacio.html", 
		{
		'banners':bn,
		'destinos':dest, 
		'noticia': n
		})


def destinoSingle(request,destino_id):
	ds = get_object_or_404(Paquete,id=destino_id)
	return render(request,"viajes/package-single.html",
		{
		'banners':bn,
		'destino':ds,
		})

def searchDestino(request):

	if request.method == 'GET':

		nombre_pais = request.GET.get('pais')
		nombre_destinos = request.GET.get('destino')
		query = nombre_pais+nombre_destinos
		
		if query:
			status = Paquete.objects.filter(Q(pais__name=nombre_pais) | Q(destino=nombre_destinos)).all()
		else:
			status = Paquete.objects.all()


		
		return render(request,"viajes/search.html",{
			'banners':bn,
			'destinos':status  
			})
