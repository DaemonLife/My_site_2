from django.contrib import admin

from .models import *

# Register your models here.
# * Registration:
a = [
   Bb,
]

for line in a:
    admin.site.register(line)