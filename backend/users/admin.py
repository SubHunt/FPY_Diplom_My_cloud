from django.contrib import admin
from .models import User, Files

admin.site.site_header = "Админ-панель My cloud"
admin.site.site_title = "Админ-панель"
admin.site.index_title = "Добро пожаловать в Админ-панель My Cloud"


class FilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')


class FilesInline(admin.TabularInline):
    model = Files
    exclude = ['published', 'description']
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'name', 'is_admin')
    fieldsets = [
        (None, {'fields': ['login']}),
        ('More info', {
            'fields': ['name', 'email', 'is_admin'],
            'classes': ['collapse']
        })
    ]
    inlines = [FilesInline]


admin.site.register(User, UserAdmin)
admin.site.register(Files, FilesAdmin)
