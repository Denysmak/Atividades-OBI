def peca_perdida():
  n_pecas = int(input())
  soma_valores_lista_completa = 0
  soma_valores_lista_incompleta = 0
  contagem_pecas = input().split()
  lista_pecas_completa = [i for i in range(1,n_pecas+1)]
  for i in lista_pecas_completa:
    soma_valores_lista_completa += i
  for i in range(len(contagem_pecas)):
    soma_valores_lista_incompleta += int(contagem_pecas[i])
  return soma_valores_lista_completa - soma_valores_lista_incompleta
def main():
  print(peca_perdida())
if __name__ == '__main__':
  main()