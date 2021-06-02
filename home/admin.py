from django.contrib import admin
from .models import gallery, gallery_type, article, news, teacher

admin.site.register(gallery)
admin.site.register(gallery_type)

admin.site.register(article)
admin.site.register(news)
admin.site.register(teacher)
