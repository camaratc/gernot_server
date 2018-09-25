# Generated by Django 2.1.1 on 2018-09-25 17:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Título')),
                ('message', models.TextField(max_length=2000, verbose_name='Mensagem')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('tag', models.IntegerField(choices=[(0, 'Erro'), (1, 'Aviso'), (2, 'Recomendação')], verbose_name='Categoria')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2018, 9, 25, 17, 2, 2, 226868, tzinfo=utc), editable=False, verbose_name='Data de Criação')),
                ('send_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de Envio')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
    ]
