from django.db import models
from django.utils import timezone

class Categoria(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre")
	subtitle = models.CharField(max_length=100,verbose_name="Subtitulo Motivador")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")
	image = models.ImageField(verbose_name="Imagen",upload_to="paquetes",null=True,blank=True)

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"
		ordering = ['-created']

	def __str__(self):
		return self.name


class Paquete(models.Model):
	destino = models.CharField(verbose_name="Nombre Del Destino",max_length=100)
	descripcion = models.TextField()
	categories = models.ManyToManyField(Categoria,verbose_name="Categorías",related_name="get_tipo")
	image = models.ImageField(verbose_name="Imagen",upload_to="paquetes",null=True,blank=True)
	precio = models.DecimalField(verbose_name="Precio del destino",max_digits=19, decimal_places=4,default=0.0)
	published = models.DateField(verbose_name="Fecha del viaje",default=timezone.now)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		ordering = ['-created']


	def __str__(self):
		return self.destino

class Incluye(models.Model):
	incluye = models.CharField(verbose_name="Incluye",max_length=100)
	paquete = models.ForeignKey(Paquete,related_name="inc",verbose_name="Cosas que incluye",default="Vacio",on_delete=models.CASCADE)

	def __str__(self):
		return self.incluye

class NoIncluye(models.Model):
	noIncluye = models.CharField(verbose_name="No Incluye",max_length=100)
	paquete = models.ForeignKey(Paquete,related_name="noinc",verbose_name="Cosas que incluye",default="Vacio",on_delete=models.CASCADE)

	def __str__(self):
		return self.noIncluye