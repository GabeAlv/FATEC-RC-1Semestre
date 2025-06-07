print('='*5+'Conversor de notas para conceito'+'='*5)
nota = float(input('Qual a sua nota de 0 a 10? '))

if 10 >= nota >= 9:
    print('Sua nota é A')
elif 8.9 >= nota >= 7:
    print('Sua nota é B')
elif 6.9 >= nota >= 5:
    print('Sua nota é C')
elif 4.9 >= nota >= 3:
    print('Sua nota é D')
elif 2.9 >= nota >= 0:
    print('Sua nota é E')
print('='*42)