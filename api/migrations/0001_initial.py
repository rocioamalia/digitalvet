# Generated by Django 4.0 on 2023-11-13 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('box_id', models.AutoField(primary_key=True, serialize=False)),
                ('box_nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('cal_id', models.AutoField(primary_key=True, serialize=False)),
                ('cal_fecha', models.DateField()),
                ('cal_feriado', models.BooleanField()),
                ('cal_cerrado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('dia_id', models.AutoField(primary_key=True, serialize=False)),
                ('dia_nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_latitude', models.FloatField(null=True)),
                ('direccion_longitud', models.FloatField(null=True)),
                ('direccion_calle', models.CharField(max_length=50, null=True)),
                ('direccion_comuna', models.CharField(max_length=15, null=True)),
                ('direccion_region', models.CharField(max_length=15, null=True)),
                ('direccion_numero', models.CharField(max_length=10, null=True)),
                ('direccion_casa', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DuenioMascota',
            fields=[
                ('dm_rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dm_nombre', models.CharField(max_length=45)),
                ('dm_apellido', models.CharField(max_length=45)),
                ('dm_direccion', models.CharField(max_length=65)),
                ('dm_telefono', models.IntegerField()),
                ('dm_email', models.CharField(max_length=25)),
                ('dm_contra', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Fallecimiento',
            fields=[
                ('fallecimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('fallecimiento_fecha', models.DateTimeField()),
                ('fallecimiento_momento', models.CharField(max_length=50)),
                ('fallecimiento_causa', models.CharField(max_length=100)),
                ('fallecimiento_tipo', models.CharField(max_length=100)),
                ('fallecimiento_observaciones', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('insumo_id', models.AutoField(primary_key=True, serialize=False)),
                ('insumo_nombre', models.CharField(max_length=50)),
                ('insumo_descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('mascota_nombre', models.CharField(max_length=45)),
                ('mascota_especie', models.CharField(max_length=10)),
                ('mascota_raza', models.CharField(max_length=40)),
                ('mascota_color', models.CharField(max_length=20)),
                ('mascota_fecha_nacimiento', models.DateField()),
                ('mascota_obtencion', models.CharField(max_length=20)),
                ('mascota_sexo', models.CharField(max_length=6)),
                ('mascota_estado_reproductivo', models.CharField(max_length=12)),
                ('mascota_peso', models.FloatField(null=True)),
                ('mascota_chip', models.CharField(max_length=10, null=True)),
                ('mascota_razon_tenencia', models.CharField(max_length=15)),
                ('mascota_enfermedades', models.CharField(max_length=45)),
                ('mascota_unica', models.BooleanField()),
                ('mascota_image_url', models.TextField(null=True)),
                ('mascota_duenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='macotas', to='api.dueniomascota')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('med_id', models.AutoField(primary_key=True, serialize=False)),
                ('med_fecha_vencimiento', models.DateField()),
                ('med_fecha_ingreso', models.DateField()),
                ('med_nombre', models.CharField(max_length=50)),
                ('med_laboratorio', models.CharField(max_length=100)),
                ('med_reaccion_adversa', models.CharField(max_length=100, null=True)),
                ('med_via_administracion', models.CharField(max_length=20)),
                ('med_indicaciones', models.CharField(max_length=100, null=True)),
                ('med_motivo_administracion', models.CharField(max_length=100, null=True)),
                ('med_n_serie', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('veterinaria_id', models.AutoField(primary_key=True, serialize=False)),
                ('veterinaria_nombre', models.CharField(max_length=45)),
                ('veterinaria_apertura', models.TimeField()),
                ('veterinaria_cierre', models.TimeField()),
                ('veterinaria_emergencia', models.BooleanField()),
                ('veterinaria_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('vet_rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('vet_nombre', models.CharField(max_length=45)),
                ('vet_apellido', models.CharField(max_length=45)),
                ('vet_email', models.CharField(max_length=25)),
                ('vet_contra', models.CharField(max_length=25)),
                ('vet_cargo', models.CharField(max_length=25)),
                ('vet_n_celular', models.CharField(max_length=15)),
                ('vet_fecha_nacimiento', models.DateField()),
                ('vet_direcion', models.CharField(max_length=45)),
                ('vet_foto', models.TextField(null=True)),
                ('vet_admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vvbd',
            fields=[
                ('vvbd_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario_Veterinaria',
            fields=[
                ('vv_id', models.AutoField(primary_key=True, serialize=False)),
                ('vv_fecha_inicio', models.DateField()),
                ('vv_fecha_fin', models.DateField()),
                ('vv_veterinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria')),
                ('vv_veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinario')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('tratamiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('tratamiento_observaciones', models.CharField(max_length=200)),
                ('tratamiento_indicaciones', models.CharField(max_length=150)),
                ('tratamiento_seguimiento', models.CharField(max_length=100)),
                ('tratamiento_dosis', models.FloatField()),
                ('tratamiento_fecha_emision', models.DateField()),
                ('tratamiento_fecha_administracion', models.DateField()),
                ('tratamiento_medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reserva_id', models.AutoField(primary_key=True, serialize=False)),
                ('reserva_fecha', models.DateField()),
                ('reserva_cancelada', models.BooleanField()),
                ('reserva_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('receta_id', models.AutoField(primary_key=True, serialize=False)),
                ('receta_dosis', models.FloatField()),
                ('receta_indicaciones', models.CharField(max_length=100)),
                ('receta_Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.medicamento')),
                ('receta_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
                ('receta_veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinario')),
            ],
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('procedimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('procedimiento_operacion', models.CharField(max_length=200)),
                ('procedimiento_oxigenacion_sangre', models.IntegerField(null=True)),
                ('procedimiento_frecuencia_cardiaca', models.IntegerField(null=True)),
                ('procedimiento_frecuencia_respiratoria', models.IntegerField(null=True)),
                ('procedimiento_temperatura_corporal', models.FloatField(null=True)),
                ('procedimiento_estado_final', models.CharField(max_length=50)),
                ('procedimiento_observaciones', models.CharField(max_length=100)),
                ('procedimiento_estado_fatal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.fallecimiento')),
                ('procedimiento_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
                ('procedimiento_medicamentos_utilizados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('inventario_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventario_cantidad', models.IntegerField()),
                ('inventario_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('inventario_veterinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria')),
            ],
        ),
        migrations.AddField(
            model_name='fallecimiento',
            name='fallecimiento_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota'),
        ),
        migrations.AddField(
            model_name='fallecimiento',
            name='fallecimiento_vet_rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinario'),
        ),
        migrations.AddField(
            model_name='fallecimiento',
            name='fallecimiento_veterinaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria'),
        ),
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('exa_estado_animal', models.AutoField(primary_key=True, serialize=False)),
                ('exa_peso', models.IntegerField()),
                ('exa_oxigenacion_sangre', models.IntegerField(null=True)),
                ('exa_frecuencia_cardiaca', models.IntegerField(null=True)),
                ('exa_frecuencia_respiratoria', models.IntegerField(null=True)),
                ('exa_temperatura_corporal', models.FloatField(null=True)),
                ('exa_llene_capilar', models.IntegerField()),
                ('exa_observaciones', models.CharField(max_length=50)),
                ('exa_mucosas', models.CharField(max_length=50)),
                ('exa_dieta', models.CharField(max_length=50)),
                ('exa_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Deudor',
            fields=[
                ('deudor_id', models.AutoField(primary_key=True, serialize=False)),
                ('deudor_monto', models.IntegerField()),
                ('deudor_razon', models.CharField(max_length=50)),
                ('deudor_duenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dueniomascota')),
                ('deudor_veterinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Desparasitacion',
            fields=[
                ('despa_id', models.AutoField(primary_key=True, serialize=False)),
                ('despa_fecha', models.DateField()),
                ('despa_precio', models.IntegerField()),
                ('despa_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
                ('despa_vet_rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinario')),
                ('despa_veterinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('consulta_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulta_tipo', models.CharField(max_length=10)),
                ('consulta_motivo', models.CharField(max_length=50)),
                ('consulta_inicio', models.TimeField()),
                ('consulta_termino', models.TimeField()),
                ('consulta_fecha', models.DateField()),
                ('consulta_precio', models.IntegerField(null=True)),
                ('consulta_diagnostico_observaciones', models.CharField(max_length=200)),
                ('consulta_diagnostico_diagnostico', models.CharField(max_length=50)),
                ('consulta_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.box')),
                ('consulta_calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.calendario')),
                ('consulta_diagnostico_examenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.examenfisico')),
                ('consulta_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mascota')),
                ('consulta_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reserva')),
                ('consulta_vvbd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vvbd')),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='box_veterinaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria'),
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('bloque_id', models.AutoField(primary_key=True, serialize=False)),
                ('bloque_hora_inicio', models.DateField()),
                ('bloque_hora_fin', models.DateField()),
                ('bloque_veterinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.veterinaria')),
            ],
        ),
    ]
