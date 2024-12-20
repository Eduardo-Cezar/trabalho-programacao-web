# Generated by Django 5.1.4 on 2024-12-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pratos',
            name='ingredientes',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='pratos',
            name='nome',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('analise', 'Em Análise'), ('aceito', 'Aceito'), ('fazendo', 'Fazendo'), ('caminho', 'A Caminho'), ('entregue', 'Entregue')], default='analise', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('prato', models.ManyToManyField(related_name='pedidos', to='myapp.pratos')),
            ],
        ),
    ]
