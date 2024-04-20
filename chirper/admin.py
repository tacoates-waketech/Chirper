from django.contrib import admin
from .models import Chirp, Comment

@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ('title', 'chirper', 'body')
    search_fields = ('title', 'chirper__username')
    list_filter = ('chirper',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('chirp', 'chirper', 'body')
    search_fields = ('chirp__title', 'chirper__username')
    list_filter = ('chirp', 'chirper')

