"""Formularios
    -Categoría
    -Producto
"""
from django import forms
from .models import CategoryModel, ProductModel

class CategoryForm(forms.ModelForm):
#Crear Categoría

    class Meta:
        model=CategoryModel
        fields=['category']
        label={
            'category':"Ingressar la categoría",
        }


class ProductForm(forms.ModelForm):
#Crear Producto

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product'].widget.attrs['class']='form-control'
        self.fields['product'].widget.attrs['placeholder']='Ingrese el producto'
        self.fields['quantity'].widget.attrs['class']='form-control'
        self.fields['quantity'].widget.attrs['placeholder']='Ingrese la cantidad'
        self.fields['price'].widget.attrs['class']='form-control'
        self.fields['price'].widget.attrs['placeholder']='Ingrese el precio'
        self.fields['category'].widget.attrs['class']='form-control'
        
    
    class Meta:
        model=ProductModel
        fields=['product', 'quantity','price', 'category', 'user']
        


