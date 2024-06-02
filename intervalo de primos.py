p1 = int(input('Digite o primeiro valor do intervalo: '))
p2 = int(input('Digite o segundo valor do intervalo: '))
contador = 2
resultado = 0
primos = 0

while p1 <= p2:
    if p1 == 2:
        primos += 1
    while contador < p1:
        resultado = p1 % contador
        if resultado == 0:
            break
        else:
            contador += 1
    if resultado != 0:
        primos += 1
    p1 += 1
    contador = 2
print('A quantidade de primos nesse intervalo é {}'.format(primos))