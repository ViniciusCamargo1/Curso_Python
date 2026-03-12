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
idade  =  int(input('idade: '))

match idade:
    case x if x >= 0 and x <=12:
        print('Crianca')
    case x if x >12 and x <= 17:
        print('Adolescente')
    case x if x >=18 and x <=35:
        print('jovem')
    case x if x >= 36 and x <64:
        print('Adulto')
    case _:
        print('Idoso ')                


