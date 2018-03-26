from django.shortcuts import render
from django.contrib.auth.forms import \
    UserCreationForm  # aqui importamos o django battery included form de User, o qual utiliza o model user dele mesmo também


# Create your views here.

def signup(request):
    form = UserCreationForm() #instanciamos a UserCreationForm na variável form
    return render(request, 'signup.html', {'form': form}) #retornamos o renderizador com os objetos respectivos

#daqui voltamos para o signup.html
