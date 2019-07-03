from django.shortcuts import render,get_object_or_404, get_list_or_404
from core.models import Banners,BannerPrincipalBlog
from .models import Post, Category
from django.core.paginator import Paginator

bn = Banners.objects.get(id=1)
bnBlog =  BannerPrincipalBlog.objects.get(id=1)
posts = Post.objects.order_by('-views').all()[:4]
cat = Category.objects.all()[:3]

 
def category(request,category_id):
	category = get_object_or_404(Category,id=category_id)

	posts = category.get_posts.all()

	paginator = Paginator(posts,4)

	page = request.GET.get('page')

	posts = paginator.get_page(page)

	return render(request,"blog/category.html",{
		'category':posts,
		'bns':bnBlog,
		'banners':bn
		})

def blog_single(request,post_id,post_slug):
	ps = get_object_or_404(Post,id=post_id)
	ps.views +=1
	ps.save()
	print(ps.title)
	return render(request,"blog/blog-single.html",{
		'post':ps,
		'postAlls':posts,
		'bns':bnBlog,
		'categorys':cat,
		'banners':bn
		})


def blog_home(request):
	blogs = Post.objects.all()

	paginator = Paginator(blogs,4)

	page = request.GET.get('page')

	blogs = paginator.get_page(page)

	return render(request,'blog/blog-home.html',{
		'banners':bn,
		'bns':bnBlog,
		'cats':cat,
		'posts':blogs
		})