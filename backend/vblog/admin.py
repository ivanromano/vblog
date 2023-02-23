from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')

@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'carousel')