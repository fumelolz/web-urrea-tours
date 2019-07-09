from django.db import models

class NoticiaHome(models.Model):
	title = models.CharField(max_length=140,verbose_name="Titulo")
	content = models.TextField(verbose_name="Contenido")
	image = models.ImageField(verbose_name="Imagen",upload_to="noticias",null=True,blank=True)
	btn = models.CharField(max_length=140,verbose_name="Texto del boton")
	url = models.URLField(verbose_name="Enlace",max_length=500,null=True,blank=True)
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "Noticia Home"
		verbose_name_plural = "Noticia Pagina Home"
		ordering = ['-created']

	def __str__(self):
		return self.title

class NoticiaDestinos(models.Model):
	title = models.CharField(max_length=140,verbose_name="Titulo")
	content = models.TextField(verbose_name="Contenido")
	image = models.ImageField(verbose_name="Imagen",upload_to="noticias",null=True,blank=True)
	btn = models.CharField(max_length=140,verbose_name="Texto del boton")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")
		
	class Meta:
		verbose_name = "Noticia Destinos"
		verbose_name_plural = "Noticia Pagina Destinos"
		ordering = ['-created']

	def __str__(self):
		return self.title
