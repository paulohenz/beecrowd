codigo, quantidade = map(float, input().split())
posicao = int(codigo) - 1
valores = [4.00, 4.50, 5.00, 2.00, 1.50]
total = valores[posicao] * quantidade
print(f'Total: R$ {total:.2f}')