from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Notifications)
