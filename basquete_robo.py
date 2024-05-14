def pontuacao():
    distancia = int(input())
    if distancia <= 800:
        print(1)
    elif distancia <= 1400:
        print(2)
    else:
        print(3)      
if __name__ == '__main__':
    pontuacao()        