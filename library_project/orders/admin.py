from django.contrib import admin

from .models import Order, Feedback


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'book', 'user_name', 'user_email', 'user_address', 'date'
    )
    search_fields = ('user_email', 'user_address')
    list_filter = ('date', 'book')
    list_display_links = ('id', 'book')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_email', 'comment', 'date')
    search_fields = ('user_email', 'comment')
    list_filter = ('date',)
    list_display_links = ('id', 'user_email')
