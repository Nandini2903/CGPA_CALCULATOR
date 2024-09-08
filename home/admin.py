from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'credit', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('grade', 'credit')

admin.site.register(Subject, SubjectAdmin)
