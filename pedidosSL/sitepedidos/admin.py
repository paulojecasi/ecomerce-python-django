

from django.contrib import admin

# Register your models here.

from .models import(
    Cliente,
    Cad_prod_bebida,
    Cad_prod_aluguel,
    Carrinho_bebidas,
    Pedido,
    Endereco_entrega
)


class ClienteAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('id','nome','cpf','cidade')         #-campos p/ aparecer na lista
    list_filter = ('bairro','cidade')                            #-adc um filtro na tela
    search_fields = ('id','nome','bairro','cidade','endereco')  #-cria um campo de busca


class Cad_bebidaAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('id', 'bebida','complemento','tamanho','valor','site')      #-campos p/ aparecer na lista
    list_filter = ('bebida','complemento','tamanho','valor')       #-adc um filtro na tela
    search_fields = ('bebida','complemento','tamanho','valor')     #-cria um campo de busca


class Cad_produtoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('produto','descricao','valor','site')         #-campos p/ aparecer na lista
    list_filter = ('produto','descricao')                            #-adc um filtro na tela
    search_fields = ('produto','descricao')  #-cria um campo de busca

class Cad_itemCarrinho(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('id', 'produto','quantidade','valor_unitario','valor_total_item')  #-campos p/ aparecer na lista
    list_filter = ('produto','dt_inclusao','pedido','user')                            #-adc um filtro na tela
    search_fields = ('produto','dt_inclusao','pedido','user')  #-cria um campo de busca

class PedidoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('id','user','dt_abertura','dt_fechamento','situacao','valor')         #-campos p/ aparecer na lista
    list_filter = ('dt_abertura','situacao')                            #-adc um filtro na tela
    search_fields = ('id','dt_abertura','situacao')  #-cria um campo de busca

class EntregaAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')                        #-campos p/ aparecer no cadastro
    list_display = ('id','user','endereco','bairro','cidade')         #-campos p/ aparecer na lista
    list_filter = ('id','bairro','cidade','endereco')                            #-adc um filtro na tela
    search_fields = ('id','bairro','cidade','endereco')  #-cria um campo de busca



admin.site.register(Cad_prod_bebida,Cad_bebidaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Cad_prod_aluguel,Cad_produtoAdmin)
admin.site.register(Carrinho_bebidas,Cad_itemCarrinho)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Endereco_entrega,EntregaAdmin)

