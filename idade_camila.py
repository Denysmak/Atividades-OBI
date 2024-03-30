#idade_um = input('primeira idade: ')
#idade_dois = input('segunda idade: ')
#idade_tres = input('terceira idade: ')
lista_desordenada = []
lista_ordenada = []
""" maior_valor = 0 """
for i in range(3):
    idade = input()
    lista_desordenada.append(int(idade))
while len(lista_desordenada) > 0:   
    maior_valor = 0
    for i in lista_desordenada:
        if i >= maior_valor:
            maior_valor = i
            lista_ordenada.append(maior_valor)
    lista_desordenada.remove(maior_valor)     
print(lista_desordenada)




