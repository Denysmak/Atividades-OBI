def quem_ganhou():
    lista_numeros = [int(input()) for i in range(3)]
    quem_par = lista_numeros[0]
    if (lista_numeros[1]+lista_numeros[2])%2 == 0:
        print(quem_par)
    else:
        if quem_par == 0:
            print(1)
        else:
            print(0)
quem_ganhou()        