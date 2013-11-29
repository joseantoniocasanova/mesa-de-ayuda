from django.contrib import admin
from mesa.models import *

class ReporteSoliUsua(models.Model):


    cod_report_usua = ("codigo_reporte",)
    descripcion = ("descripcion_problema")
    prioridad = ("prioridad")
    
admin.site.register(ReporteSoliUsua)

class CalidadAtencion(models.Model):
    cod_atencion = ("cod_atencion",)
    calificacion = ("calificacion",)
    
admin.site.register(CalidadAtencion)

class Dependencias(models.Model):
    cod_dependencia = ("dependencia",)
    nombre_dependencia = ("nomdependencia",)

admin.site.register(Dependencias)

class Usuarios(models.Model):
    cod_usuario = ("usuario",)
    cod_dependencia = ("dependencia",)
    cod_atencion = ("atencion",)
    nombre_usuario = ("nombusuario",)
    direccio = ("direccion",)
    telefono = ("telefono",)
    apellido = ("apellido",)

admin.site.register(Usuarios)
    
class ReportSolucProb(models.Model):
    cod_report_soluc_prob = ("codtecnico",)
    solucion = ("detsolucion",)

admin.site.register(ReportSolucProb)

class Tecnico(models.Model):
    cod_tecnico = ("codtecnico",)
    nombre_tecnico = ("nombtecnico",)
    apellido_tecnico = ("apelltecnico",)

admin.site.register(Tecnico)
    


class Caso(models.Model):
    cod_caso = ("codcaso",)
    cod_report_usua = ("codrepousuario",)
    cod_usuario = ("codusuario",)

admin.site.register(Caso)
    


class CierreCaso(models.Model):
    cod_cierre_caso = ("codcierre",)
    soluccion = ("solucion",)

admin.site.register(CierreCaso)
    

class Conclucion(models.Model):
    cod_conclucion = ("codconclusion",)
    cod_cierre_caso = ("codcierre",)
    cod_usuario = ("codusuario",)

admin.site.register(Conclucion)
    

class Revision(models.Model):
    cod_revision = ("codrevision",)
    cod_tecnico = ("codtecnico",)
    cod_report_usua = ("codreport",)

admin.site.register(Revision)
    

class Solucionar(models.Model):
    cod_solucionar = ("codsolucion",)
    cod_report_soluc_prob = ("codreportsol",)
    cod_tecnico = ("codtecnico",)

admin.site.register(Solucionar)
   



    





