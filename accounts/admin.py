from django.contrib import admin
from .models import Authors

# Register your models here.

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["pk", 'username', 'display_full_name', 'email', 'is_active',]
    list_select_related = ['username',]

    def display_full_name(self, obj):
        fullName = f"{obj.first_name} {obj.last_name}"
        return fullName
    
