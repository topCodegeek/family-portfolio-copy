from django.shortcuts import render, get_object_or_404
from .models import Member
from Blogs import models as Blogmodels

# Create your views here.
def homepage(request):
    members = Member.objects.all()
    blog_count = Blogmodels.Blog.objects.count()
    first_five = Blogmodels.Blog.objects.order_by('-date')[:5]
    return render (request, "homepage.html", {"members":members, "first_five":first_five, "blog_count":blog_count})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    blogs = Blogmodels.Blog.objects.order_by('-date').filter(author=member.name)
    blog_count = blogs.count()
    return render (request, 'member-detail.html', {"member":member, "blogs":blogs, "blog_count":blog_count})