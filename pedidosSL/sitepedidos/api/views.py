
######################################################################################
############# ----------------------SERIALLIZAÇÂO-------------------------------------
######################################################################################

from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from ..models import (
    Cliente,
    Cad_prod_aluguel,
    Cad_prod_bebida,
    Carrinho_bebidas,
    Endereco_entrega,
    Pedido
)



from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ClienteSerializer,
    Cad_prod_bebidaSerializer,
    Carrinho_bebidasSerializer,
    Endereco_entregaSerializer,
    PedidoSerializer

)


#------------------- Cliente

class ClienteList(APIView):

   def get(self,request):
       cliente = Cliente.objects.all()
       serializer = ClienteSerializer(cliente, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = ClienteSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteMethodObject(APIView):

    def get_object(self, id):
        try:
            return Cliente.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        cliente=self.get_object(id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#------------------- Pedido

class PedidoList(APIView):

   def get(self,request):
       pedido = Pedido.objects.all()
       serializer = PedidoSerializer(pedido, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = PedidoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoMethodObject(APIView):

    def get_object(self, id):
        try:
            return Pedido.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        pedido = self.get_object(id)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        pedido = self.get_object(id)
        serializer = PedidoSerializer(pedido, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        pedido=self.get_object(id)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#------------------- Endereco_entrega

class Endereco_entregaList(APIView):

   def get(self,request):
       entrega = Endereco_entrega.objects.all()
       serializer = Endereco_entregaSerializer(entrega, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = Endereco_entregaSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Endereco_entregaMethodObject(APIView):

    def get_object(self, id):
        try:
            return Endereco_entrega.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        entrega = self.get_object(id)
        serializer = Endereco_entregaSerializer(entrega)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        entrega = self.get_object(id)
        serializer = Endereco_entregaSerializer(entrega, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        entrega=self.get_object(id)
        entrega.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#------------------- Carrinho_bebidas

class Carrinho_bebidasList(APIView):

   def get(self,request):
       carrinho = Carrinho_bebidas.objects.all()
       serializer = Carrinho_bebidasSerializer(carrinho, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = Carrinho_bebidasSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Carrinho_bebidasMethodObject(APIView):

    def get_object(self, id):
        try:
            return Carrinho_bebidas.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        carrinho = self.get_object(id)
        serializer = Carrinho_bebidasSerializer(carrinho)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        carrinho = self.get_object(id)
        serializer = Carrinho_bebidasSerializer(carrinho, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        carrinho=self.get_object(id)
        carrinho.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#------------------- Cad_prod_bebida

class Cad_prod_bebidaList(APIView):

   def get(self,request):
       bebida = Cad_prod_bebida.objects.all()
       serializer = Cad_prod_bebidaSerializer(bebida, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = Cad_prod_bebidaSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cad_prod_bebidaMethodObject(APIView):

    def get_object(self, id):
        try:
            return Cad_prod_bebida.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        bebida = self.get_object(id)
        serializer = Cad_prod_bebidaSerializer(bebida)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        bebida = self.get_object(id)
        serializer = Cad_prod_bebidaSerializer(bebida, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        bebida=self.get_object(id)
        bebida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


