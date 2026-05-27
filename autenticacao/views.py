from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from django.contrib import messages
from django.contrib.messages import constants

def login(request):

    if request.method == 'GET':
        return render(request, 'login/login.html')

    elif request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        pessoa = Pessoa.objects.filter(
            email=email,
            senha=senha
        ).first()

        if not pessoa:

            messages.add_message(
                request,
                constants.WARNING,
                'Usuário inexistente!'
            )

            return redirect('login')

        else:

            request.session['pessoa_id'] = pessoa.id

            return redirect('dashboard')