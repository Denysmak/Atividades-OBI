def tamanhoSequencia(): 
    tamanho_sequencia = int(input())
    lista_valores = [[None]]*tamanho_sequencia
    for i in range (tamanho_sequencia):
        numero = input()
        lista_valores[i] = int(numero)
    n_max_sequencia = lista_valores[0]
    contador = 1
    for i in lista_valores:
        if i != n_max_sequencia:
            contador+=1
            n_max_sequencia = i
    return contador

def main():
    tamanhoSequencia()

if __name__=='__main__':
    main()    

