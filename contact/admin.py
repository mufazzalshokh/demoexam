from django.contrib import admin

from contact.forms import ContactModelForm
from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    form = ContactModelForm
