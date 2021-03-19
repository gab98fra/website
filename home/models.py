from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField("Nombre",max_length=30)
    apellido=models.CharField("Apellido", max_length=30)
    correo=models.EmailField("Correo")
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre



    