"""Registro de modelos en Admin

    -Uso de import-export    
    -Funcionalidades
"""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import CategoryModel, ProductModel

class CategoriaResource(resources.ModelResource):
#Botón import y export

    class Meta:
        model=CategoryModel

class CategoryAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    """Funcionalidades

        -Buscador
        -Campos de despliegue
        -Visualizar campos se solo lectura
        -Botón import-export
    """    
    search_fields=['category']
    list_display=("category", "status","created",)
    readonly_fields=("created","updated", "category_user")
    resource_class=CategoriaResource

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


#Registro de modelos
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)

