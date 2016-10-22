from django import forms
from .models import Asignacion, Estudiante

class estudianteForm(forms.ModelForm):

	class Meta:
		model = Estudiante
		fields = ('carnet','nombre','apellido')
		def __unicode__(self):
			return u'{0}'.format(self.carnet)


class asignacionForm(forms.ModelForm):
	"""carnet =  forms.ModelChoiceField(queryset= Estudiante.objects.values('carnet').values_list('carnet',flat=True))"""
	class Meta:
		model = Asignacion
		fields = ('id_asignacion','nombre_curso','carnet','ciclo')
