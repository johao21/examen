import re
from django.shortcuts import render
from rest_framework.response import Response #permite al ususario retornar respuesta
from rest_framework.views import APIView #permite crear endpint
from .models import TIPO_PRODUCTO, PRODUCTO
# Create your views here.

class HolaMundo(APIView):
    def get(self, request):
        nombre = request.GET.get("nombre")
        return Response({"response":"Hola " +nombre})

    def post(self, request):
        if("nombre" not in request.data):
            return Response({"response":"Faltan datos"})
        nombre = request.data.get("nombre")
        return Response({"response":"Hola "+nombre})

class TipoProductoApi(APIView):
     
    #agregar prductos 
    def post(self, request):            
        if("nombre" in request.data):
            nombre = request.data.get("nombre")
            tipoObj = TIPO_PRODUCTO()
            tipoObj.descripcion = nombre
            tipoObj.save()
            #insert into tipo_producto values(NULL,'nombre');
            return Response({"response":"Tipo de producto guardado"})

    #ver el listado de productos
    def get(self,request):
        lista = TIPO_PRODUCTO.objects.all().values()
        #select * from tipo_producto;
        return Response(lista)

    #modificar tipo de productos
    def put(self,request):
        if("id_tipo" in request.data):
            id_tipo = request.data.get("id_tipo")
            try:
                tipoProducto = TIPO_PRODUCTO.objects.get(id_tipo_producto = id_tipo)
            except TIPO_PRODUCTO.DoesNotExist:
                return Response ({"response":"Tipo de producto no existe"})
            tipoProducto.descripcion = request.data.get("nombre")
            tipoProducto.save()
            return Response({"response":"Tipo de producto actualizado"})

    #borrar
    def delete(self,request):
        id_tipo = request.data.get("id_tipo")
        try:
            tipoProducto = TIPO_PRODUCTO.objects.get(id_tipo_producto = id_tipo)
        except TIPO_PRODUCTO.DoesNotExist:
            return Response ({"response":"Tipo de producto no existe"})
        tipoProducto.delete()
        return Response({"response":"Articulo eliminado correctamente"})

class productoApi(APIView):
    def get(self,request):
        productos = PRODUCTO.objects.all().values()
        return Response (productos)
