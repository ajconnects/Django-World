from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  #StackedInline show it in line the admin while the Tabularinline show in table
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"] #you can display function on the admin panel
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.site_header = "Aj Connect"  #change the admin name

#admin.site.register(Choice)