from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (DashboardView, CategoryListView,CategoryCreateView, CategoryUpdateeView, CategoryDeleteView,
                    ProductListView, ProductCreateView, ProductUpdateeView, ProductDeleteView)

urlpatterns = [
    #path('', Home, name="home"),
    path('', DashboardView.as_view(), name="dashboard"),

    #Right Panel - Category
    path('categorylist/', CategoryListView.as_view(), name="categorylist"),
    path('categorycreate/', CategoryCreateView.as_view(), name="categorycreate"),
    path('categoryupdate/<int:pk>', CategoryUpdateeView.as_view(), name="categoryupdate"),
    path('categorydelete/<int:pk>', CategoryDeleteView.as_view(), name="categorydelete"),

    #Right Panel - Products
    path('productsall/', ProductListView.as_view(), name="productlist"),
    path('productscreate/', ProductCreateView.as_view(), name="productcreate"),
    path('productsupdate/<int:pk>', ProductUpdateeView.as_view(), name="productupdate"),
    path('produdctdelete/<int:pk>', ProductDeleteView.as_view(), name="productdelete"),
]
