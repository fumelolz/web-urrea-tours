from django.contrib import admin
from .models import Paquete,Incluye,NoIncluye,Categoria,Pais,Galeria,Temporada,Plan,Planes

class PlanesInline(admin.StackedInline):
	model = Planes

class PlanInline(admin.StackedInline):
	model = Plan
	extra = 2
	inlines = [PlanesInline]

class IncluyeAdmin(admin.StackedInline):
	model = Incluye

class NoIncluyecAdmin(admin.StackedInline):
	model = NoIncluye
	extra = 2 

class GaleriaAdmin(admin.StackedInline):
	model = Galeria

class PaqueteAdmin(admin.ModelAdmin):
	model = Paquete 
	list_display = ('destino','get_paises','descripcion','created')
	search_fields = ('destino',)
	inlines = [

		IncluyeAdmin,
		NoIncluyecAdmin,
		GaleriaAdmin,
		PlanInline,

	]

	def get_paises(self,obj):
		return ",".join([c.name for c in obj.pais.all()])
	get_paises.short_description = "Pais"

class PlanAdmin(admin.ModelAdmin):
	model = Plan
	list_display = ('paquete','nombre','tipo',)
	inlines = [PlanesInline]

admin.site.register(Paquete,PaqueteAdmin)
admin.site.register(Categoria)
admin.site.register(Pais)
admin.site.register(Temporada)
admin.site.register(Plan,PlanAdmin)