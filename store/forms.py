from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    estate form
    """
    class Meta:
        model = Product
        fields = ['name',
                  'producer',
                  'cost',
                  'type',
                  'description',
                  'image',
                  'units']
