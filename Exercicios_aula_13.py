import random
print ("Atividade 1")

def atividade1():
    x = random.randint(5, 10)
    return x
  
print ("Atividade 2")
def atividade2():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    return x, y, z

print ("Atividade 3")
def atividade3():
    x = random.choice(range(10, 31)) 
    return x
print ("Atividade 4")
def atividade4():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")

print ("Atividade 5")
def atividade5():
    numero_str = input("Insira um número inteiro positivo: ")
    
    if numero_str.isdigit():
        numero = int(numero_str)
        soma = 0
        
        for i in range(2, numero + 1):
            if i % 2 == 0: 
                soma += i
                
        return f"A soma dos números pares de 2 até {numero} é: {soma}"
    else:
        return "Entrada inválida. Por favor, insira apenas números inteiros."
      
print ("Atividade 6")
def atividade6():
    numero_str = input("Insira um número inteiro para ver a tabuada: ")
    
    try:
        numero = int(numero_str)
        print(f"\n--- Tabuada do {numero} ---")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Entrada inválida. Você não digitou um número inteiro.")
      
print ("Atividade 7")
def atividade7():
    for i in range(99, 0, -2):
        print(i, end=" ")
    print()
