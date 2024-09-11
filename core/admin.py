# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Request, Notification

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('created_at',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('email', 'created_at')}),
    )

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'stock', 'added_at']
    list_filter = ['author', 'published_date']
    search_fields = ['title', 'author']

class RequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'book_title', 'book_author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'book_title', 'book_author']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'notification_status', 'created_at']
    list_filter = ['notification_status', 'created_at']
    search_fields = ['user__username', 'book__title']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Notification, NotificationAdmin)
