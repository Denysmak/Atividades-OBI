def janela():
    resposta = 'N'
    todas_dimensoes = [None] * 5
    for i in range(5):
        todas_dimensoes[i] = int(input())
    x = 20
    y = 10
    for i in range(3):
        for j in range(3):
            if i != j and ((todas_dimensoes[i] <= todas_dimensoes[3] and todas_dimensoes[j] <= todas_dimensoes[4]) or (todas_dimensoes[i] <= todas_dimensoes[4] and todas_dimensoes[j] <= todas_dimensoes[3])):
                resposta = 'S'
    print(resposta)
if __name__ == '__main__':
    janela()