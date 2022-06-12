from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class SneakersAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BootsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='boots'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)







admin.site.register(Category)
admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(Boots, BootsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)