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
        fields = ('id', 'title', 'thumbnail', 'excerpt', 'description', 'slug', 'published', 'category', 'get_thumnail')
