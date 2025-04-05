from django.shortcuts import render, get_object_or_404
from Portfolios import models
from Blogs import models as Blogmodels
# Create your views here.
def blogs(request):
    blog_count = Blogmodels.Blog.objects.count()
    members = models.Member.objects.all()
    first_five = Blogmodels.Blog.objects.order_by('-date')[:5]
    all_blogs = Blogmodels.Blog.objects.order_by('-date')
    return render (request, "blogs.html", {"members":members, "first_five":first_five, "all_blogs":all_blogs, "blog_count":blog_count})


def detail(request, blog_id):
    '''
    blog = Blogmodels.Blog.objects.all()
    for x in blog:
        if x.id == Blog_id:
            blog = x
            break
    '''
    blog = get_object_or_404(Blogmodels.Blog, pk = blog_id)
    return render (request, "detail.html", {"blog":blog})