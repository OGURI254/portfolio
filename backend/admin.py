from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Category, Tag

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('categories', 'tags')
    prepopulated_fields = {'title': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

