# Generated by Django 4.0 on 2023-11-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='inventario_content_type',
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_descripcion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.medicamento'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_medicamento',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='inventario_nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]