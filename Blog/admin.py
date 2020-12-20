from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Person)
admin.site.register(BlogModel)
admin.site.register(Category)
admin.site.register(LikeBlog)
admin.site.register(UserDetail)