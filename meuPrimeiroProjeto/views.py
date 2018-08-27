from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def helloworld(request):
    return HttpResponse('Hello World')

def articles(request, year):
    return HttpResponse('O ano passado foi ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 21},
        {'nome': 'Joao', 'idade': 22},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Nao encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    return HttpResponse('Encontrado: ' + str(result['idade']))

def fname2(request, nome):
    result = lerDoBanco(nome)
    print(result)
    return render(request, 'pessoa.html', {'v_idade': result['idade']})
