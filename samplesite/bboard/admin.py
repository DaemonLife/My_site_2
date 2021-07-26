from django.contrib import admin

from .models import *

# Register your models here.
# * Registration:
a = [
   Bb,
]

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

for line in a:
    admin.site.register(line, BbAdmin)