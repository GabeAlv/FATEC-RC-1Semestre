nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print(f'Você tirou {nota}, está APROVADO')
elif 6.9 >= nota > 5:
    print(f'Você tirou {nota}, está de RECUPERAÇÃO')
else:
    print(f'Você tirou {nota}, está REPROVADO')
