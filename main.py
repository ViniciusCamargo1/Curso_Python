import os
import shutil

#Utilizando Python:

#**Exercício 1: Criar e ler um Arquivo**
teste = "meu_arquivo.txt"

# Criando arquivo
with open(teste, 'w') as arquivo:
    arquivo.write("Ola Este é um texto de teste para o exercício 1")

# Lendo o arquivo 
with open(teste, 'r') as arquivo:
    conteudo = arquivo.read()
    print("--- Conteúdo do Arquivo ---")
    print(conteudo)

#**Exemplo 2: Cria um Diretório**

teste_de_diretorio = "pasta_exemplo"

if not os.path.exists(teste_de_diretorio):
    os.mkdir(teste_de_diretorio)
    print(f"Diretório '{teste_de_diretorio}' criado com sucesso!\n")
else:
    print(f"O diretório '{teste_de_diretorio}' já existe.\n")

#**Exercício 3: Renomear um Diretório**
novo_nome_diretorio = "pasta_renomeada"

# Renomeando de "pasta_exemplo" para "pasta_renomeada"
if os.path.exists(teste_de_diretorio):
    os.rename(teste_de_diretorio, novo_nome_diretorio)
    print(f"Diretório renomeado para '{novo_nome_diretorio}'.\n")

#**Exercício 4:  Listar Arquivos em um Diretório** 

diretorio_atual = "."

lista_de_arquivos = os.listdir(diretorio_atual)

print("--- Itens no Diretório Atual ---")
for item in lista_de_arquivos:
    print(f"- {item}")

#**Exercício 5:  Copiar Arquivos em um Diretório**

caminho_destino = os.path.join(novo_nome_diretorio, "copia_meu_arquivo.txt")
shutil.copy(teste, caminho_destino)
print(f"Arquivo copiado com sucesso para: {caminho_destino}\n")

#**Exercício 6:  Remover**

if os.path.exists(teste):
    os.remove(teste)
    print(f"Arquivo '{teste}' removido.")

if os.path.exists(caminho_destino):
    os.remove(caminho_destino)
    print(f"Arquivo '{caminho_destino}' removido.")

if os.path.exists(novo_nome_diretorio):
    os.rmdir(novo_nome_diretorio)
    print(f"Diretório '{novo_nome_diretorio}' removido.\n")