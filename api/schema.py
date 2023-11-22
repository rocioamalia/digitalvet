from datetime import date, time
from ninja import Schema

class DuenioMascotaSchema(Schema):
    dm_rut: str
    dm_nombre: str
    dm_apellido: str
    dm_direccion: str
    dm_telefono: int
    dm_email: str
    dm_contra: str


class MedicamentoSchema(Schema):
    med_id: int
    med_fecha_vencimiento: date
    med_fecha_ingreso: date
    med_nombre: str
    med_laboratorio: str
    med_reaccion_adversa: str
    med_via_administracion: str
    med_indicaciones: str
    med_motivo_administracion: str
    med_n_serie: str

class MascotaSchema(Schema):
    mascota_id : int
    mascota_nombre: str
    mascota_especie: str
    mascota_raza: str
    mascota_color: str
    mascota_fecha_nacimiento: date
    mascota_obtencion: str
    mascota_sexo: str
    mascota_estado_reproductivo: str
    mascota_peso: float
    mascota_chip: str = None 
    mascota_razon_tenencia: str
    mascota_enfermedades: str = None
    #mascota_medicamentos_permanentes: list 
    mascota_unica: bool
    mascota_duenio: DuenioMascotaSchema 
    mascota_image_url : str = None

class DireccionSchema(Schema):
    direccion_id: int
    direccion_latitude : float = None
    direccion_longitud : float = None
    direccion_calle : str = None
    direccion_comuna : str = None
    direccion_region : str = None
    direccion_numero : str = None
    direccion_casa : str = None
'''
class ImagenSchema(Schema):
    imagen_id: int
    imagen_nombre: str
    imagen_img_base64: str
    imagen_mascota: MascotaSchema
'''

class VeterinariaSchema(Schema):
    veterinaria_id: int
    veterinaria_nombre: str
    veterinaria_direccion: DireccionSchema
    veterinaria_apertura: time
    veterinaria_cierre: time
    veterinaria_emergencia: bool

class VeterinarioSchema(Schema):
    vet_rut: str
    vet_nombre: str
    vet_apellido: str
    vet_email: str
    vet_contra: str
    vet_cargo : str
    vet_n_celular : str
    vet_fecha_nacimiento : date
    vet_direcion : str
    vet_foto :str = None
    vet_admin: bool

class BoxSchema(Schema):
    box_id : int
    box_nombre: str
    box_veterinaria: VeterinariaSchema
    
class VeterinarioVeterinariaSchema(Schema):
    vv_id : int
    vv_fecha_inicio : date
    vv_fecha_fin : date = None 
    vv_veterinario : VeterinarioSchema
    vv_veterinaria : VeterinariaSchema
    vv_veterinaria : VeterinariaSchema

class BloqueSchema(Schema):
    bloque_id: int
    bloque_hora_inicio : date
    bloque_hora_fin : date
    bloque_veterinaria: VeterinariaSchema

class DiaSchema(Schema):
    dia_id : int
    dia_nombr : str

class CalendarioSchema(Schema):
    cal_id : int
    cal_fecha : date
    cal_feriado : bool
    cal_cerrado : bool

class ReservaSchema(Schema):
    reserva_id : int
    reserva_fecha : date
    reserva_cancelada : bool
    reserva_mascota : MascotaSchema

class VvbdSchema(Schema):
    vvbd_id : int

class ExamenFisicoSchema(Schema):
    exa_estado_animal: int
    exa_peso: int
    exa_oxigenacion_sangre: int
    exa_frecuencia_cardiaca: int
    exa_frecuencia_respiratoria: int
    exa_temperatura_corporal: float
    exa_llene_capilar: int
    exa_observaciones: str
    exa_mucosas: str
    exa_dieta: str
    exa_mascota: MascotaSchema

class ConsultaSchema(Schema):
    consulta_id: int
    consulta_tipo: str
    consulta_motivo: str
    consulta_inicio: str
    consulta_termino: str
    consulta_fecha: str
    consulta_precio: int
    consulta_mascota: MascotaSchema
    consulta_diagnostico_observaciones: str
    consulta_diagnostico_diagnostico: str
    consulta_diagnostico_examenes: ExamenFisicoSchema
    consulta_box : BoxSchema
    consulta_reserva: ReservaSchema
    consulta_calendario : CalendarioSchema
    consulta_vvbd : VvbdSchema

class TratamientoSchema(Schema):
    tratamiento_id: int
    tratamiento_observaciones: str
    tratamiento_indicaciones: str
    tratamiento_seguimiento: str
    tratamiento_medicamento: MedicamentoSchema
    tratamiento_dosis: float
    tratamiento_fecha_emision: str
    tratamiento_fecha_administracion: str


class FallecimientoSchema(Schema):
    fallecimiento_id: int
    fallecimiento_fecha: str
    fallecimiento_momento: str
    fallecimiento_causa: str
    fallecimiento_tipo: str
    fallecimiento_observaciones: str
    fallecimiento_mascota: MascotaSchema
    fallecimiento_veterinaria: VeterinariaSchema
    fallecimiento_vet_rut: VeterinarioSchema


class ProcedimientoSchema(Schema):
    procedimiento_id: int
    procedimiento_operacion: str
    procedimiento_oxigenacion_sangre: int
    procedimiento_frecuencia_cardiaca: int
    procedimiento_frecuencia_respiratoria: int
    procedimiento_temperatura_corporal: float
    procedimiento_estado_final: str
    procedimiento_observaciones: str
    procedimiento_medicamentos_utilizados: MedicamentoSchema
    procedimiento_estado_fatal: FallecimientoSchema
    procedimiento_mascota: MascotaSchema


class DesparasitacionSchema(Schema):
    despa_id: int
    despa_fecha: str
    despa_precio: int
    despa_veterinaria: VeterinariaSchema
    despa_vet_rut: VeterinarioSchema
    despa_mascota: MascotaSchema
'''
class InsumoSchema(Schema):
    insumo_id: int
    insumo_nombre : str
    insumo_descripcion : str = None
'''

class InventarioSchema(Schema):
    inventario_id : int
    inventario_cantidad : int
    inventario_nombre :str
    inventario_descripcion :str
    inventario_veterinaria : VeterinariaSchema

class DeudorSchema(Schema):
    deudor_id : int
    deudor_duenio : DuenioMascotaSchema
    deudor_monto : int
    deudor_razon : str = None
    deudor_veterinaria : VeterinariaSchema

class RecetaSchema(Schema):
    receta_id : int
    receta_dosis : float
    receta_indicaciones : str
    receta_Medicamento : MedicamentoSchema
    receta_veterinario : VeterinarioSchema
    receta_mascota : MascotaSchema

class CosasSchema(Schema):
    cosas_id : int
    cosas_cantidad : int
    cosas_nombre: str
    cosas_descripcion: str