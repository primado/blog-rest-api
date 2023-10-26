from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["pk", 'username', 'display_full_name', 'email', 'is_active',]
    list_display_links = ['username',]

    def display_full_name(self, obj):
        fullName = f"{obj.first_name} {obj.last_name}"
        return fullName
    
