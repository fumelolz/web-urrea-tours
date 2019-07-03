from django.shortcuts import render,get_object_or_404
from core.models import Banners
from .models import Paquete
from noticias.models import NoticiaDestinos
from django.core.paginator import Paginator

n = NoticiaDestinos.objects.get(pk=1)

d = Paquete.objects.all()[:6]

bn = Banners.objects.get(id=1)

def packageAll(request):
	destinosw = Paquete.objects.all()
	paginator = Paginator(destinosw,6)

	page = request.GET.get('page')

	dest = paginator.get_page(page)

	return render(request,"viajes/packages.html",
		{
		'banners':bn,
		'destinos':dest,
		'noticia': n
		})

def packageInter(request):
	dest = Paquete.objects.filter(categories__id=2).all()

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
	dest = Paquete.objects.filter(categories__id=1).all()

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
		'destino':ds
		})

def searchDestino(request):

	if request.method == 'GET':
		nombre_destino = request.GET.get('busqueda')
		status = Paquete.objects.filter(destino__icontains=nombre_destino).all()
		return render(request,"viajes/search.html",{
			'banners':bn,
			'destinos':status
			})
