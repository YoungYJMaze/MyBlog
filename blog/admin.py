from django.contrib import admin
from .models import Post,Category,Tag,Essay
from comments.models import Comment,Essay_Comment
from . import models
from mdeditor.widgets import MDEditorWidget

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Essay)
admin.site.register(Comment)

admin.site.register(Essay_Comment)





