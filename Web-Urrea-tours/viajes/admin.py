from django.contrib import admin
from .models import Paquete,Incluye,NoIncluye,Categoria


class IncluyeAdmin(admin.StackedInline):
	model = Incluye

class NoIncluyecAdmin(admin.StackedInline):
	model = NoIncluye 

class PaqueteAdmin(admin.ModelAdmin):
	model = Paquete 
	list_display = ('destino','precio','descripcion','created')
	search_fields = ('destino',)
	inlines = [

		IncluyeAdmin,
		NoIncluyecAdmin,

	]

admin.site.register(Paquete,PaqueteAdmin)
admin.site.register(Categoria)