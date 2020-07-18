from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from .models import (
    Cliente,
    Cad_prod_aluguel,
    Cad_prod_bebida,
    Carrinho_bebidas,
    Endereco_entrega,
    Pedido
)


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Sum, Count


# Create your views here.

class TotalizaCarrinho:

    def setListaCarrinho(self,usuario):
        self.lista_carrinho =\
            Carrinho_bebidas.objects.filter(user=usuario,
                                            situacao_carrinho=0);

    def setVlTotalCarrinho(self,usuario):
        lista_carrinho = \
            Carrinho_bebidas.objects.filter(user=usuario,
                                            situacao_carrinho=0);
        vlTotCar  = 0
        for tot in lista_carrinho:
            vlTotCar = vlTotCar + tot.valor_total_item

        self.vlTotalCarrinho = vlTotCar

    def setQtTotalCarrinho(self,usuario):
        lista_carrinho = \
            Carrinho_bebidas.objects.filter(user=usuario,
                                            situacao_carrinho=0);
        qtTotCar = 0
        for tot in lista_carrinho:
            qtTotCar = qtTotCar + 1

        self.qtTotalCarrinho = qtTotCar

    def getListacarrinho(self):
        return self.lista_carrinho

    def getVlTotalCarrinho(self):
        return self.vlTotalCarrinho

    def getQtTotalCarrinho(self):
        return self.qtTotalCarrinho



def stpedidos(request):

    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)
    dados = {
        'lista_carrinho': totCarrinho.getListacarrinho(),
        'vlTotalCarrinho': totCarrinho.getVlTotalCarrinho(),
        'qtTotalCarrinho': totCarrinho.getQtTotalCarrinho()
    }

    return render(request,'index.html',dados)


def pedBebidas(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    lista_bebidas = Cad_prod_bebida.objects.filter(site="SIM")
    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)

    dados = {
        'lista_bebidas': lista_bebidas,
        'lista_carrinho': totCarrinho.getListacarrinho(),
        'vlTotalCarrinho': totCarrinho.getVlTotalCarrinho(),
        'qtTotalCarrinho': totCarrinho.getQtTotalCarrinho()
    }
    return render(request, 'pedBebidas.html',dados)


def pedAluguel(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)

    dados = {
        'lista_carrinho': totCarrinho.getListacarrinho(),
        'vlTotalCarrinho': totCarrinho.getVlTotalCarrinho(),
        'qtTotalCarrinho': totCarrinho.getQtTotalCarrinho()
    }

    return render(request, 'pedAluguel.html',dados)


def sobreoSite(request):
    return render(request, 'sobreoSite.html')


def telaCadastroUsuario(request):  # aqui carregamos o form com os campos da tabela

    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

   # totCarrinho = TotalizaCarrinho()
   # totCarrinho.setListaCarrinho(usuario)
   # totCarrinho.setVlTotalCarrinho(usuario)
   # totCarrinho.setQtTotalCarrinho(usuario)

    if request.user.is_authenticated:

        usuario = User.objects.get(id=request.user.id)

        dados = {'usuario': usuario,
                # 'lista_carrinho': totCarrinho.getListacarrinho(),
                # 'vlTotalCarrinho': totCarrinho.getVlTotalCarrinho(),
                # 'qtTotalCarrinho': totCarrinho.getQtTotalCarrinho()
        }

    else:
        dados = {'usuario': usuario}
   #     dados = {'lista_carrinho': totCarrinho.lista_carrinho,
   #              'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
   #              'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
   #              }

    return render(request,'cadUsuario.html',dados)


def telaCadastroClientes(request,id):  # aqui carregamos o form com os campos da tabela

    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

   # totCarrinho = TotalizaCarrinho()
   # totCarrinho.setListaCarrinho(usuario)
   # totCarrinho.setVlTotalCarrinho(usuario)
   # totCarrinho.setQtTotalCarrinho(usuario)

    if request.user.is_authenticated:
        user_cliente = User.objects.get(id = id);
        cliente_u = Cliente.objects.filter(user=user_cliente).first();

        dados = {'User_cliente': user_cliente,
    #             'lista_carrinho': totCarrinho.lista_carrinho,
    #             'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
    #             'qtTotalCarrinho': totCarrinho.qtTotalCarrinho,
                 'Cliente_u': cliente_u
        }

    #else:

     #   dados = {'lista_carrinho': totCarrinho.lista_carrinho,
     #            'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
     #            'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
     #   }


    return render(request,'cadClientes.html',dados)

def gravaAlteraUsuarioNovo(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            user_altera = User.objects.get(id=request.user.id);

            user_altera.set_password('senha');

            user_altera.email = request.POST.get('email');
            user_altera.username = request.POST.get('email');
            user_altera.first_name = request.POST.get('primeiro_nome');
            user_altera.last_name = request.POST.get('sobre_nome');

            user_altera.save()

            return redirect('/accounts/logout/');

        else:

            #user = User.objects.create_user('myusername',
            #                                'myemail@crazymail.com',
            #                                'mypassword')
            user_add = User.objects.create_user(request.POST.get('email'),
                                            request.POST.get('email'),
                                            request.POST.get('senha'))

            user_add.first_name = request.POST.get('primeiro_nome');
            user_add.last_name = request.POST.get('sobre_nome');


            user_add.save()

            messages.info(request, 'Usuario Cadastrado com Sucesso')
            return redirect('/accounts/login/');

def gravaAlteraClienteNovo(request,id):   # aqui vamos gravar os dados do form na tabela Cliente

    if request.method == 'POST':
        user_User = User.objects.get(id=id)

        alteraCLI = Cliente.objects.filter(user=user_User).first()

        if alteraCLI is not None:

            alteraCLI.nome = (request.POST.get('primeiro_nome') + " " +
                              request.POST.get('sobre_nome'));
            alteraCLI.primeiro_nome = request.POST.get('primeiro_nome');
            alteraCLI.sobre_nome = request.POST.get('sobre_nome');
            alteraCLI.cpf = request.POST.get('cpf');
            alteraCLI.endereco = request.POST.get('endereco');
            alteraCLI.numero = request.POST.get('numero');
            alteraCLI.complemento = request.POST.get('complemento');
            alteraCLI.cep = request.POST.get('cep');
            alteraCLI.bairro = request.POST.get('bairro');
            alteraCLI.cidade = request.POST.get('cidade');
            alteraCLI.estado = request.POST.get('estado');
            alteraCLI.telcelular = request.POST.get('telcelular');
            alteraCLI.telfixo = request.POST.get('telfixo');
            alteraCLI.latitude = request.POST.get('latitudeEnt');
            alteraCLI.longitude = request.POST.get('longitudeEnt');

            alteraCLI.save();
            messages.info(request, 'Cliente atualizado com sucesso')

        else:

            gravaCLI = Cliente();

            gravaCLI.user = user_User;
            gravaCLI.nome = (request.POST.get('primeiro_nome') + " " +
                              request.POST.get('sobre_nome'));
            gravaCLI.primeiro_nome = request.POST.get('primeiro_nome');
            gravaCLI.sobre_nome = request.POST.get('sobre_nome');
            gravaCLI.cpf = request.POST.get('cpf');
            gravaCLI.endereco = request.POST.get('endereco');
            gravaCLI.numero = request.POST.get('numero');
            gravaCLI.complemento = request.POST.get('complemento');
            gravaCLI.cep = request.POST.get('cep');
            gravaCLI.bairro = request.POST.get('bairro');
            gravaCLI.cidade = request.POST.get('cidade');
            gravaCLI.estado = request.POST.get('estado');
            gravaCLI.telcelular = request.POST.get('telcelular');
            gravaCLI.telfixo = request.POST.get('telfixo');
            gravaCLI.latitude = request.POST.get('latitudeEnt');
            gravaCLI.longitude = request.POST.get('longitudeEnt');

            gravaCLI.save()

            messages.info(request, 'Cliente cadastrado com sucesso')


        alteraEND_ENT = Endereco_entrega.objects.filter(user=user_User).first()

        if alteraEND_ENT is not None:
            alteraEND_ENT.endereco = request.POST.get('enderecoEnt');
            alteraEND_ENT.numero = request.POST.get('numeroEnt');
            alteraEND_ENT.complemento = request.POST.get('complementoEnt');
            alteraEND_ENT.cep = request.POST.get('cepEnt');
            alteraEND_ENT.bairro = request.POST.get('bairroEnt');
            alteraEND_ENT.cidade = request.POST.get('cidadeEnt');
            alteraEND_ENT.estado = request.POST.get('estadoEnt');
            alteraEND_ENT.latitude = request.POST.get('latitudeEnt');
            alteraEND_ENT.longitude = request.POST.get('longitudeEnt');


            alteraEND_ENT.save()
        else:
            gravaEND_ENT = Endereco_entrega()

            gravaEND_ENT.user = user_User;
            gravaEND_ENT.endereco = request.POST.get('enderecoEnt');
            gravaEND_ENT.numero = request.POST.get('numeroEnt');
            gravaEND_ENT.complemento = request.POST.get('complementoEnt');
            gravaEND_ENT.cep = request.POST.get('cepEnt')
            gravaEND_ENT.bairro = request.POST.get('bairroEnt');
            gravaEND_ENT.cidade = request.POST.get('cidadeEnt');
            gravaEND_ENT.estado = request.POST.get('estadoEnt');
            gravaEND_ENT.latitude = request.POST.get('latitudeEnt');
            gravaEND_ENT.longitude = request.POST.get('longitudeEnt');

            gravaEND_ENT.save()


        return redirect('telaCadastroClientes',user_User.id)




def colocarCarrinho(request, id):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)

    itemNoCarrinho = Cad_prod_bebida.objects.get(id=id)

    dados = {
        'itemNoCarrinho': itemNoCarrinho,
        'lista_carrinho': totCarrinho.lista_carrinho,
        'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
        'qtTotalCarrinho': totCarrinho.qtTotalCarrinho

    }
    return render(request, 'colocarCarrinho.html',dados)



def gravaItemCarrinho(request):

    if request.method == 'POST':
                #-selecionar usuario logado
        user_carrinho = User.objects.get(id=request.user.id);
        id_prod_bebida = request.POST.get('produto');
        cadprod_bebida = Cad_prod_bebida.objects.filter(id=id_prod_bebida).first();

        #--- verei se tem pedidos em aberto
        cad_pedido = Pedido.objects.filter(user=user_carrinho,situacao=0).first();


        # NAO TEM PEDIDO ABERTO, VAMOS ABRIR UM
        if cad_pedido is None:
            pedidoADD = Pedido();

            pedidoADD.user = user_carrinho;
            pedidoADD.situacao = 0;
            pedidoADD.tipo_pedido =  1;
            pedidoADD.dt_abertura = datetime.now();
            #pedidoADD.valor =  1000;

            pedidoADD.save()

            # APOS GRAVAR O PEDIDO, VAMOS CARREGAR PRA GRAVAR NO CARRINHO
            cad_pedido = pedidoADD;

        if cadprod_bebida is not None:
            carrinhoB = Carrinho_bebidas();

            carrinhoB.user = user_carrinho;       #aqui vamos gravar o usuario relacionado no carrinho
            carrinhoB.produto = cadprod_bebida;   #aqui vamos gravar o produto relacionado no carrinho
            carrinhoB.pedido = cad_pedido;   #aqui vamos gravar o pedido relacionado
            carrinhoB.valor_unitario = request.POST.get('valor_unitario');
            carrinhoB.quantidade = request.POST.get('quantidade');
            carrinhoB.valor_total_item = request.POST.get('valor_total_item');
            carrinhoB.situacao_carrinho = 0;

            carrinhoB.save()

        #-- AQUI O PEDIDO JA FOI GRAVADO, VAMOS ATUALIZAZ O VALOR

        if cad_pedido is not None:
            atualizaValorPedido = Carrinho_bebidas.objects.filter(pedido=cad_pedido)
            vlTotPed = 0
            for totped in atualizaValorPedido:
                vlTotPed = vlTotPed + totped.valor_total_item

            cad_pedido.valor = vlTotPed;
            cad_pedido.save();


        messages.success(request, 'Item foi adicionado no carrinho')
        return redirect('pedBebidas')



def itensDoCarrinho(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    #totCarrinho.setVlTotalCarrinho(usuario)
    #totCarrinho.setQtTotalCarrinho(usuario)

    dados = {
        'lista_carrinhoL': totCarrinho.lista_carrinho,
    #    'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
    #    'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
    }

    return render(request, 'itensDoCarrinho.html', dados)


def alteraItensDoCarrinho(request, id):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)

    altera_carrinho = Carrinho_bebidas.objects.get(id=id)

    dados = {
        'altera_carrinho': altera_carrinho,
        'lista_carrinho': totCarrinho.lista_carrinho,
        'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
        'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
    }

    return render(request, 'alterarCarrinho.html', dados)

def confirmaAlteraItensDoCarrinho(request, id):
    if request.method == 'POST':
        #alteraItemDoCarrinho = Carrinho_bebidas.objects.get(id=id)

        carrinhoALT = Carrinho_bebidas.objects.get(id=id)
        carrinhoALT.valor_unitario = request.POST.get('valor_unitario')
        carrinhoALT.quantidade = request.POST.get('quantidade')
        carrinhoALT.valor_total_item = request.POST.get('valor_total_item')

        carrinhoALT.save()
    messages.info(request, 'Item atualizado com sucesso')
    return redirect('itensDoCarrinho')



def confirmaRetirarItemCarrinho(request,id):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

    totCarrinho = TotalizaCarrinho()
    totCarrinho.setListaCarrinho(usuario)
    totCarrinho.setVlTotalCarrinho(usuario)
    totCarrinho.setQtTotalCarrinho(usuario)

    moveItemDoCarrinho = Carrinho_bebidas.objects.get(id=id)

    dados2 = {
        'moveItemDoCarr': moveItemDoCarrinho,
        'lista_carrinho': totCarrinho.lista_carrinho,
        'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
        'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
    }

    return render(request,'confirmaRetirarItemCarrinho.html', dados2)


def deletaItemCarrinho(request, id):
    deletaitem = Carrinho_bebidas.objects.get(id=id)
    if request.method == "POST":
        deletaitem.delete()

    messages.info(request, 'Item retirado do carrinho com sucesso')
    return redirect('itensDoCarrinho')

def listaPedidos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

   # totCarrinho = TotalizaCarrinho()
   # totCarrinho.setListaCarrinho(usuario)
   # totCarrinho.setVlTotalCarrinho(usuario)
   # totCarrinho.setQtTotalCarrinho(usuario)

    lista_Pedidos = Pedido.objects.filter(user = usuario)

    dados = {
        'Lista_Pedidos': lista_Pedidos,
    #    'lista_carrinho': totCarrinho.lista_carrinho,
    #    'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
    #    'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
    }

    return render(request, 'listaPedidos.html', dados)

def itensDoPedido(request, id):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
    else:
        usuario = 0

   # totCarrinho = TotalizaCarrinho()
   # totCarrinho.setListaCarrinho(usuario)
   # totCarrinho.setVlTotalCarrinho(usuario)
   # totCarrinho.setQtTotalCarrinho(usuario)

    id_pedido = Pedido.objects.get(id=id)
    listaItensDoPedido = Carrinho_bebidas.objects.filter(pedido=id_pedido)


    dados = {
        'Id_pedido': id_pedido,
        'ListaItensDoPedido': listaItensDoPedido,
    #    'lista_carrinho': totCarrinho.lista_carrinho,
    #    'vlTotalCarrinho': totCarrinho.vlTotalCarrinho,
    #    'qtTotalCarrinho': totCarrinho.qtTotalCarrinho
    }

    return render(request, 'itensDoPedido.html', dados)

def finalizaCompra(request):

    user_pedido = User.objects.get(id=request.user.id);

    #--- verei se tem pedidos em aberto
    finaliza_pedido = Pedido.objects.filter(user=user_pedido,situacao=0).first();

    finaliza_Itens = Carrinho_bebidas.objects.filter(pedido=finaliza_pedido)

    if finaliza_pedido is not None:

        vlTotPed = 0
        for totped in finaliza_Itens:
            vlTotPed = vlTotPed + totped.valor_total_item

        finaliza_pedido.valor =  vlTotPed;
        finaliza_pedido.situacao = 1;
        finaliza_pedido.dt_fechamento = datetime.now();
        finaliza_pedido.save();

        finaliza_Itens.update(situacao_carrinho=1);

    messages.info(request, 'Compra finalizada com sucesso')

    return redirect('inicio')


