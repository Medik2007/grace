from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import Dress, DressSize, DressModel, DressColor
from users.models import Delivery, Order
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.unregister(Group)


class ColorInLine(admin.StackedInline):
    model = DressColor
    extra = 0
class SizeInLine(admin.StackedInline):
    model = DressSize 
    extra = 0
class ModelInLine(admin.StackedInline):
    model = DressModel
    extra = 0

@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    inlines = [ColorInLine, SizeInLine, ModelInLine]


class OrderInLine(admin.TabularInline):
    model = Order
    extra = 0
    can_delete = False
    def get_readonly_fields(self, request, obj=None): #pyright:ignore
        return [f.name for f in self.model._meta.fields] #pyright:ignore
    def has_add_permission(self, request, obj):
        return False

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    inlines = [OrderInLine]
    def get_readonly_fields(self, request, obj=None): #pyright:ignore
        if obj:
            return [f.name for f in self.model._meta.fields if f.name != 'state']
        return self.readonly_fields
    def has_add_permission(self, request):
        return False




class DeliveryInLine(admin.TabularInline):
    model = Delivery
    extra = 0
    can_delete = False
    fields = ['state']
    def view_on_site(self, obj):
        return f'/admin/users/delivery/{obj.id}/change/'
    def get_readonly_fields(self, request, obj=None): #pyright:ignore
        return [f.name for f in self.model._meta.fields] #pyright:ignore
    def has_add_permission(self, request, obj):
        return False

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [DeliveryInLine]
    list_display = ('username', 'name', 'phone')
    fieldsets = (
        (None, {'fields': ('username', 'name', 'phone')}),
    )
    def get_readonly_fields(self, request, obj=None): #pyright:ignore
        if obj:
            return [f.name for f in self.model._meta.fields if f.name != 'state']
        return self.readonly_fields
    def has_add_permission(self, request):
        return False
