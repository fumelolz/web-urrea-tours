from django.urls import path
from . import views 

urlpatterns = [
	#Url bloh home
    path('blog/', views.blog_home,name="core-blog-home"),
    path('categoria/<int:category_id>/',views.category,name="category"),
    path('blog/<int:post_id>/<slug:post_slug>/',views.blog_single,name="blog-single")
]
