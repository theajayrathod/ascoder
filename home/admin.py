from django.contrib import admin
from .models import Contact, AddQuestion, Addanswer, CreatePost

# Register your models here.
admin.site.register(Contact)
admin.site.register(AddQuestion)
admin.site.register(CreatePost)

@admin.register(Addanswer)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tiny.js',)

