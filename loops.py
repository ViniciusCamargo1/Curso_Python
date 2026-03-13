print("Atividade 1.1")
contador_numero = 0
while contador_numero <= 1000:
    print("O numero é",contador_numero)
    contador_numero += 1

print("Atividade 1.2")
nomes =[]
contador_nomes = 0 

while contador_nomes <= 10:
    nome = input("Escreva o Nome:")
    nomes.append(nome)
    contador_nomes +=1
    print("Lista de nomes: ",nomes)

print("Atividade 2")
print('Escola Senai - 🏫')
chances = 3
senha_correta = ("Senha123")
for chances in range (3):
    print('Escola Senai - 🏫')
senha = input("Digite a sua senha: ")
if senha == senha_correta:
    print("Acesso Realizado com Sucesso =) ")
    