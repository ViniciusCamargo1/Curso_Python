print ("Atividade 1: ")
def comparar():
    n1 =  int(input('Digite o número 1:'))
    n2 =  int(input('Digite o número 2:'))

    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Ambos são pares',n1,n2)
    elif n1 % 2 == 0 or n2 % 2 == 0:
        print('Um deles é par',n1,n2)
    else:
        print('Ambos impares',n1,n2)
comparar()

print ("Atividade 2: ")
def multi():
    numero1 =  int(input('Digite o número 1:'))
    numero2 =  int(input('Digite o número 2:'))
    numero3 =  int(input('Digite o número 3:'))
    print("A multiplicação entre os números é :",numero1*numero2*numero3)
multi()


    