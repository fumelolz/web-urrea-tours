from django.db import models

class Banners(models.Model):
	name = models.CharField(max_length=30,verbose_name="Banners",default='Banners')
	bannerInicio = models.ImageField(verbose_name="Banner Inicio",upload_to="banners",null=True,blank=True)
	bannerBlog = models.ImageField(verbose_name="Banner Blog",upload_to="banners",null=True,blank=True)
	bannerAbout = models.ImageField(verbose_name="Banner Otros",upload_to="banners",null=True,blank=True)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "banner"
		verbose_name_plural = "Cambiar Banner"
		ordering = ['-created']

	def __str__(self):
		return self.name

class BannerPrincipalInicio(models.Model):
	title = models.CharField(max_length=100,verbose_name="Titulo")
	subtitle = models.CharField(max_length=100,verbose_name="SubTitulo") 
	content = models.TextField(verbose_name="Contenido")
	NameBtn = models.CharField(max_length=30,verbose_name="Nombre del boton",default="Haz click aquí")
	url = models.URLField(verbose_name="Enlace",max_length=500,null=True,blank=True)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "banner"
		verbose_name_plural = "Cambiar Texto Banner Principal"
		ordering = ['-created']

	def __str__(self):
		return self.title

class BannerPrincipalBlog(models.Model):
	title = models.CharField(max_length=100,verbose_name="Titulo") 
	content = models.TextField(verbose_name="Contenido")
	NameBtn = models.CharField(max_length=30,verbose_name="Nombre del boton",default="Haz click aquí")
	url = models.URLField(verbose_name="Enlace",max_length=500,null=True,blank=True)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "banner"
		verbose_name_plural = "Cambiar Texto Banner Blog"
		ordering = ['-created']

	def __str__(self):
		return self.title

class Testimonios(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre del cliente")
	content = models.TextField(verbose_name="Comentario")
	starts =  models.IntegerField(verbose_name="Estrellas")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "testimonio"
		verbose_name_plural = "Crear Testimonio"
		ordering = ['-created']

	def __str__(self):
		return self.name

	
