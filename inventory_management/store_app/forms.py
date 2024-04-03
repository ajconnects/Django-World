from django import forms
from .models import Product, Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["username", "address", "email", "phone"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "stock", "price", "supplier"]

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be positive.")
        return price