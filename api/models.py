from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class DuenioMascota(models.Model):
    dm_rut = models.CharField(max_length=10, primary_key=True)
    dm_nombre = models.CharField(max_length=45)
    dm_apellido = models.CharField(max_length=45)
    dm_direccion = models.CharField(max_length=65)
    dm_telefono = models.IntegerField()
    dm_email = models.CharField(max_length=25)
    dm_contra = models.CharField(max_length=25)


class Medicamento(models.Model):
    med_id = models.AutoField(primary_key=True)
    med_fecha_vencimiento = models.DateField()
    med_fecha_ingreso = models.DateField()
    med_nombre = models.CharField(max_length=50)
    med_laboratorio = models.CharField(max_length=100)
    med_reaccion_adversa = models.CharField(max_length=100, null=True)
    med_via_administracion = models.CharField(max_length=20)
    med_indicaciones = models.CharField(max_length=100, null=True)
    med_motivo_administracion = models.CharField(max_length=100, null=True)
    med_n_serie = models.CharField(max_length=100, null=True)

class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    mascota_nombre = models.CharField(max_length=45)
    mascota_especie = models.CharField(max_length=10)
    mascota_raza = models.CharField(max_length=40)
    mascota_color = models.CharField(max_length=20)
    mascota_fecha_nacimiento = models.DateField()
    mascota_obtencion = models.CharField(max_length=20)
    mascota_sexo = models.CharField(max_length=6)
    mascota_estado_reproductivo = models.CharField(max_length=12)
    mascota_peso = models.FloatField(null=True)
    mascota_chip = models.CharField(max_length=10, null=True)
    mascota_razon_tenencia = models.CharField(max_length=15)
    mascota_enfermedades = models.CharField(max_length=45)
    #mascota_medicamentos_permanentes = models.ManyToManyField(Medicamento, related_name='macotas', blank=True)
    mascota_unica = models.BooleanField()
    mascota_duenio = models.ForeignKey(DuenioMascota, on_delete=models.CASCADE, related_name='macotas')
    mascota_image_url = models.TextField(null=True)
'''
class Imagen(models.Model):
    imagen_id = models.AutoField(primary_key=True)
    imagen_nombre = models.CharField(max_length=100)
    imagen_img_base64 = models.TextField()
    imagen_mascota = models.ForeignKey(Mascota, related_name='imagenes', on_delete=models.CASCADE)
'''
    
class Direccion(models.Model):
    direccion_id= models.AutoField(primary_key=True)
    direccion_latitude = models.FloatField(null=True)
    direccion_longitud = models.FloatField(null=True)
    direccion_calle = models.CharField(max_length=50 ,null=True)
    direccion_comuna = models.CharField(max_length=15 ,null=True)
    direccion_region = models.CharField(max_length=15 ,null=True)
    direccion_numero = models.CharField(max_length=10 ,null=True)
    direccion_casa = models.CharField(max_length=50,null=True)
   # direccion_nombre = models.CharField(max_length=50)


class Veterinaria(models.Model):
    veterinaria_id = models.AutoField(primary_key=True)
    veterinaria_nombre = models.CharField(max_length=45)
    veterinaria_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    veterinaria_apertura = models.TimeField()
    veterinaria_cierre = models.TimeField()
    veterinaria_emergencia = models.BooleanField()

class Veterinario(models.Model):
    vet_rut = models.CharField(max_length=10, primary_key=True)
    vet_nombre = models.CharField(max_length=45)
    vet_apellido = models.CharField(max_length=45)
    vet_email = models.CharField(max_length=25)
    vet_contra = models.CharField(max_length=25)
    vet_cargo = models.CharField(max_length=25)
    vet_n_celular = models.CharField(max_length=15)
    vet_fecha_nacimiento = models.DateField()
    vet_direcion = models.CharField(max_length=45)
    vet_foto = models.TextField(null=True)
    vet_admin = models.BooleanField() 

class Veterinario_Veterinaria(models.Model):
    vv_id = models.AutoField(primary_key=True)
    vv_fecha_inicio = models.DateField()
    vv_fecha_fin = models.DateField()
    vv_veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    vv_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)


class Box(models.Model):
    box_id = models.AutoField(primary_key=True)
    box_nombre = models.CharField(max_length=45)
    box_veterinaria = models.ForeignKey(Veterinaria, on_delete= models.CASCADE)

class Bloque (models.Model):
    bloque_id = models.AutoField(primary_key=True)
    bloque_hora_inicio = models.DateField()
    bloque_hora_fin = models.DateField()
    bloque_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)


class Dia (models.Model):
    dia_id = models.AutoField(primary_key=True)
    dia_nombre = models.CharField(max_length=45)

class Calendario (models.Model):
    cal_id = models.AutoField(primary_key=True)
    cal_fecha = models.DateField()
    cal_feriado = models.BooleanField()
    cal_cerrado = models.BooleanField()

class Reserva (models.Model):
    reserva_id = models.AutoField(primary_key=True)
    reserva_fecha = models.DateField()
    reserva_cancelada = models.BooleanField()
    reserva_mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
#    reserva_vv= models.ForeignKey(Veterinario_Veterinaria, on_delete= models)
    #añadir veterinario veterinaria
class Vvbd (models.Model):
    vvbd_id = models.AutoField(primary_key=True)
#aki#

class ExamenFisico(models.Model):
    exa_estado_animal = models.AutoField(primary_key=True)
    exa_peso = models.IntegerField()
    exa_oxigenacion_sangre = models.IntegerField(null=True)
    exa_frecuencia_cardiaca = models.IntegerField(null=True)
    exa_frecuencia_respiratoria = models.IntegerField(null=True)
    exa_temperatura_corporal = models.FloatField(null=True)
    exa_llene_capilar = models.IntegerField()
    exa_observaciones = models.CharField(max_length=50)
    exa_mucosas = models.CharField(max_length=50)
    exa_dieta = models.CharField(max_length=50)
    exa_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

class Consulta(models.Model):
    consulta_id = models.AutoField(primary_key=True)
    consulta_tipo = models.CharField(max_length=10)
    consulta_motivo = models.CharField(max_length=50)
    consulta_inicio = models.TimeField()
    consulta_termino = models.TimeField()
    consulta_fecha = models.DateField()
    consulta_precio = models.IntegerField(null=True)
    consulta_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    consulta_diagnostico_observaciones = models.CharField(max_length=200)
    consulta_diagnostico_diagnostico = models.CharField(max_length=50)
    #a
    consulta_box = models.ForeignKey(Box, on_delete=models.CASCADE)
    consulta_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    consulta_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    consulta_vvbd = models.ForeignKey(Vvbd, on_delete=models.CASCADE)
    consulta_diagnostico_examenes = models.ForeignKey(ExamenFisico, on_delete=models.CASCADE)

class Tratamiento(models.Model):
    tratamiento_id = models.AutoField(primary_key=True)
    tratamiento_observaciones = models.CharField(max_length=200)
    tratamiento_indicaciones = models.CharField(max_length=150)
    tratamiento_seguimiento = models.CharField(max_length=100)
    tratamiento_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    tratamiento_dosis = models.FloatField()
    tratamiento_fecha_emision = models.DateField()
    tratamiento_fecha_administracion = models.DateField()

class Fallecimiento(models.Model):
    fallecimiento_id = models.AutoField(primary_key=True)
    fallecimiento_fecha = models.DateTimeField()
    fallecimiento_momento = models.CharField(max_length=50)
    fallecimiento_causa = models.CharField(max_length=100)
    fallecimiento_tipo = models.CharField(max_length=100)
    fallecimiento_observaciones = models.CharField(max_length=200)
    fallecimiento_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fallecimiento_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)
    fallecimiento_vet_rut = models.ForeignKey(Veterinario, on_delete=models.CASCADE)


class Procedimiento(models.Model):
    procedimiento_id = models.AutoField(primary_key=True)
    procedimiento_operacion = models.CharField(max_length=200)
    procedimiento_oxigenacion_sangre = models.IntegerField(null=True)
    procedimiento_frecuencia_cardiaca = models.IntegerField(null=True)
    procedimiento_frecuencia_respiratoria = models.IntegerField(null=True)
    procedimiento_temperatura_corporal = models.FloatField(null=True)
    procedimiento_estado_final = models.CharField(max_length=50)
    procedimiento_observaciones = models.CharField(max_length=100)
    procedimiento_medicamentos_utilizados = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    procedimiento_estado_fatal = models.ForeignKey(Fallecimiento, on_delete=models.CASCADE, null=True)
    procedimiento_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)


class Desparasitacion(models.Model):
    despa_id = models.AutoField(primary_key=True)
    despa_fecha = models.DateField()
    despa_precio = models.IntegerField()
    despa_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)
    despa_vet_rut = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    despa_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

class Insumo(models.Model):
    insumo_id= models.AutoField(primary_key=True)
    insumo_nombre =  models.CharField(max_length=50)
    insumo_descripcion =  models.CharField(max_length=50)

class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    inventario_cantidad = models.IntegerField()
    inventario_nombre =  models.CharField(max_length=50)
    inventario_descripcion = models.CharField(max_length=50)
    #inventario_medicamento =  models.BooleanField()
    #inventario_item = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=True)
    #inventario_item = GenericForeignKey('inventario_content_type', 'inventario_id')
    inventario_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)
    

class Deudor(models.Model):
    deudor_id = models.AutoField(primary_key=True)
    deudor_duenio = models.ForeignKey(DuenioMascota, on_delete=models.CASCADE)
    deudor_monto = models.IntegerField()
    deudor_razon =  models.CharField(max_length=50)
    deudor_veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)

class Receta(models.Model):
    receta_id = models.AutoField(primary_key=True)
    receta_dosis = models.FloatField()
    receta_indicaciones = models.CharField(max_length=100)
    receta_Medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    receta_veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    receta_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

class Cosas(models.Model):
    cosas_id = models.AutoField(primary_key=True)
    cosas_cantidad = models.IntegerField()
    cosas_nombre =  models.CharField(max_length=50)
    cosas_descripcion = models.CharField(max_length=50)