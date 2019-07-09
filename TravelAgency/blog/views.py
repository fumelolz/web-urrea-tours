from django.shortcuts import render,get_object_or_404, get_list_or_404
from core.models import Banners,BannerPrincipalBlog 
from .models import Post, Category
from django.core.paginator import Paginator

#Llamado del objecto banner, cambia el banner de la pagina de inicio/home
bannerHome = Banners.objects.get(id=1)

#Llamado del objecto banner, cambia el banner de la pagina de blog
bannerBlog =  BannerPrincipalBlog.objects.get(id=1)

#Llamado de los post o blogs, para la pagina home
posts = Post.objects.order_by('-views').all()[:4]

#Llamado de las categorias, muestra 15 categorias, para la barra lateral
categorias = Category.objects.all()[:15]

def category(request,category_id):
	category = get_object_or_404(Category,id=category_id)

	posts = category.get_posts.all()

	paginator = Paginator(posts,4)

	page = request.GET.get('page')

	posts = paginator.get_page(page)

	return render(request,"blog/category.html",{
		'category':posts,
		'bns':bannerBlog,
		'categorys':categorias,
		'banners':bannerHome
		})

def blog_single(request,post_id,post_slug):
	ps = get_object_or_404(Post,id=post_id)
	ps.views +=1
	ps.save()
	print(ps.title)
	return render(request,"blog/blog-single.html",{
		#Muestra solo un blog
		'post':ps,
		#Muestra todos los blogs
		'postAlls':posts,
		'bns':bannerBlog,
		'categorys':categorias,
		'banners':bannerHome
		})


def blog_home(request):
	blogs = Post.objects.all()

	paginator = Paginator(blogs,4)

	page = request.GET.get('page')

	blogs = paginator.get_page(page)

	return render(request,'blog/blog-home.html',{
		'banners':bannerHome,
		'bns':bannerBlog,
		'cats':categorias,
		'posts':blogs
		})