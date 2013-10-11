from django.contrib import admin
from entity.project.models import KeyWord
from entity.project.models import ContentUrl
from entity.project.models import Info
from entity.project.models import Comment

admin.site.register(Info)
admin.site.register(KeyWord)
admin.site.register(ContentUrl)
admin.site.register(Comment)
