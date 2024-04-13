def n_chamadas(n):
  contador = 0
  def calcula(n):
    nonlocal contador
    contador += 1
    if n == 1:
      return 1
    elif n%2==0:
      return calcula(n/2)
    else:
      return calcula(3*n+1) 
  calcula(n)
  return contador

def main():
  casos_teste = int(input())
  lista_resposta = [None]*casos_teste
  for i in range(casos_teste):
    maior_valor = 0
    a_e_b = input().split()
    for e in range(int(a_e_b[0]), int(a_e_b[1]) + 1):
      if n_chamadas(e)>maior_valor:
        maior_valor = n_chamadas(e)
    lista_resposta[i] = maior_valor
  for indice, valor in enumerate(lista_resposta):
    print(f'caso {indice + 1}: {valor}')
main()
