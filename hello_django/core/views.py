from django.shortcuts import render, HttpResponse

# Create your views here.

#exercicio 1
def hello(request, num1, num2, soma): #somar URL
    soma = 10 + 20
    return HttpResponse('A soma de  {} + {} é igual á: {}'.format( num1, num2, soma))

def sub_hello(request, num1, num2, soma): #subtrair a URL
    soma = num1 - num2
    return HttpResponse('A soma de  {} - {} é igual á: {}'.format( num1, num2, soma))

def mult_hello(request, num1, num2, soma): #multiplicar a URL
    soma = num1 * num2
    return HttpResponse('A soma de  {} - {} é igual á: {}'.format( num1, num2, soma))
