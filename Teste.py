print("Atividade 2")
print('Escola Senai - 🏫')
usuario = ("professor01")
senha_correta = ("Senha123")
erros = 0
n1 = 0
n2 = 0
n3 = 0
notas = (n1,n2,n3)
media = notas/3
while True:
    tentativa_usuario = input("Digite seu usuario: ")
    if tentativa_usuario == usuario:
        print("Usuario correto")
        tentativa_senha= input("Digite sua senha: ")
    if tentativa_senha == senha_correta:
        print("Sua senha está correta")
        print("Acesso realizado com sucesso, Olá ",usuario)
        lançar_media = input ("Deseja lançar as medias?")
        if lançar_media == ("sim"): 
            notas = input("'digite a nota 1:', n1 'digite a nota 2:',n2 'digite a nota 3',n3")
    else:
        print("usuario incorreto, tente novamente")
    erros = erros +1
    print("Erros:",erros)

    tentativa_senha= input("Digite sua senha")
    if tentativa_senha == senha_correta:
        print("Sua senha está correta")
        print("Acesso realizado com sucesso, Olá ",usuario)