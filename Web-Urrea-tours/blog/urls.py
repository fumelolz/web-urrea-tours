from django.urls import path
from . import views 

urlpatterns = [
    path('blog-home/', views.blog_home,name="core-blog-home"),
    path('category/<int:category_id>/',views.category,name="category"),
    path('post/<int:post_id>/<slug:post_slug>/',views.blog_single,name="blog-single")
]
