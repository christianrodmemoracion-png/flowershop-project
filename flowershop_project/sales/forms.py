from django import forms
from .models import Sale, Customer
from inventory.models import Flower

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['flower', 'quantity', 'unit_price', 'customer_name', 'customer_email', 'payment_method']
        labels = {
            'unit_price': 'Unit Price (₱)',
        }
        widgets = {
            'unit_price': forms.NumberInput(attrs={'placeholder': '₱0.00'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }