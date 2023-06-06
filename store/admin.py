from django.contrib import admin

from .models import Product, Producer, ProductType, Client
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    register estate
    """
    list_display = ['name',
                    'producer',
                    'image',
                    'cost',
                    'type',
                    'units']
    list_filter = ['producer',
                   'type']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    """
    register owner
    """
    list_display = ['name',
                    'country']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    register type of estate
    """
    list_display = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    register client
    """
    list_display = ['first_name', 'last_name',
                    'date_of_birth',
                    'email',
                    'phone_number']
    