#Blogs
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Blogs"

urlpatterns = [
    path("", views.blogs, name = "blogs"),
    path("<int:blog_id>", views.detail, name = "detail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
