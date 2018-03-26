from django.shortcuts import render, redirect
from django.contrib.auth.forms import \
    UserCreationForm  # aqui importamos o django battery included form de User, o qual utiliza o model user dele mesmo também
from django.contrib.auth import login as auth_login  # novamente o AS é para criar um alias.


# Create your views here.

def signup(request):
    if request.method == 'POST':  # aqui validamos se é um POST ou GET (post seria forms enviadas e etc)
        form = UserCreationForm(request.POST)  # aqui atribuimos os dados recebidos a variavel form
        if form.is_valid():  # valida os dados da form
            user = form.save()  # cria um User, não salva no DB
            auth_login(request, user)  # não sei, a adicionar // edit: Aqui o user criado é autenticado
            return redirect('home')  # redireciona para home após cadastro OK e user autenticado
    else:
        form = UserCreationForm()  # instanciamos a UserCreationForm na variável form SE FOR GET (CONFORME IF LA EM CIMA)
    return render(request, 'signup.html', {'form': form})  # retornamos o renderizador com os objetos respectivos

# daqui voltamos para o signup.html
