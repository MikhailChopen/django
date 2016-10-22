from django.shortcuts import render
from django.http import HttpResponse
from .models import Asignacion, Estudiante
from .forms import estudianteForm, asignacionForm

def home(request):

	template = "practica/home.html"
	asignados = Asignacion.objects.select_related().values('carnet__nombre','carnet__apellido','id_asignacion','nombre_curso','carnet__carnet','ciclo')

	context = {'asignados':asignados}
	return render(request,template,context)


def estudiantes(request):
	template = "practica/estudiantes.html"
	estu = Estudiante.objects.all()
	form = estudianteForm()
	

	if request.method == "POST":
		form = estudianteForm(request.POST)

		tipo = request.POST.get('tipo',False)

		if tipo == '1':
			if form.is_valid():
				estudiante = form.save(commit=True)
				form = estudianteForm()
				print("SI")
			else:
				form = form()
				print("NO")
		else:
			carnn = request.POST.get('carn',False)
			objeto = Estudiante.objects.get(carnet=carnn)
			asigacion = Asignacion.objects.filter(carnet__carnet=carnn)
			asigacion.delete()
			objeto.delete()


	form.fields['nombre'].widget.attrs = {'class':'form-control'}
	form.fields['apellido'].widget.attrs = {'class':'form-control'}

	context = {'estu':estu,'form':form}
	return render(request,template,context)


def editarestu(request):
	template = "practica/editarestu.html"
	
	form = estudianteForm()
	

	if request.method == "POST":
		form = estudianteForm(request.POST)
		carnn = request.POST.get('carnn',False)
		tipo = request.POST.get('tipo',False)


		if tipo == '3':
			
			objeto = Estudiante.objects.get(carnet=carnn)
			data = {'nombre':objeto.nombre,'apellido': objeto.apellido}
			form = estudianteForm(initial=data)
		else:
			
			if form.is_valid():
				form.save()
			else:
				
				objeto = Estudiante.objects.get(carnet=carnn)
				data = {'nombre':objeto.nombre,'apellido': objeto.apellido}
				form = estudianteForm(initial=data)
				


	form.fields['nombre'].widget.attrs = {'class':'form-control'}
	form.fields['apellido'].widget.attrs = {'class':'form-control'}

	context = {'form':form}
	return render(request,template,context)



def asignaciones(request):
	template = "practica/asignaciones.html"
	asigna = Asignacion.objects.select_related().values('id_asignacion','nombre_curso','carnet__carnet','ciclo')
	form = asignacionForm()
	

	if request.method == "POST":
		form = asignacionForm(request.POST)

		tipo = request.POST.get('tipo',False)
		
		if tipo == '1':
			
			if form.is_valid():
				asignac = form.save(commit=True)
				form = asignacionForm()
			else:
				print("nol")
		else:
			idasig = request.POST.get('idasig',False)
			objeto = Asignacion.objects.get(id_asignacion=idasig)
			objeto.delete()


	

	form.fields['nombre_curso'].widget.attrs = {'class':'form-control'}
	form.fields['carnet'].widget.attrs = {'class':'form-control'}
	form.fields['ciclo'].widget.attrs = {'class':'form-control'}

	context = {'asigna':asigna,'form':form}
	return render(request,template,context)


def editarasig(request):
	template = "practica/editarasig.html"
	
	form = asignacionForm()
	

	if request.method == "POST":
		form = asignacionForm(request.POST)

		tipo = request.POST.get('tipo',False)

		if tipo == '3':
			idasig = request.POST.get('idasig',False)
			objeto = Asignacion.objects.get(id_asignacion=idasig)
			data = {'carnet':objeto.carnet,'nombre_curso':objeto.nombre_curso,'ciclo': objeto.ciclo}
			form = asignacionForm(initial=data)
		else:
			
			if form.is_valid():
				form.save()
			else:
				idasig = request.POST.get('idasig',False)
				objeto = Asignacion.objects.get(id_asignacion=idasig)
				data = {'carnet':objeto.carnet,'nombre_curso':objeto.nombre_curso,'ciclo': objeto.ciclo}
				form = asignacionForm(initial=data)
				


	form.fields['nombre_curso'].widget.attrs = {'class':'form-control'}
	form.fields['carnet'].widget.attrs = {'class':'form-control'}
	form.fields['ciclo'].widget.attrs = {'class':'form-control'}

	context = {'form':form}
	return render(request,template,context)

"""

def asignaciones(request):
	template = "practica/asignaciones.html"
	asigna = Asignacion.objects.select_related().values('id_asignacion','nombre_curso','carnet__carnet','ciclo')

	form = asignacionForm()
	form.fields['nombre_curso'].widget.attrs = {'class':'form-control'}
	form.fields['carnet'].widget.attrs = {'class':'form-control'}
	form.fields['ciclo'].widget.attrs = {'class':'form-control'}

	print (form)

	context = {'asigna':asigna,'form':form}
	return render(request,template,context)

"""