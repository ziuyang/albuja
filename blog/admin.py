from django.contrib import admin

from .models import Blog
admin.site.register(Blog)

from .models import QnA
admin.site.register(QnA)
# Register your models here.
