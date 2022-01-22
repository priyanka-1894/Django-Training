from django.contrib import admin

from .models import Author, Tag, Post

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):    
    list_display = ("first_name", "last_name")

class PostAdmin(admin.ModelAdmin):    
    list_display = ("title", "date", "author",)
    list_filter = ("author", "date", "tags",)
    prepopulated_fields = {
        "slug": ("title",)
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)