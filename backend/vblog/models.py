
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.core.files import File
from io import BytesIO
from ckeditor.fields import RichTextField
from django.shortcuts import get_object_or_404


# def user_directory_path(instance, filename):
  # el 0 es la instancia, el 1 el filename
  # return 'blog/{0}/{1}'.format(instance.title, filename)

# ! Category
class Category(models.Model):
  name =   models.CharField(max_length=255, unique=True)
  slug =   models.CharField(max_length=255, unique=True)
  views =  models.IntegerField(default=0, blank=True)

  # padre
  parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name
  
  def get_view_acount(self):
    # views filtra lo que este en su padre
    views = ViewCount.objects.filter(category=self).count
    return views



# ! Post
class Post(models.Model):

# esto manda todo al administrador
  class PostObjects(models.Manager):
    def get_queryset(self):
      return super().get_queryset()

  title =       models.CharField(max_length=255)
  url_imagen =  models.CharField(max_length=900, null=True, default='bafybeiff234nianjb5dxthct7x6frafnisl4ne3zisgfmcmu4cl7mfv42y')
  # thumbnail =   models.ImageField(upload_to='uploads/', blank=True, null=True)
  excerpt =     models.TextField(null=True)
  description = RichTextField(blank=True)
  slug =        models.SlugField(max_length=255, null=False, unique=True)
  published =   models.DateTimeField(default=timezone.now)
  carousel =    models.BooleanField(default=True)
  objects =     models.Manager()
  postobjects = PostObjects()
  category =    models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  views = models.IntegerField(default=0)

#  se ordena
  class Meta:
    ordering = ('-published', )

# para que aparezca el titulo en admin
  def __str__(self):
    return self.title

# para obtener la imagen
  # def get_thumnail(self):
  #   if self.thumbnail:
  #     return 'https://poison.onrender.com' + self.thumbnail.url

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

# ! contador de visitas
class ViewCount(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  ip_user = models.CharField(max_length=20, null=True)
  count = models.IntegerField(default=0)

  def __str__(self):
    return {self.ip_user}











