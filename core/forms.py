from django import forms
from core.models import Product, Category, Brand, Supplier

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description','price','stock','brand','categories','line','supplier','expiration_date','image','state']

    def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super(ProductForm, self).__init__(*args, **kwargs)
            if user:
                self.fields['categories'].queryset = Category.objects.filter(user=user, state=True)
                self.fields['supplier'].queryset = Supplier.objects.filter(user=user, state=True)
                self.fields['brand'].queryset = Brand.objects.filter(user=user, state=True)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description', 'state']
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields=['name','ruc','address','phone','state']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'state']







