# Generated by Django 5.0.7 on 2024-07-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProductos', models.IntegerField()),
                ('descripcionProductos', models.CharField(max_length=255)),
                ('estatus', models.BooleanField()),
            ],
        ),
    ]
