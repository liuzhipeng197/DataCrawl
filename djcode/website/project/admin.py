from django.contrib import admin
from project.models import KeyWord
from project.models import ContentUrl
from project.models import Info
from project.models import Comment

admin.site.register(Info)
admin.site.register(KeyWord)
admin.site.register(ContentUrl)
admin.site.register(Comment)
