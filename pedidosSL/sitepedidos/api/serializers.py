from rest_framework import serializers
from ..models import (
    Cliente,
    Pedido,
    Endereco_entrega,
    Carrinho_bebidas,
    Cad_prod_bebida
)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class Endereco_entregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco_entrega
        fields = '__all__'

class Carrinho_bebidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho_bebidas
        fields = '__all__'

class Cad_prod_bebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cad_prod_bebida
        fields = '__all__'