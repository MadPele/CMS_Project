from django.contrib import admin
from .models import User, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
