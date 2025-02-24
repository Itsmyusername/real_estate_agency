from django.contrib import admin
from django.contrib.admin import register

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner
    raw_id_fields = ['flats']


@register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['like']
    inlines = [OwnerInline]


@register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']


@register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
