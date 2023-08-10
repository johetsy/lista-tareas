from django.shortcuts import render
from django.http import HttpResponseRedirect 
from administrar.models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url = "/iniciar-sesion")
@permission_required('administrar.view_tarea', login_url="/iniciar-sesion")
def v_index(request):
  if request.method == 'POST':
    ####
    #Post voy a crear un registro
    ###
    if not request.user.has_perm("administrar.add_tarea"):
      return HttpResponseRedirect("/permisos-denegados")
      
    _titulo = request.POST["titulo"]
    
    datos = request.POST.copy()
    
    form = TareaForm(datos) #para validaciones
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

@login_required(login_url = "/iniciar-sesion")
@permission_required('administrar.delete_tarea', login_url="/iniciar-sesion")
def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id = tarea_id).delete()
  return HttpResponseRedirect("/")
  
@login_required(login_url = "/iniciar-sesion")
@permission_required('administrar.change_tarea', login_url="/permiso-denegado")
def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1 #la marca como completado
  task.save()
  return HttpResponseRedirect("/")

def v_denied(request):
    return render(request, 'permission-denied.html')

def v_login(request):
  from .forms import LoginForm #importando el formulario
  from django.contrib.auth import authenticate, login
  
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid(): #verifica los datos que necesita
      user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password"]) 
      if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
      else:
        return HttpResponseRedirect("/")
    else:
    #los datos no son correctos
      return HttpResponseRedirect("/")
  else:
    context = {
      "form": LoginForm(request.POST) #envio un formal html
    }
  return render(request, "login.html", context)

def v_logout(request):
  from django.contrib.auth import logout
  
  if request.user.is_authenticated:
    logout(request) #aqui se cierra la sesion

  return HttpResponseRedirect("/")
  

