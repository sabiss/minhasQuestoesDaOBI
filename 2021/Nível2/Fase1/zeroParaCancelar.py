numeroDeNumeroFalados = int(input())

arrayDeNumeros = []
cont = 0

while(cont < numeroDeNumeroFalados):
    numero = int(input())
    if(numero == 0):
        arrayDeNumeros.pop()
    else:
        arrayDeNumeros.append(numero)
    cont+=1
soma = 0

for numero in arrayDeNumeros:
    soma+=numero
print(soma)
