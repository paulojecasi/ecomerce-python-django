from django.contrib import admin
from django.urls import path, include
from .views import(
   stpedidos,
   pedBebidas,
   pedAluguel,
   sobreoSite,
   colocarCarrinho,
   telaCadastroClientes,
   gravaAlteraClienteNovo,
   gravaItemCarrinho,
   itensDoCarrinho,
   deletaItemCarrinho,
   confirmaRetirarItemCarrinho,
   alteraItensDoCarrinho,
   confirmaAlteraItensDoCarrinho,
   gravaAlteraUsuarioNovo,
   telaCadastroUsuario,
   listaPedidos,
   finalizaCompra,
   itensDoPedido,

)

from .api.views import(
   ClienteList,
   ClienteMethodObject,
   PedidoList,
   PedidoMethodObject,
   Endereco_entregaList,
   Endereco_entregaMethodObject,
   Cad_prod_bebidaList,
   Cad_prod_bebidaMethodObject,
   Carrinho_bebidasList,
   Carrinho_bebidasMethodObject

)

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
   path('',stpedidos, name ="inicio"),
   path('bebidas/',pedBebidas, name="pedBebidas"),
   path('aluguel/',pedAluguel),
   path('sobre/',sobreoSite, name = 'sobreoSite'),
   path('nocarrinho/<int:id>',colocarCarrinho, name = 'colocarCarrinho'),

   path('tela-cadastro-clientes/<int:id>',telaCadastroClientes, name="telaCadastroClientes"),
   path('grava-cliente-novo/<int:id>',gravaAlteraClienteNovo, name='gravaAlteraClienteNovo'),

   path('tela-usuario/',telaCadastroUsuario, name="telaCadastroUsuario"),
   path('grava-usuario-novo/',gravaAlteraUsuarioNovo, name='gravaAlteraUsuarioNovo'),

   path('itenscarrinho/',itensDoCarrinho, name='itensDoCarrinho'),
   path('gravaitemcarrinho/',gravaItemCarrinho, name='gravaItemCarrinho'),

   path('altera-item-do-carrinho/<int:id>',alteraItensDoCarrinho,
        name='alteraItensDoCarrinho'),
   path('confirma-altera-itens-do-carrinho/<int:id>',confirmaAlteraItensDoCarrinho,
        name='confirmaAlteraItensDoCarrinho'),

   path('confirma-retirar-item-carrinho/<int:id>',confirmaRetirarItemCarrinho,
        name = 'confirmaRetirarItemCarrinho'),
   path('deletaitem/<int:id>',deletaItemCarrinho, name = 'deletaItemCarrinho'),

   path('lista-de-pedidos/',listaPedidos, name='listaPedidos'),
   path('itens-do-pedido/<int:id>',itensDoPedido, name='itensDoPedido'),

   path('finalizar-compra/',finalizaCompra, name='finalizaCompra'),



   # --- DA SERIALIZAÇÃO


   path('sclientes/', ClienteList.as_view()),
   path('scliente/<int:id>', ClienteMethodObject.as_view()),

   path('spedidos/', PedidoList.as_view()),
   path('spedido/<int:id>', PedidoMethodObject.as_view()),

   path('senderecos-ent/', Endereco_entregaList.as_view()),
   path('sendereco-ent/<int:id>', Endereco_entregaMethodObject.as_view()),

   path('scadastro-bebidas/', Cad_prod_bebidaList.as_view()),
   path('scadastro-bebida/<int:id>', Cad_prod_bebidaMethodObject.as_view()),

   path('scarrinhos/', Carrinho_bebidasList.as_view()),
   path('scarrinho/<int:id>', Carrinho_bebidasMethodObject.as_view())


   # path('clientes/', include('cliente.urls')),

]