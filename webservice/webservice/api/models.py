from django.db import models

# Create your models here.

class TIPO_PRODUCTO(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    class Meta:
        db_table = 'tipo_producto'
    def __str__(self):
        return self.descripcion


class PRODUCTO(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos")
    tipo = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.CASCADE)
    class Meta:
        db_table = 'producto'
    def __str__(self):
        return self.nombre
    




