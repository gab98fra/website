from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField("Category", max_length=30, null=False, blank=False)
    category_user=models.ManyToManyField(User, through='ProductModel')#Asociar con dos modelos
    status=models.BooleanField("Status", default=True, )
    created=models.DateField("Created", auto_now_add=True, editable=True)
    updated=models.DateTimeField("Updated", auto_now=True, editable=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["category"]

    def __str__(self):
        return self.category


class ProductModel(models.Model):
    """Relación de uno a muchos

    """
    id = models.AutoField(primary_key=True)
    product=models.CharField("Product",max_length=30)
    quantity=models.IntegerField("Quantity", default=1)
    price=models.FloatField("Price")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created=models.DateField("Created", auto_now_add=True, editable=True)
    updated=models.DateField("Updated", auto_now=True, editable=True)
    status=models.BooleanField("Status", default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["product"]

    def __str__(self):
        return self.product




