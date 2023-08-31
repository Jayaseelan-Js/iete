from django.contrib import admin
from .models import News, Publication, Events, Education

# Register your models here.

admin.site.register(News)
admin.site.register(Publication)
admin.site.register(Events)
admin.site.register(Education)