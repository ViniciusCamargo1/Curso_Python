print("Atividade 1")
try:
     numero =  int(input('Insira um número inteiro: '))
except TypeError:
     print('Você não inseriu um número inteiro')
     
except ValueError:
    print('Você não inseriu um número inteiro')
else:
    print(numero,": Seu número é inteiro")

    print("Atividade 2")
try:
     n1 =  int(input('Insira o numero 1: '))
     n2 =  int(input('Insira o numero 2: '))
     div  =  n1 / n2
     print(div)
except ZeroDivisionError:
     print('O divisor não pode ser = 0')
except ValueError:
     print('Precisa ser um número')

print("Atividade 3")

try:
     lista = ["", "Nissan GTR R33","Nissan GTR R34","Nissan GTR R35"]
     visualizar_indice = int(input("Digite qual indice gostaria de ver:"))
     print(lista [visualizar_indice])
except IndexError:
    print("Digite um indice disponivel")