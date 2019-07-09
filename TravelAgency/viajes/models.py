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

class Pais(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre del pais")
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de edición")   
	class Meta:
		verbose_name = "Pais"
		verbose_name_plural = "Paises"
		ordering = ['-created']

	def __str__(self):
		return self.name


class Paquete(models.Model):
	destino = models.CharField(verbose_name="Nombre Del Destino",max_length=100)
	descripcion = models.TextField()
	categories = models.ManyToManyField(Categoria,verbose_name="Categorías",related_name="get_tipo")
	pais = models.ManyToManyField(Pais,verbose_name="Pais",related_name="get_pais")
	image = models.ImageField(verbose_name="Imagen",upload_to="paquetes",null=True,blank=True)
	oferta = models.PositiveSmallIntegerField(null=True,blank=True)
	porcentajeoferta = models.PositiveSmallIntegerField(verbose_name="1 a 100",null=True,blank=True)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		ordering = ['-created']


	def __str__(self):
		return self.destino

class Galeria(models.Model):
	image = models.ImageField(verbose_name="Imagen",upload_to="galeria",null=True,blank=True)
	paquete = models.ForeignKey(Paquete,related_name="img",verbose_name="Imagenes que incluye",on_delete=models.CASCADE)
	


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

class Temporada(models.Model):
	tipo = models.CharField(verbose_name="Tipo",max_length=100)

	def __str__(self):
		return self.tipo

class Plan(models.Model):
	tipo = models.ForeignKey(Temporada,related_name="type",on_delete=models.CASCADE)
	paquete = models.ForeignKey(Paquete,related_name="plan_paquete",on_delete=models.CASCADE)
	nombre = models.CharField(verbose_name="Nombre del plan",max_length=100)
	def __str__(self):
		return self.nombre

class Planes(models.Model):
	plan = models.ForeignKey(Plan,related_name="get_plans",on_delete=models.CASCADE)
	hotel = models.CharField(verbose_name="Hotel",max_length=100)
	categoriaHotel = models.PositiveSmallIntegerField(verbose_name="1 a 5",null=True,blank=True)
	sencilla = models.PositiveIntegerField(verbose_name="Precio sencilla",null=True,blank=True)
	extrasencilla = models.PositiveIntegerField(verbose_name="Precio Noche extra sencilla",null=True,blank=True)
	doble = models.PositiveIntegerField(verbose_name="Precio doble",null=True,blank=True)
	extradoble = models.PositiveIntegerField(verbose_name="Precio Noche extra doble",null=True,blank=True)
	triple = models.PositiveIntegerField(verbose_name="Precio triple",null=True,blank=True)
	extratriple = models.PositiveIntegerField(verbose_name="Precio Noche extra triple",null=True,blank=True)
	niños = models.PositiveIntegerField(verbose_name="Precio niños",null=True,blank=True)
	extraniños = models.PositiveIntegerField(verbose_name="Precio noche extra niños",null=True,blank=True)
	



