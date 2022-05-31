# Generated by Django 4.0.4 on 2022-05-31 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='IdCategorias')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='NombreCategorias')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre')),
                ('precio', models.CharField(max_length=20, verbose_name='Precio')),
                ('caracteristicas', models.CharField(blank=True, max_length=20, null=True, verbose_name='Caracteristicas')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
