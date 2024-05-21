from django.forms import ModelForm #Importacion de la clase para crear formularios en base a modelos
from . import models #Importacion de todos los modelos

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto #Modelo de referencia
        fields = ['nombre', 'stock', 'puntaje', 'categoria'] # Campos que utilizara