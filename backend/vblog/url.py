from django.urls import path
from .views import BlogListView, CategoryListView, FullBlogAndCategory, PostDetailView
app_name='blog'

urlpatterns = [
    path('posts/', BlogListView.as_view()),
    path('cat/', CategoryListView.as_view()),
    path('full/', FullBlogAndCategory.as_view()),
    path('<slug>', PostDetailView.as_view()),
]