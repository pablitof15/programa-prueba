from django.shortcuts import render


def inicio(request):
    template_name="inicio.html"
    usuario= {
        "nombre":"Pablo",
        "apellido":"Flea"
        
    }
    ctx = {
        "user_dict":usuario
    }
    return render(request,template_name,ctx)