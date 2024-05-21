def figurinhasFaltando():
    qtd_figurinhas_album = int(input())
    qtd_figurinhas_compradas = int(input())   
    lista_figurinhas_compradas = set()
    for _ in range(qtd_figurinhas_compradas):
        figurinha = int(input())
        lista_figurinhas_compradas.add(figurinha)
    print(qtd_figurinhas_album - len(lista_figurinhas_compradas))
if __name__ == '__main__':
    figurinhasFaltando()








