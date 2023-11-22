from django.http import JsonResponse
from ninja import NinjaAPI
from api.models import DuenioMascota, Medicamento, Mascota, Veterinaria, Veterinario, Veterinario_Veterinaria, Box, Bloque, Dia, Calendario, Reserva, Vvbd, Consulta, ExamenFisico, Tratamiento, Fallecimiento, Procedimiento, Desparasitacion, Veterinario_Veterinaria, Box, Bloque, Dia, Calendario, Vvbd, Insumo, Inventario, Deudor, Receta ,Direccion, Cosas
from api.schema import DuenioMascotaSchema, MedicamentoSchema, MascotaSchema, VeterinariaSchema, VeterinarioSchema, VeterinarioVeterinariaSchema, BoxSchema , BloqueSchema, DiaSchema, CalendarioSchema, ReservaSchema, VvbdSchema, ConsultaSchema, ExamenFisicoSchema, TratamientoSchema, FallecimientoSchema, ProcedimientoSchema, DesparasitacionSchema, VeterinarioVeterinariaSchema, BloqueSchema, DiaSchema, CalendarioSchema, VvbdSchema, InventarioSchema, DeudorSchema, RecetaSchema, DireccionSchema, CosasSchema
from django.http import JsonResponse

api=NinjaAPI()

@api.get("/test")
def test(request):
    return {'test':'success'}


@api.get("/duenios_mascota")
def listar_duenios_mascota(request):
    duenios_mascota = DuenioMascota.objects.all()
    return [DuenioMascotaSchema.from_orm(duenio) for duenio in duenios_mascota]

@api.post("/duenios_mascota")
def crear_duenio_mascota(request, duenio: DuenioMascotaSchema):
    nuevo_duenio = DuenioMascota.objects.create(**duenio.dict())
    return DuenioMascotaSchema.from_orm(nuevo_duenio)

@api.get("/duenios_mascota/{dm_rut}")
def obtener_duenio_mascota(request, dm_rut: str):
    duenio_mascota = DuenioMascota.objects.get(dm_rut=dm_rut)
    return DuenioMascotaSchema.from_orm(duenio_mascota)


@api.put("/duenios_mascota/{dm_rut}")
def actualizar_duenio_mascota(request, dm_rut: str, duenio: DuenioMascotaSchema):
    duenio_mascota = DuenioMascota.objects.get(dm_rut=dm_rut)
    duenio_mascota.dm_nombre = duenio.dm_nombre
    duenio_mascota.dm_apellido = duenio.dm_apellido
    duenio_mascota.dm_direccion = duenio.dm_direccion
    duenio_mascota.dm_telefono = duenio.dm_telefono
    duenio_mascota.dm_email = duenio.dm_email
    duenio_mascota.dm_contra = duenio.dm_contra
    duenio_mascota.save()
    return DuenioMascotaSchema.from_orm(duenio_mascota)

@api.get("/medicamentos")
def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return [MedicamentoSchema.from_orm(medicamento) for medicamento in medicamentos]

@api.post("/medicamentos")
def crear_medicamento(request, medicamento: MedicamentoSchema):
    nuevo_medicamento = Medicamento.objects.create(**medicamento.dict())
    return MedicamentoSchema.from_orm(nuevo_medicamento)

@api.get("/medicamentos/{med_id}")
def obtener_medicamento(request, med_id: int):
    medicamento = Medicamento.objects.get(med_id=med_id)
    return MedicamentoSchema.from_orm(medicamento)

@api.put("/medicamentos/{med_id}")
def actualizar_medicamento(request, med_id: int, medicamento: MedicamentoSchema):
    med = Medicamento.objects.get(med_id=med_id)
    med.med_fecha_vencimiento = medicamento["med_fecha_vencimiento"]
    med.med_fecha_ingreso = medicamento["med_fecha_ingreso"]
    med.med_nombre = medicamento["med_nombre"]
    med.med_laboratorio = medicamento["med_laboratorio"]
    med.med_reaccion_adversa = medicamento["med_reaccion_adversa"]
    med.med_via_administracion = medicamento["med_via_administracion"]
    med.med_indicaciones = medicamento["med_indicaciones"]
    med.med_motivo_administracion = medicamento["med_motivo_administracion"]
    med.med_n_serie = medicamento["med_n_serie"]
    med.save()
    return MedicamentoSchema.from_orm(med)

@api.get("/mascotas")
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return [MascotaSchema.from_orm(mascota) for mascota in mascotas]

@api.post("/mascotas")
def crear_mascotas(request, mascota: MascotaSchema):
    #duenio=obtener_duenio_mascota(request,mascota.mascota_duenio.dm_rut)
    #mascota.mascota_duenio=duenio
    #nueva_mascota = Mascota.objects.create(**mascota.dict())
    # Crear instancia de DuenioMascota
    duenio_existente = DuenioMascota.objects.get(dm_rut=mascota.mascota_duenio.dm_rut)
    # Crear instancia de Mascota y asignar el dueño
    nueva_mascota = Mascota.objects.create(
        mascota_nombre=mascota.mascota_nombre,
        mascota_especie=mascota.mascota_especie,
        mascota_raza=mascota.mascota_raza,
        mascota_color=mascota.mascota_color,
        mascota_fecha_nacimiento=mascota.mascota_fecha_nacimiento,
        mascota_obtencion=mascota.mascota_obtencion,
        mascota_sexo=mascota.mascota_sexo,
        mascota_estado_reproductivo=mascota.mascota_estado_reproductivo,
        mascota_peso=mascota.mascota_peso,
        mascota_chip=mascota.mascota_chip,
        mascota_razon_tenencia=mascota.mascota_razon_tenencia,
        #mascota_enfermedades = mascota.mascota_enfermedades,
        mascota_unica=mascota.mascota_unica,
        mascota_duenio=duenio_existente
    )
    #crear instancia de medicamento si es necesario
    #for med in mascota.mascota_medicamentos_permanentes:
        #medicamento = Medicamento.objects.get(med_id=med)  # Ajusta según tu esquema
        #nueva_mascota.mascota_medicamentos_permanentes.add(medicamento)
    return MascotaSchema.from_orm(nueva_mascota)

@api.get("/mascotas/{mascota_id}")
def obtener_mascotas(request, mascota_id: int):
    mascotas = Mascota.objects.get(mascota_id=mascota_id)
    return MascotaSchema.from_orm(mascotas)

@api.put("/mascotas/{mascota_id}")
def actualizar_mascota(request, mascota_id: int, mascota: MascotaSchema):
    mascota_obj = Mascota.objects.get(mascota_id=mascota_id)
    mascota_obj.mascota_nombre = mascota["mascota_nombre"]
    mascota_obj.mascota_especie = mascota["mascota_especie"]
    mascota_obj.mascota_raza = mascota["mascota_raza"]
    mascota_obj.mascota_color = mascota["mascota_color"]
    mascota_obj.mascota_fecha_nacimiento = mascota["mascota_fecha_nacimiento"]
    mascota_obj.mascota_obtencion = mascota["mascota_obtencion"]
    mascota_obj.mascota_sexo = mascota["mascota_sexo"]
    mascota_obj.mascota_estado_reproductivo = mascota["mascota_estado_reproductivo"]
    mascota_obj.mascota_peso = mascota["mascota_peso"]
    mascota_obj.mascota_chip = mascota["mascota_chip"]
    mascota_obj.mascota_razon_tenencia = mascota["mascota_razon_tenencia"]
    mascota_obj.mascota_enfermedades = mascota["mascota_enfermedades"]
    mascota_obj.mascota_medicamentos_permanentes = mascota["mascota_medicamentos_permanentes"]
    mascota_obj.mascota_unica = mascota["mascota_unica"]
    mascota_obj.mascota_duenio = mascota["mascota_duenio"]
    mascota_obj.save()
    return MascotaSchema.from_orm(mascota_obj)

@api.get("/veterinarias")
def listar_veterinarias(request):
    veterinarias = Veterinaria.objects.all()
    return [VeterinariaSchema.from_orm(veterinaria) for veterinaria in veterinarias]

@api.post("/veterinarias")
def crear_veterinarias(request, veterinaria: VeterinariaSchema):
    nueva_vete = Veterinaria.objects.create(**veterinaria.dict())
    return VeterinariaSchema.from_orm(nueva_vete)

@api.get("/veterinarias/{veterinaria_id}")
def obtener_veterinarias(request, veterinaria_id: int):
    veterinaria = Veterinaria.objects.get(veterinaria_id=veterinaria_id)
    return VeterinariaSchema.from_orm(veterinaria)

@api.put("/veterinarias/{veterinaria_id}")
def actualizar_veterinaria(request, veterinaria_id: int, veterinaria: VeterinariaSchema):
    vet = Veterinaria.objects.get(veterinaria_id=veterinaria_id)
    vet.veterinaria_nombre = veterinaria["veterinaria_nombre"]
    vet.veterinaria_direccion = veterinaria["veterinaria_direccion"]
    vet.veterinaria_apertura = veterinaria["veterinaria_apertura"]
    vet.veterinaria_cierre = veterinaria["veterinaria_cierre"]
    vet.veterinaria_emergencia = veterinaria["veterinaria_emergencia"]
    vet.save()
    return VeterinariaSchema.from_orm(vet)

@api.get("/veterinarios")
def listar_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return [VeterinarioSchema.from_orm(veterinario) for veterinario in veterinarios]

@api.post("/veterinarios")
def crear_veterinarios(request, veterinario: VeterinarioSchema):
    nuevo_vete = Veterinario.objects.create(**veterinario.dict())
    return VeterinarioSchema.from_orm(nuevo_vete)

@api.get("/veterinarios/{vet_rut}")
def obtener_veterinarios(request, vet_rut: str):
    veterinario = Veterinario.objects.get(vet_rut=vet_rut)
    return VeterinarioSchema.from_orm(veterinario)

@api.put("/veterinarios/{vet_rut}")
def actualizar_veterinario(request, vet_rut: str, veterinario: VeterinarioSchema):
    vet = Veterinario.objects.get(vet_rut=vet_rut)
    vet.vet_nombre = veterinario["vet_nombre"]
    vet.vet_apellido = veterinario["vet_apellido"]
    vet.vet_email = veterinario["vet_email"]
    vet.vet_contra = veterinario["vet_contra"]
    vet.vet_cargo = veterinario["vet_cargo"]
    vet.vet_admin = veterinario["vet_admin"]
    vet.save()
    return VeterinarioSchema.from_orm(vet)

@api.get("/consultas")
def listar_consultas(request):
    consultas = Consulta.objects.all()
    return [ConsultaSchema.from_orm(consulta) for consulta in consultas]

@api.post("/consultas")
def crear_consultas(request, consulta: ConsultaSchema):
    nueva_consulta = Consulta.objects.create(**consulta.dict())
    return ConsultaSchema.from_orm(nueva_consulta)

@api.get("/consultas/{consulta_id}")
def obtener_consultas(request, consulta_id: int):
    consulta = Consulta.objects.get(consulta_id=consulta_id)
    return ConsultaSchema.from_orm(consulta)
'''
@api.put("/consultas/{consulta_id}")
def actualizar_consulta(request, consulta_id: int, consulta: ConsultaSchema):
    consulta_obj = Consulta.objects.get(consulta_id=consulta_id)
    consulta_obj.consulta_tipo = consulta.consulta_tipo
    consulta_obj.consulta_motivo = consulta.consulta_motivo
    consulta_obj.consulta_inicio = consulta.consulta_inicio
    consulta_obj.consulta_termino = consulta.consulta_termino
    consulta_obj.consulta_fecha = consulta.consulta_fecha
    consulta_obj.consulta_precio = consulta.consulta_precio
    consulta_obj.consulta_mascota_id = consulta.consulta_mascota_id
    consulta_obj.consulta_vetrinaria_id = consulta.consulta_vetrinaria_id
    consulta_obj.consulta_vet_rut = consulta.consulta_vet_rut
    consulta_obj.save()
    return ConsultaSchema.from_orm(consulta_obj)
'''

#desde aqui faltan los modificar

@api.get("/examenesfisicos")
def listar_examenesfisicos(request):
    examenesfisicos = ExamenFisico.objects.all()
    return [ExamenFisicoSchema.from_orm(examenesfisico) for examenesfisico in examenesfisicos]

@api.post("/examenesfisicos")
def crear_examenesfisicos(request, Examen: ExamenFisicoSchema):
    nuevo_examen = ExamenFisico.objects.create(**Examen.dict())
    return ExamenFisicoSchema.from_orm(nuevo_examen)

@api.get("/examenesfisicos/{exa_mascota}")
def obtener_examenesfisicos(request, exa_mascota: int):
    exa_fisico = ExamenFisico.objects.get(exa_mascota=exa_mascota)
    return ExamenFisicoSchema.from_orm(exa_fisico)

@api.get("/tratamientos")
def listar_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return [TratamientoSchema.from_orm(tratamiento) for tratamiento in tratamientos]

@api.post("/tratamientos")
def crear_tratamientos(request, tratamiento: TratamientoSchema):
    nuevo_tratamiento = Tratamiento.objects.create(**tratamiento.dict())
    return TratamientoSchema.from_orm(nuevo_tratamiento)

@api.get("/tratamientos/{tratamiento_id}")
def obtener_tratamientos(request, tratamiento_id: int):
    tratamiento = Tratamiento.objects.get(tratamiento_id=tratamiento_id)
    return TratamientoSchema.from_orm(tratamiento)

@api.get("/fallecimientos")
def listar_fallecimientos(request):
    fallecimientos = Fallecimiento.objects.all()
    return [FallecimientoSchema.from_orm(fallecimiento) for fallecimiento in fallecimientos]

@api.post("/fallecimientos")
def crear_fallecimiento(request, tratamiento: FallecimientoSchema):
    nuevo_fallecimiento = Fallecimiento.objects.create(**tratamiento.dict())
    return FallecimientoSchema.from_orm(nuevo_fallecimiento)

@api.get("/fallecimientos/{fallecimiento_id}")
def obtener_fallecimiento(request, fallecimiento_id: int):
    fallecimiento = Fallecimiento.objects.get(fallecimiento_id=fallecimiento_id)
    return FallecimientoSchema.from_orm(fallecimiento)


@api.get("/procedimientos")
def listar_procedimientos(request):
    procedimientos = Procedimiento.objects.all()
    return [ProcedimientoSchema.from_orm(procedimiento) for procedimiento in procedimientos]

@api.post("/procedimientos")
def crear_procedimiento(request, procedimiento: ProcedimientoSchema):
    nuevo_procedimiento = Procedimiento.objects.create(**procedimiento.dict())
    return ProcedimientoSchema.from_orm(nuevo_procedimiento)

@api.get("/procedimientos/{procedimiento_id}")
def obtener_procedimiento(request, procedimiento_id: int):
    procedimiento= Procedimiento.objects.get(procedimiento_id=procedimiento_id)
    return ProcedimientoSchema.from_orm(procedimiento)

@api.get("/desparasitaciones")
def listar_desparasitaciones(request):
    desparasitaciones = Desparasitacion.objects.all()
    return [DesparasitacionSchema.from_orm(desparasitacion) for desparasitacion in desparasitaciones]

@api.post("/desparasitaciones")
def crear_desparasitacion(request, desparasitacion: DesparasitacionSchema):
    nuevo_desparasitacion = Desparasitacion.objects.create(**desparasitacion.dict())
    return DesparasitacionSchema.from_orm(nuevo_desparasitacion)

@api.get("/desparasitaciones/{despa_id}")
def obtener_desparasitacion(request, despa_id: int):
    desparasitacion= Desparasitacion.objects.get(despa_id=despa_id)
    return DesparasitacionSchema.from_orm(desparasitacion)

#tablas ekisde

@api.get("/vv")
def listar_vv(request):
    vvs = Veterinario_Veterinaria.objects.all()
    return [VeterinarioVeterinariaSchema.from_orm(vv) for vv in vvs]

@api.get("/vv/{vv_veterinaria_id}")
def obtener_vv(request, vv_veterinaria_id: int):
    vvs = Veterinario_Veterinaria.objects.filter(vv_veterinaria_id=vv_veterinaria_id)
    return [VeterinarioVeterinariaSchema.from_orm(vv) for vv in vvs]
    #return Veterinario_Veterinaria.from_orm(vvs)

@api.post("/vv")
def crear_vv(request, Vv: VeterinarioVeterinariaSchema):
    nuevo_vv = Vv.objects.create(**Vv.dict())
    return  VeterinarioVeterinariaSchema.from_orm(nuevo_vv)


@api.get("/box")
def listar_boxs(request):
    boxs = Box.objects.all()
    return [BoxSchema.from_orm(box) for box in boxs]

@api.post("/box")
def crear_boxs(request, Box: BoxSchema):
    nuevo_box = Box.objects.create(**Box.dict())
    return BoxSchema.from_orm(nuevo_box)


@api.get("/bloques")
def listar_bloques(request):
    bloques = Bloque.objects.all()
    return [BloqueSchema.from_orm(bloque) for bloque in bloques]

@api.post("/bloques")
def crear_bloques(request, Bloque: BloqueSchema):
    nuevo_bloque = Bloque.objects.create(**Bloque.dict())
    return BloqueSchema.from_orm(nuevo_bloque)


@api.get("/dias")
def listar_dias(request):
    bloques = Bloque.objects.all()
    return [BloqueSchema.from_orm(bloque) for bloque in bloques]

@api.post("/dias")
def crear_dias(request, Bloque: BloqueSchema):
    nuevo_bloque = Bloque.objects.create(**Bloque.dict())
    return BloqueSchema.from_orm(nuevo_bloque)

@api.get("/calendarios")
def listar_calendarios(request):
    calendarios = Calendario.objects.all()
    return [CalendarioSchema.from_orm(calendario) for calendario in calendarios]

@api.post("/calendarios")
def crear_calendarios(request, Examen: ExamenFisicoSchema):
    nuevo_calendario = Calendario.objects.create(**Calendario.dict())
    return CalendarioSchema.from_orm(nuevo_calendario)

@api.get("/reservas")
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return [ReservaSchema.from_orm(reserva) for reserva in reservas]

@api.post("/reservas")
def crear_reservas(request, Examen: ExamenFisicoSchema):
    nuevo_reserva = Reserva.objects.create(**Reserva.dict())
    return ReservaSchema.from_orm(nuevo_reserva)

@api.get("/vvbds")
def listar_vvbds(request):
    vvbds = Vvbd.objects.all()
    return [VvbdSchema.from_orm(vvbd) for vvbd in vvbds]

@api.post("/vvbds")
def crear_vvbds(request, Vvbd: VvbdSchema):
    nuevo_vvbd = Vvbd.objects.create(**Vvbd.dict())
    return VvbdSchema.from_orm(nuevo_vvbd)

@api.get("/inventario")
def listar_inventario(request):
    inven = Inventario.objects.all()
    return [InventarioSchema.from_orm(inve) for inve in inven]

@api.post("/inventario")
def crear_inventario(request,  inventario: InventarioSchema):
    # Supongamos que la veterinaria con ID 1 ya existe
    veterinaria = Veterinaria.objects.get(veterinaria_id=1)

    # Crea la instancia de Inventario con la instancia de Veterinaria
    nuevo_inventario = Inventario.objects.create(
        inventario_cantidad=inventario.cantidad,
        inventario_nombre=inventario.nombre,
        inventario_descripcion=inventario.descripcion,
        inventario_veterinaria=veterinaria
    )

    return JsonResponse(InventarioSchema.from_orm(nuevo_inventario).dict(), status=201)    #return (InventarioSchema.from_orm(nuevo_inventario).dict())
    #nuevo_inventario = Inventario.objects.create(inventario_veterinaria=1, **inventario.dict())
    #Inventario: InventarioSchema):
    #nuevo_inventario = Inventario.objects.create(**Inventario.dict())
    #return InventarioSchema.from_orm(nuevo_inventario)


@api.get("/deudores")
def listar_deudores(request):
    deudores = Deudor.objects.all()
    return [DeudorSchema.from_orm(deudor) for deudor in deudores]

@api.post("/deudores")
def crear_deudores(request, Deudor: DeudorSchema):
    nuevo_deudor = Deudor.objects.create(**Deudor.dict())
    return DeudorSchema.from_orm(nuevo_deudor)


@api.get("/direcciones")
def listar_direcciones(request):
    direcciones = Direccion.objects.all()
    return [DireccionSchema.from_orm(direccion) for direccion in direcciones]

@api.post("/direcciones")
def crear_direcciones(request, Direccion: DireccionSchema):
    nueva_direccion = Direccion.objects.create(**Direccion.dict())
    return DireccionSchema.from_orm(nueva_direccion)

@api.get("/recetas")
def listar_recetas(request):
    recetas = Receta.objects.all()
    return [Receta.from_orm(receta) for receta in recetas]

@api.post("/recetas")
def crear_recetas(request, Receta: RecetaSchema):
    nueva_receta = Receta.objects.create(**Receta.dict())
    return RecetaSchema.from_orm(nueva_receta)
'''
@api.get("/imagenes")
def listar_imagenes(request):
    imagens = Imagen.objects.all()
    return [ImagenSchema.from_orm(imagen) for imagen in imagens]

@api.post("/imagenes")
def crear_imagenes(request, Imagen: ImagenSchema):
    nueva_imagen = Imagen.objects.create(**Imagen.dict())
    return ImagenSchema.from_orm(nueva_imagen)

@api.get("/imagenes/{imagen_id}")
def obtener_imagenes(request, imagen_id: int):
    imagen = Imagen.objects.get(imagen_id=imagen_id)
    return ImagenSchema.from_orm(imagen)'''

@api.get("/cosas")
def listar_cosas(request):
    cosas = Cosas.objects.all()
    return [CosasSchema.from_orm(cosa) for cosa in cosas]

@api.post("/cosas")
def crear_cosas(request, cosas: CosasSchema):
    nueva_cosa = Cosas.objects.create(**cosas.dict())
    return CosasSchema.from_orm(nueva_cosa)
'''
@api.put("/cosas/{cosas_id}")
def cosas_mas(request, cosa_id: int):
    co = Cosas.objects.get(cosa_id=cosa_id)
    co.cosas_id = co.cosas_id
    co.cosas_cantidad = co.cosas_cantidad +1 
    co.cosas_nombre =  co.cosas_nombre
    co.cosas_descripcion = co.cosas_descripcion
    co.save()
    return CosasSchema.from_orm(co)
'''