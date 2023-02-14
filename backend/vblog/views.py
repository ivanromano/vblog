from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, Category, ViewCount
from .serializers import PostSerializer, CategorySerializer
from .pagination import SmallSetPagination

# Create your views here.

#  devuelve todas las categorías que existen en el modelo Category con sus subcategorías, si existen.
class CategoryListView(APIView): 
  permission_classes = (permissions.AllowAny, )
  def get(self, request, format=None):

    if Category.objects.all().exists():
      # agarra todas las categorias que existen
      categories = Category.objects.all()
      result = []

      for category in categories:
        if not category.parent: # si no tiene una subcategoria se crea un dicci/json llamado item
          item = {}
          item['id'] = category.id
          item['name'] = category.name
          item['slug'] = category.slug
          item['views'] = category.views
          item['sub_categories'] = []
          for sub_category in categories: # en cada vuelta quiero crear un sub_item y en el item se expande con sub_Category
            sub_item = {}
            if sub_category.parent and sub_category.parent.id == category.id:
              sub_item['id'] = sub_category.id
              sub_item['name'] = sub_category.name
              sub_item['slug'] = sub_category.slug
              sub_item['views'] = sub_category.views
              item['sub_categories'].append(sub_item) #item obtiene todo

          result.append(item) 
      return Response({'categories': result}, status=status.HTTP_200_OK)
    else: 
      return Response({'error': 'no se encontro'}, status=status.HTTP_404_NOT_FOUND)



# devuelve una lista paginada de publicaciones (Post) usando el serializador PostSerializer.
class BlogListView(APIView):
  # permission_classes = (permissions.AllowAny)
  def get(self, request, *args, **kwargs):
    paginator = SmallSetPagination()
    posts = Post.postobjects.all()
    result = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result, many=True)
    return paginator.get_paginated_response(serializer.data)
  # Response(serializer.data)

# devuelve todas las publicaciones de un objeto Category en particular, incluidas las subcategorías y todas las publicaciones de cada subcategoría.
class FullBlogAndCategory(APIView):
  def get(self, request, *args, **kwargs):
    if Post.postobjects.all().exists():
      slug = request.query_params.get('slug') # se agarra el slug del objeto
      category = Category.objects.get(slug=slug)
      posts = Post.postobjects.order_by('-published').all()

      #comprobar si no tiene categorias hijas
      if not Category.objects.filter(parent=category).exists():
        posts = posts.filter(category=category)
      else: 
        sub_categories = Category.objects.filter(parent=category) # si existen hijos. 
        filtro_categories = [category]
          
        for cat in sub_categories:
          filtro_categories.append(cat)
          
        filtro_categories = tuple(filtro_categories)
        posts = posts.filter(category__in=filtro_categories)

      paginator = SmallSetPagination()
      results = paginator.paginate_queryset(posts, request)
      serializer = PostSerializer(results, many=True)
      print(serializer.data)
      return paginator.get_paginated_response(serializer.data)
    else:
      return Response({"error :(": "404"}, status=status.HTTP_404_NOT_FOUND)
    # http://localhost:8000/blog/full/?slug=pensante

# devuelve detalles de una publicación Post específica y aumenta la vista de la publicación.
class PostDetailView(APIView):
  def get(self, request, slug, format=None):
    if Post.postobjects.filter(slug=slug).exists():
      post = Post.postobjects.get(slug=slug)
      serializer = PostSerializer(post)

      adress = request.META.get('HTTP_X_FORWARDED_FOR')
      if adress:
        ip = adress.split(',')[-1].strip()
      else:
        ip = adress.get('REMOTE_ADDR')

      if not ViewCount.objects.filter(post=post, ip_user=ip):
        view = ViewCount(post=post, ip_user=ip)
        view.save
        post.views += 1
        post.save
 
      return Response({"post": "details"}, status=status.HTTP_200_OK)
    else:
      return Response({"error ": "details"}, status=status.HTTP_404_NOT_FOUND)



