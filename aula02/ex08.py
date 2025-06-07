lado1 = float(input('Quanto mede o primeiro lado? '))
lado2 = float(input('Quanto mede o segundo lado? '))
lado3 = float(input('Quanto mede o terceiro lado? '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('É um triângulo equilatero')
    elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
        print('É um triângulo isosceles')
    elif lado1 != lado2 != lado3:
        print('É um triângulo escaleno')
else:
    print('Não se pode formar um triângulo')
