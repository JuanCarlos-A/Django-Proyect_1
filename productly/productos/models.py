from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE : Elimina el produto
    # PROTECT : Proteje el producto lanzando un error
    # RESTRICT : Solo elimina el producto si no existen mas produtos con la misma caracteristica (Categoria en este caso)
    # SET_NULL : Set es introduce un valor nulo en el campo
    # SET_DEFAULT : Introduce el valor por defecto
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.nombre