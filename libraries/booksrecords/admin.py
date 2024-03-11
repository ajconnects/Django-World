from django.contrib import admin
from .models import BooksDetails

# Register your models here.

class BooksDetailsAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "rating",)
    list_display = ("title", "fullname",)

admin.site.register(BooksDetails, BooksDetailsAdmin)