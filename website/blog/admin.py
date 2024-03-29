from django.contrib import admin
from .models import Post, Author, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author",)
    list_filter = ("author", "title", "date",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)