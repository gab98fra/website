from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CategoryModel, ProductModel
from .forms import CategoryForm, ProductForm



class DashboardView(TemplateView):
    """Dashboard principal

    """
    template_name="dashboard/dashboard.html"


"""Vistas para Category
    -List
    -Create
    -Update
    -Delete
"""

class CategoryListView(ListView):
    model=CategoryModel
    template_name="dashboard/category/list.html"
    queryset=CategoryModel.objects.filter(status=True)
    context_object_name="categories"

class CategoryCreateView(CreateView):
    """ Permite crear el producto con el usuario logeado

        -El usuario se captura en el template, -user- para evitar mostrar los usuarios de la DBA

    """
    model=CategoryModel
    form_class=CategoryForm
    template_name='dashboard/category/register.html'
    context_object_name="form"
    success_url=reverse_lazy("categorylist")


class CategoryUpdateeView(UpdateView):
    model=CategoryModel
    form_class=CategoryForm
    context_object_name="form"
    template_name='dashboard/category/update.html'
    success_url=reverse_lazy("categorylist")
    
class CategoryDeleteView(DeleteView):
    
    model=CategoryModel
    context_object_name="form"
    template_name='dashboard/category/delete.html'

    def post(self, request, pk, *args, **kwargs):
        object=CategoryModel.objects.get(id=pk)
        object.status=False
        object.save()
        return redirect ("categorylist")


"""Vistas para Products
    -List
    -Create
    -Update
    -Delete

"""

class ProductListView(ListView):
    model=ProductModel
    template_name="dashboard/product/list.html"
    queryset=ProductModel.objects.filter(status=True)
    context_object_name="products"

class ProductCreateView(CreateView):
    """ Permite crear el producto con el usuario logeado

        -El usuario se captura en el template, -user- para evitar mostrar los usuarios de la DBA

    """
    model=ProductModel
    form_class=ProductForm
    template_name='dashboard/product/register.html'
    context_object_name="form"
    success_url=reverse_lazy("productlist")


class ProductUpdateeView(UpdateView):
    model=ProductModel
    form_class=ProductForm
    context_object_name="form"
    template_name='dashboard/product/update.html'
    success_url=reverse_lazy("productlist")
    
class ProductDeleteView(DeleteView):
    
    model=ProductModel
    context_object_name="form"
    template_name='dashboard/product/delete.html'

    def post(self, request, pk, *args, **kwargs):
        object=ProductModel.objects.get(id=pk)
        object.status=False
        object.save()
        return redirect ("productlist")

