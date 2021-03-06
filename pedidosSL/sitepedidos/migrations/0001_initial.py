# Generated by Django 3.0.6 on 2020-07-06 16:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_prod_aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(choices=[('MESA', 'MESA'), ('CADEIRA', 'CADEIRA'), ('TOALHA DE MESA', 'TOALHA DE MESA'), ('GUARDANAPOS', 'GUARDANAPOS'), ('CONJUNTO DE MESA COM CADEIRAS', 'CONJUNTO DE MESA COM CADEIRAS'), ('CONJUNTO DE MESA COM CADEIRAS E TOALHAS', 'CONJUNTO DE MESA COM CADEIRAS E TOALHAS'), ('FREEZER', 'FREEZER'), ('OUTROS', 'OUTROS')], max_length=100, verbose_name='Produto')),
                ('descricao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição Complementar')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor R$')),
                ('url_imagem', models.CharField(blank=True, max_length=500, null=True, verbose_name='URL da Imagem do Produto')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='sitepedidos/static/css/imgCadastro', verbose_name='Foto do Produto')),
                ('site', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], default='SIM', max_length=3, verbose_name='Para apresentação no site?')),
                ('dt_inicio', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 101392), null=True, verbose_name='Data inicio da apresentação')),
                ('dt_final', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 101392), null=True, verbose_name='Data final da apresentação')),
            ],
        ),
        migrations.CreateModel(
            name='Cad_prod_bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bebida', models.CharField(choices=[('ANTARCTICA', 'ANTARCTICA'), ('BADER', 'BADER'), ('BAVARIA', 'BAVARIA'), ('BOHEMIA', 'BOHEMIA'), ('BRAHMA', 'BRAHMA'), ('BUDWEISER', 'BUDWEISER'), ('CARACU', 'CARACU'), ('CORONA', 'CORONA'), ('CRYSTAL', 'CRYSTAL'), ('DEVASSA', 'DEVASSA'), ('EISENBAHN', 'EISENBAHN'), ('GLACIAL', 'GLACIAL'), ('HEINEKEN', 'HEINEKEN'), ('ITAIPAVA', 'ITAIPAVA'), ('KAISER', 'KAISER'), ('PETRA', 'PETRA'), ('SCHIN', 'SCHIN'), ('SKOL', 'SKOL'), ('STELLA', 'STELLA'), ('TIJUCA', 'TIJUCA')], help_text='Selecione o produto', max_length=100, verbose_name='Bebida')),
                ('complemento', models.CharField(blank=True, help_text='Digite o complemento de informações do produto', max_length=200, null=True, verbose_name='Descrição Complementar')),
                ('tamanho', models.CharField(choices=[('LATA 350 ML', 'LATA 350 ML'), ('LATAO 550 ML', 'LATA 550 ML'), ('LATAO 473 ML', 'LATAO 473 ML'), ('LATINHA 269 ML', 'LATINHA 269 ML'), ('LITRAO 1000 ML', 'LITRAO 1000 ML'), ('LITRAO 990 ML', 'LITRAO 990 ML'), ('LITRO 600 ML', 'LITRO 600 ML'), ('LONG NECK 250 ML', 'LONG NECK 250 ML'), ('LONG NECK 275 ML', 'LONG NECK 275 ML'), ('LONG NECK 330 ML', 'LONG NECK 330 ML'), ('LONG NECK 350 ML', 'LONG NECK 350 ML'), ('LONG NECK 355 ML', 'LONG NECK 355 ML'), ('PERIGUETE 300 ML', 'PERIGUETE 300 ML')], help_text='Selecione a quantidade/tamanho', max_length=100, verbose_name='Tamanho')),
                ('valor', models.DecimalField(decimal_places=2, help_text='Informe o valor', max_digits=12, verbose_name='Valor R$')),
                ('url_imagem', models.CharField(blank=True, help_text='Digite a url de endereço da imagem', max_length=500, null=True, verbose_name='URL da Imagem do Produto')),
                ('foto', models.FileField(blank=True, help_text='Selecione a foto do produto', null=True, upload_to='media/images/produtos', verbose_name='Foto do Produto')),
                ('site', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], default='SIM', help_text='Informe se o produto vai aparecer no site', max_length=3, verbose_name='Para apresentação no site?')),
                ('dt_inicio', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 100392), null=True, verbose_name='Data inicio da apresentação')),
                ('dt_final', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 100392), null=True, verbose_name='Data final da apresentação')),
            ],
            options={
                'ordering': ['bebida'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pedido', models.CharField(blank=True, choices=[('1', 'CONVENIENCIA'), ('2', 'ALUGUEIS'), ('3', 'OUTROS')], max_length=2, null=True, verbose_name='Tipo de Pedido')),
                ('dt_abertura', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 102392), null=True, verbose_name='Data de abertura do pedido')),
                ('dt_fechamento', models.DateField(blank=True, null=True, verbose_name='Data fechamento do pedido')),
                ('dt_cancelamento', models.DateField(blank=True, null=True, verbose_name='Data cancelamento do pedido')),
                ('situacao', models.CharField(blank=True, choices=[('0', 'ABERTO'), ('1', 'FECHADO'), ('2', 'CANCELADO')], max_length=2, null=True, verbose_name='Situação do pedido')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Valor do pedido R$')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco_entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(blank=True, max_length=300, null=True, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=6, null=True, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=300, null=True, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=10, verbose_name='Cep')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='U F')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_entrega', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('primeiro_nome', models.CharField(max_length=20, verbose_name='Primeiro Nome')),
                ('sobre_nome', models.CharField(max_length=20, verbose_name='Sobre Nome')),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='C N P J')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='C P F')),
                ('dtNascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('estado_civil', models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, verbose_name='Estado civil')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('endereco', models.CharField(blank=True, max_length=300, null=True, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=6, null=True, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=300, null=True, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=10, verbose_name='Cep')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='U F')),
                ('telcelular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nº telefone celular')),
                ('telfixo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nº telefone fixo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nº Whatsapp')),
                ('facebook', models.CharField(blank=True, max_length=80, null=True, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=80, null=True, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, max_length=80, null=True, verbose_name='twitter')),
                ('dt_cadastro', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 98392), null=True, verbose_name='Data cadastro')),
                ('senha', models.CharField(max_length=25, verbose_name='Senha')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrinho_bebidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateField(blank=True, default=datetime.datetime(2020, 7, 6, 13, 7, 36, 103392), null=True, verbose_name='Data de inclusão no carrinho')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor unitario R$')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Quntidade de itens')),
                ('valor_total_item', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor Total R$')),
                ('situacao_carrinho', models.CharField(blank=True, choices=[('0', 'ABERTO'), ('1', 'FECHADO'), ('2', 'CANCELADO')], max_length=2, null=True, verbose_name='Situação do carrinho')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_bebidas', to='sitepedidos.Pedido', verbose_name='Pedido')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_bebidas', to='sitepedidos.Cad_prod_bebida', verbose_name='Produto')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_bebidas', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
