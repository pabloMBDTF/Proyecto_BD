# Generated by Django 5.0.2 on 2024-05-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers_remove_cliente_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombreSucursal',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefonoSucursal',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
