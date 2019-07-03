from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre")
	subtitle = models.CharField(max_length=100,verbose_name="Subtitulo Motivador")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")
	image = models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"
		ordering = ['-created']

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200,verbose_name="Titulo")
	content = RichTextField(verbose_name="Contenido")
	published = models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
	image = models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)
	views = models.PositiveIntegerField(default=0)
	author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
	categories = models.ManyToManyField(Category,verbose_name="Categorías",related_name="get_posts")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "entrada"
		verbose_name_plural = "entradas"
		ordering = ['-created']

	def __str__(self):
		return self.title

