from django.contrib import admin
from mesa.models import *

class ReporteSoliUsua1(admin.ModelAdmin):
    list_display= ("descripcion",)
    search_fields = ("cod_report_usua",)
    lister_filter = ("prioridad",)
    
admin.site.register(ReporteSoliUsua,ReporteSoliUsua1)

class CalidadAtencion1(admin.ModelAdmin):
    list_display= ("calificacion",)
    search_fields = ("cod_atencion",)

admin.site.register(CalidadAtencion,CalidadAtencion1)

class Dependencias1(admin.ModelAdmin):
    list_display= ("cod_dependencia",)
    search_fields = ("nombre_dependencia",)

admin.site.register(Dependencias,Dependencias1)

class Usuarios1(admin.ModelAdmin):
    list_display= ("cod_usuario",)
    search_fields = ("cod_dependencia",)
    lister_filter = ("cod_atencion",)
    list_display= ("nombre_usuario,apellido",)
    search_fields = ("direccio",)
    lister_filter = ("telefono",)
    list_display= ("apellido",)

admin.site.register(Usuarios,Usuarios1)
    
class ReportSolucProb1(admin.ModelAdmin):
    list_display= ("cod_report_soluc_prob",)
    search_fields = ("solucion",)

admin.site.register(ReportSolucProb,ReportSolucProb1)

class Tecnico1(admin.ModelAdmin):
    list_display= ("cod_tecnico",)
    search_fields = ("nombre_tecnico",)
    lister_filter = ("apellido_tecnico",)

admin.site.register(Tecnico,Tecnico1)
    


class Caso1(admin.ModelAdmin):
    list_display= ("cod_caso",)
    search_fields = ("cod_report_usua",)
    lister_filter = ("cod_usuario",)

admin.site.register(Caso,Caso1)
    

class CierreCaso1(admin.ModelAdmin):
    list_display= ("cod_cierre_caso",)
    search_fields = ("soluccion",)

admin.site.register(CierreCaso,CierreCaso1)
    

class Conclucion1(admin.ModelAdmin):
    list_display= ("cod_conclucion",)
    search_fields = ("cod_cierre_caso",)
    lister_filter = ("cod_usuario",)

admin.site.register(Conclucion,Conclucion1)
    

class Revision1(admin.ModelAdmin):
    list_display= ("cod_revision",)
    search_fields = ("cod_tecnico",)
    lister_filter = ("cod_report_usua",)

admin.site.register(Revision,Revision1)
    

class Solucionar1(admin.ModelAdmin):
    list_display= ("cod_solucionar",)
    search_fields = ("cod_report_soluc_prob",)
    lister_filter = ("cod_tecnico",)

admin.site.register(Solucionar,Solucionar1)
   



    





