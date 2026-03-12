print("Exercicio 1")
numero = int(input('numero:'))

match numero:

    case numero if numero % 2 == 0:
        print("é par")
    case _:
        print('É impar')

print("Exercicio 2")
numero1 = int(input('Digite 1 numero: '))
match numero:
    case numero1 if numero1 > 0:
        print('Positivo')
    case numero1 if numero1 < 0:
        print('Negativo')
    case _:
        print('Zero')         

print("Exercicio 3")
digito = input('Digite algo = ')

match digito:
    case '':
      print('Vazia')
    case _:
      print('Cheia')

print("Exercicio 4")
numero2 = int(input('Digite um numero: '))
match numero2:
    case numero2 if numero2 > 10:
     print('Numero maior que 10')
    case numero2 if numero2 == 10:
     print('Numero é igual a 10')
    case _:
     print("Numero menor que 10")

print("Exercicio 5")
idade = int(input('Digite sua idade: '))
match idade:
    case idade if idade <13:
      print("faixa etária de criança")
    case idade if idade > 14 and idade <17:
      print("faixa etária de adolescente")
    case idade if idade > 18 and idade <35:
      print("faixa etária de jovem")
    case idade if idade >=35 and idade <63:
      print("faixa etária de Adulto")
    case _:
      print("Idoso")
