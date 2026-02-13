from django import forms
from .models import Flower, Supplier

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'category', 'description', 'price', 'quantity_in_stock', 'reorder_level']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'placeholder': '₱0.00'}),
        }
        labels = {
            'price': 'Price (₱)',
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }