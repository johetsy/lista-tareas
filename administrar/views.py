from django.shortcuts import render
from django.http import HttpResponseRedirect 
from administrar.models import Tarea
from .forms import TareaForm

# Create your views here.
def v_index(request):
  if request.method == 'POST':
    ####
    #Post voy a crear un registro
    ###
    _titulo = request.POST["titulo"]

    datos = request.POST.copy()
    form = TareaForm(datos)
    if form. is_valid():
      form.save()
    else:
      return HttpResponseRedirect("/")   
      
    if False:
      # se usa el if false cuando no queremos que se ejecute las lineas de codgo que esten dentro del if
      tarea = Tarea() #instancio un modelo
      tarea.titulo = _titulo #asigno titulo a la tarea
      tarea.save()
    
    return HttpResponseRedirect("/")
    
  else:
    #Peticiones method = GET 
    #icontains es para que acepte mayusculas y minusculas
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo", ""))
    
    if request.GET.get("estado","") != "":
      consulta = consulta.filter(estado = request.GET.get("estado", ""))
      
    #listar tareas
    
    context = {
      'var1': 'Valor1',
      'var2': 'Valor123456',
      'lista': consulta
  }
  return render(request,'index.html', context)

def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id = tarea_id).delete()
  return HttpResponseRedirect("/")

def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1 #la marca como completado
  task.save()
  return HttpResponseRedirect("/")
  