def maior_area():
    lista_medidas = [ int(input()) for i in range(4)]    
    if lista_medidas[0]*lista_medidas[1]>lista_medidas[2]*lista_medidas[3]:
        print(lista_medidas[0]*lista_medidas[1])
    else:
        print(lista_medidas[2]*lista_medidas[3])
maior_area()