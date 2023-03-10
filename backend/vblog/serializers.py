# español. subi esta app en render. todas las rutas funcionan de forma perfecta, exepto una que me tira error 500. este es mi models.py
from rest_framework import serializers
from .models import Post, Category, ViewCount

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'views') 

class ViewCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewCount
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Post
        fields = ('id', 'title', 'url_imagen', 'excerpt', 'description', 'slug', 'published', 'carousel', 'category')
