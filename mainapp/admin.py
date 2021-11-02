from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class WinterAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='wintersneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SummerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='summersneakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)







admin.site.register(Category)
admin.site.register(Winter, WinterAdmin)
admin.site.register(Summer, SummerAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)