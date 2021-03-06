# Generated by Django 3.0.8 on 2021-09-19 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout.CarritoCompras')),
            ],
        ),
    ]
