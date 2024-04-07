def lampadas():
    n_apertos = int(input())
    interruptores_apertados = input().split()
    n_ums = 0
    n_dois = 0
    for i in interruptores_apertados:
        if i == '1':
            n_ums += 1
        else: 
            n_dois += 1
    if n_dois%2 == 0:
        if n_ums%2==0:
            resultado = 0,0
        else:
            resultado = 1,0    
    else:
        if n_ums == 0:
            resultado = 1,1
        else:
            resultado = 0,1    
    print(resultado[0])
    print(resultado[1])
lampadas()    