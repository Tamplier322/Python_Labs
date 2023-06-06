'''
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    register order(deal) form
    """
    class Meta:
        model = Order
        fields = ['client']
'''