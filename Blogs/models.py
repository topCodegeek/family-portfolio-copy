from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 20)
    content = models.TextField()
    date = models.DateField(default = timezone.now())
    def __str__(self):
        return self.title