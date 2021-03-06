# Generated by Django 3.0.6 on 2020-07-08 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepedidos', '0005_auto_20200708_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_prod_aluguel',
            name='dt_final',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 339003), null=True, verbose_name='Data final da apresentação'),
        ),
        migrations.AlterField(
            model_name='cad_prod_aluguel',
            name='dt_inicio',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 339003), null=True, verbose_name='Data inicio da apresentação'),
        ),
        migrations.AlterField(
            model_name='cad_prod_bebida',
            name='dt_final',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 338003), null=True, verbose_name='Data final da apresentação'),
        ),
        migrations.AlterField(
            model_name='cad_prod_bebida',
            name='dt_inicio',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 338003), null=True, verbose_name='Data inicio da apresentação'),
        ),
        migrations.AlterField(
            model_name='cad_prod_bebida',
            name='url_imagem',
            field=models.CharField(blank=True, help_text='Digite a url de endereço da imagem', max_length=600, null=True, verbose_name='URL da Imagem do Produto'),
        ),
        migrations.AlterField(
            model_name='carrinho_bebidas',
            name='dt_inclusao',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 341002), null=True, verbose_name='Data de inclusão no carrinho'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dt_cadastro',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 336003), null=True, verbose_name='Data cadastro'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='dt_abertura',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 8, 20, 48, 13, 340002), null=True, verbose_name='Data de abertura do pedido'),
        ),
    ]
