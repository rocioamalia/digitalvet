# Generated by Django 4.0 on 2023-11-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_inventario_inventario_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosas',
            fields=[
                ('cosas_id', models.AutoField(primary_key=True, serialize=False)),
                ('cosas_cantidad', models.IntegerField()),
                ('cosas_nombre', models.CharField(max_length=50)),
                ('cosas_descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]
