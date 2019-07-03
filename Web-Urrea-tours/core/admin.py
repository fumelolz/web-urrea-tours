from django.contrib import admin
from .models import Banners,BannerPrincipalInicio,Testimonios,BannerPrincipalBlog

class BannersAdmin(admin.ModelAdmin):
	readonly_fields = ('name','created','updated')

class BannerPrincipalInicioAdmin(admin.ModelAdmin):

	readonly_fields = ('created','updated')
class BannerPrincipalBlogAdmin(admin.ModelAdmin):
	readonly_fields = ('created','updated')

class TestimoniosAdmin(admin.ModelAdmin):
	readonly_fields = ('created','updated')

admin.site.register(Banners,BannersAdmin)	

admin.site.register(BannerPrincipalInicio,BannerPrincipalInicioAdmin)

admin.site.register(Testimonios,TestimoniosAdmin)
admin.site.register(BannerPrincipalBlog,BannerPrincipalBlogAdmin)