
from django.db import models

class ReporteSoliUsua(models.Model):
    cod_report_usua = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=100)
    prioridad = models.CharField(max_length=10)
    class Meta:
        	db_table = u'reporte_soli_usua'
    def __unicode__(self):
	    return self.descripcion
    

class CalidadAtencion(models.Model):
    cod_atencion = models.IntegerField(primary_key=True)
    calificacion = models.CharField(max_length=10)
    class Meta:
        db_table = u'calidad_atencion'
    def __unicode__(self):
	    return(self.calificacion)

class Dependencias(models.Model):
    cod_dependencia = models.IntegerField(primary_key=True)
    nombre_dependencia = models.CharField(max_length=45)
    class Meta:
        db_table = u'dependencias'
    def __unicode__(self):
        return self.nombre_dependencia


class Usuarios(models.Model):
    cod_usuario = models.IntegerField(primary_key=True)
    cod_dependencia = models.ForeignKey(Dependencias, db_column='cod_dependencia')
    cod_atencion = models.ForeignKey(CalidadAtencion, db_column='cod_atencion')
    nombre_usuario = models.CharField(max_length=45)
    direccio = models.CharField(max_length=45)
    telefono = models.IntegerField()
    apellido = models.CharField(max_length=45)
    class Meta:
        db_table = u'usuarios'

class ReportSolucProb(models.Model):
    cod_report_soluc_prob = models.IntegerField(primary_key=True)
    solucion = models.CharField(max_length=100)
    class Meta:
        db_table = u'report_soluc_prob'

class Tecnico(models.Model):
    cod_tecnico = models.IntegerField(primary_key=True)
    nombre_tecnico = models.CharField(max_length=45)
    apellido_tecnico = models.CharField(max_length=45)
    class Meta:
        db_table = u'tecnico'
    def __unicode__(self):
        nombreCompleto = "%s %s"%(self.nombre_tecnico,self.apellido_tecnico)
        return nombreCompleto

class Caso(models.Model):
    cod_caso = models.IntegerField()
    cod_report_usua = models.ForeignKey(ReporteSoliUsua, db_column='cod_report_usua')
    cod_usuario = models.ForeignKey(Usuarios, db_column='cod_usuario')
    class Meta:
        db_table = u'caso'

class CierreCaso(models.Model):
    cod_cierre_caso = models.CharField(max_length=10, primary_key=True)
    soluccion = models.CharField(max_length=10)
    class Meta:
        db_table = u'cierre_caso'
    
class Conclucion(models.Model):
    cod_conclucion = models.IntegerField()
    cod_cierre_caso = models.ForeignKey(CierreCaso, db_column='cod_cierre_caso')
    cod_usuario = models.ForeignKey(Usuarios, db_column='cod_usuario')
    class Meta:
        db_table = u'conclucion'

class Revision(models.Model):
    cod_revision = models.IntegerField()
    cod_tecnico = models.ForeignKey(Tecnico, db_column='cod_tecnico')
    cod_report_usua = models.ForeignKey(ReporteSoliUsua, db_column='cod_report_usua')
    class Meta:
        db_table = u'revision'

class Solucionar(models.Model):
    cod_solucionar = models.IntegerField()
    cod_report_soluc_prob = models.ForeignKey(ReportSolucProb, db_column='cod_report_soluc_prob')
    cod_tecnico = models.ForeignKey(Tecnico, db_column='cod_tecnico')
    class Meta:
        db_table = u'solucionar'



