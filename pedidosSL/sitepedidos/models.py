from django.contrib.auth.models import User
from django.db import models
from datetime import datetime



# Create your models here.

class Cliente(models.Model):
    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    user = models.OneToOneField(User, related_name='cliente',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Usuario')
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    primeiro_nome = models.CharField(max_length=20, verbose_name='Primeiro Nome', blank=False, null=False)
    sobre_nome = models.CharField(max_length=20, verbose_name='Sobre Nome', blank=False, null=False)
    cnpj = models.CharField(unique=True, max_length=14, blank=True, null=True, verbose_name='C N P J')
    cpf = models.CharField(unique=True, max_length=11, blank=True, null=True, verbose_name='C P F')
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    endereco = models.CharField(max_length=300, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=6, blank=True, null=True, verbose_name='Numero')
    complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Complemento')
    cep = models.CharField(max_length=10, verbose_name='Cep')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=100, blank=True, null=True, verbose_name='U F')
    telcelular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone celular')
    telfixo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone fixo')
    email = models.EmailField(blank=True, null=True,verbose_name='E-Mail')
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº Whatsapp')
    facebook = models.CharField(max_length=80, blank=True, null=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=80, blank=True, null=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=80, blank=True, null=True, verbose_name='twitter')
    dt_cadastro = models.DateField('Data cadastro', blank=True, null=True, default=datetime.now())
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')

class Endereco_entrega(models.Model):
    user = models.OneToOneField(User, related_name='endereco_entrega',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Usuario')
    endereco = models.CharField(max_length=300, blank=True, null=True, verbose_name='Endereço')
    numero = models.CharField(max_length=6, blank=True, null=True, verbose_name='Numero')
    complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Complemento')
    cep = models.CharField(max_length=10, verbose_name='Cep')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=100, blank=True, null=True, verbose_name='U F')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')


class Cad_prod_bebida(models.Model):
    BEBIDAS_CHOICES = (
        ('KAISER', 'KAISER'),
        ('BRAHMA', 'BRAHMA'),
        ('SKOL', 'SKOL'),
        ('ANTARCTICA', 'ANTARCTICA'),
        ('BOHEMIA', 'BOHEMIA'),
        ('HEINEKEN', 'HEINEKEN'),
        ('STELLA', 'STELLA'),
        ('BAVARIA', 'BAVARIA'),
        ('GLACIAL', 'GLACIAL'),
        ('TIJUCA','TIJUCA'),
        ('PETRA','PETRA'),
        ('SCHIN', 'SCHIN'),
        ('ITAIPAVA', 'ITAIPAVA'),
        ('CRYSTAL', 'CRYSTAL'),
        ('DEVASSA', 'DEVASSA'),
        ('EISENBAHN', 'EISENBAHN'),
        ('CORONA', 'CORONA'),
        ('BUDWEISER', 'BUDWEISER'),
        ('CARACU', 'CARACU'),
        ('BADER','BADER'),
        ('TERESOPOLIS','TERESOPOLIS')

    )
    ordena_choices = sorted(BEBIDAS_CHOICES, key=lambda x: x[1])
    BEBIDAS_CHOICES = ordena_choices

    TAMANHO_CHOICES = (
        ('LONG NECK 250 ML', 'LONG NECK 250 ML'),
        ('LONG NECK 275 ML', 'LONG NECK 275 ML'),
        ('LONG NECK 330 ML', 'LONG NECK 330 ML'),
        ('LONG NECK 350 ML', 'LONG NECK 350 ML'),
        ('LONG NECK 355 ML', 'LONG NECK 355 ML'),
        ('LITRO 600 ML', 'LITRO 600 ML'),
        ('LITRAO 990 ML', 'LITRAO 990 ML'),
        ('LITRAO 1000 ML', 'LITRAO 1000 ML'),
        ('LATINHA 269 ML', 'LATINHA 269 ML'),
        ('LATA 350 ML', 'LATA 350 ML'),
        ('LATAO 473 ML', 'LATAO 473 ML'),
        ('LATAO 550 ML', 'LATA 550 ML'),
        ('PERIGUETE 300 ML', 'PERIGUETE 300 ML'),

    )

    ordena_choices = sorted(TAMANHO_CHOICES, key=lambda x: x[1])
    TAMANHO_CHOICES = ordena_choices

    PARAOSITE = (
        ('SIM', 'SIM'),
        ('NAO', 'NAO')
    )

    bebida = models.CharField(max_length=100, verbose_name='Bebida', choices=BEBIDAS_CHOICES,
                              help_text='Selecione o produto')
    complemento = models.CharField(max_length=200, blank=True, null=True,
                                   verbose_name='Descrição Complementar',
                                   help_text='Digite o complemento de informações do produto')
    tamanho = models.CharField(max_length=100, verbose_name='Tamanho', choices=TAMANHO_CHOICES,
                               help_text='Selecione a quantidade/tamanho')
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Valor R$',
                                help_text='Informe o valor')
    url_imagem = models.CharField(max_length=600, blank=True, null=True,
                                  verbose_name='URL da Imagem do Produto',
                                  help_text='Digite a url de endereço da imagem')
    foto = models.FileField (upload_to='media/images/produtos', blank=True, null=True,
                             verbose_name='Foto do Produto',
                             help_text='Selecione a foto do produto')
    site = models.CharField(max_length=3, verbose_name='Para apresentação no site?',
                            default = "SIM", choices=PARAOSITE,
                            help_text='Informe se o produto vai aparecer no site')
    dt_inicio = models.DateField('Data inicio da apresentação', blank=True, null=True,
                                 default= datetime.now())
    dt_final = models.DateField('Data final da apresentação',  blank=True, null=True,
                                default= datetime.now())

    def __str__(self):
        return self.bebida +  " " + self.tamanho

    class Meta:
        ordering = ['bebida']


class Cad_prod_aluguel(models.Model):
    PRODUTO_CHOICES = (
        ('MESA', 'MESA'),
        ('CADEIRA', 'CADEIRA'),
        ('TOALHA DE MESA', 'TOALHA DE MESA'),
        ('GUARDANAPOS', 'GUARDANAPOS'),
        ('CONJUNTO DE MESA COM CADEIRAS', 'CONJUNTO DE MESA COM CADEIRAS'),
        ('CONJUNTO DE MESA COM CADEIRAS E TOALHAS', 'CONJUNTO DE MESA COM CADEIRAS E TOALHAS'),
        ('FREEZER', 'FREEZER'),
        ('OUTROS', 'OUTROS')
    )

    PARAOSITE = (
        ('SIM','SIM'),
        ('NAO','NAO')
    )

    produto = models.CharField(max_length=100, verbose_name='Produto',
                               choices=PRODUTO_CHOICES)
    descricao = models.CharField(max_length=200, blank=True, null=True,
                                 verbose_name='Descrição Complementar')
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Valor R$')
    url_imagem = models.CharField(max_length=500, blank=True, null=True,
                                  verbose_name='URL da Imagem do Produto')
    foto = models.ImageField(upload_to='sitepedidos/static/css/imgCadastro',
                             blank=True, null=True, verbose_name='Foto do Produto')
    site = models.CharField(max_length=3, verbose_name='Para apresentação no site?',
                            default = "SIM", choices=PARAOSITE)
    dt_inicio = models.DateField('Data inicio da apresentação', blank=True, null=True,
                                 default= datetime.now())
    dt_final = models.DateField('Data final da apresentação', blank=True, null=True,
                                default= datetime.now())

class Pedido(models.Model):
    TIPO_PEDIDO = (
        ('1', 'CONVENIENCIA'),
        ('2', 'ALUGUEIS'),
        ('3', 'OUTROS')
    )

    SITUACAO_PEDIDO = (
        ('0', 'ABERTO'),
        ('1', 'FECHADO'),
        ('2', 'CANCELADO')
    )

    user = models.ForeignKey(User, related_name='pedido',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Usuario')

    tipo_pedido = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Tipo de Pedido',
        choices=TIPO_PEDIDO
    )
    dt_abertura = models.DateField('Data de abertura do pedido',
        blank=True,
        null=True,
        default=datetime.now()

    )
    dt_fechamento = models.DateField('Data fechamento do pedido',
        blank=True,
        null=True

    )

    dt_cancelamento = models.DateField('Data cancelamento do pedido',
        blank=True,
        null=True
    )

    situacao = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Situação do pedido',
        choices = SITUACAO_PEDIDO
    )

    valor = models.DecimalField(
        max_digits=12,
        blank=True,
        null=True,
        decimal_places=2,
        verbose_name='Valor do pedido R$')

    def __str__(self):
        return str(self.id)




class Carrinho_bebidas(models.Model):
    SITUACAO_CARRINHO_BEB = (
        ('0', 'ABERTO'),
        ('1', 'FECHADO'),
        ('2', 'CANCELADO')
    )
    user = models.ForeignKey(User, related_name='carrinho_bebidas',
                             on_delete=models.CASCADE,
                             null=True,
                             verbose_name='Usuario')

    produto = models.ForeignKey(Cad_prod_bebida, related_name='carrinho_bebidas',
        on_delete=models.CASCADE,
        null=True,
        verbose_name= 'Produto'
    )

    pedido = models.ForeignKey(Pedido, related_name='carrinho_bebidas',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Pedido'
    )

    dt_inclusao = models.DateField('Data de inclusão no carrinho',
        blank=True,
        null=True,
        editable=True,
        default= datetime.now()
    )
    valor_unitario = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name='Valor unitario R$'
    )
    quantidade = models.DecimalField(
        max_digits=7, decimal_places=2,
        verbose_name='Quntidade de itens'
    )
    valor_total_item = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Valor Total R$'
    )
    situacao_carrinho = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name='Situação do carrinho',
        choices=SITUACAO_CARRINHO_BEB
    )


