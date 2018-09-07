from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    blog_type = models.ForeignKey(BlogType, on_delete=None)
    author = models.ForeignKey(User, on_delete=None)
    create_time = models.TimeField(auto_now_add=True)
    last_update_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "<Blog: %s>" % self.title
