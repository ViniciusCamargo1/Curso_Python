dados = {
'nomes':[],
'idades':[],
'quartos':["Simples", "Duplo" , "Luxo"],
'valores':[100.0,150.0,250.0],
}

quantidade_de_pessoas = int(input('Quantidade de Pessoas:'))
valor_quartos= input('Escolha qual o quarto: Simples R$100 Duplo R$150 Luxo R$250')
dias = 0
valor_reserva = 0

if quantidade_de_pessoas == 1:
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))
    dias = int(input("Dias de estadia: "))
    if valor_quartos == "simples":
     valor_reserva = (dias * 100.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "duplo":
     valor_reserva = (dias * 150.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "luxo":
     valor_reserva = (dias * 250.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)

elif quantidade_de_pessoas == 2:
    dados['nomes'].append(input('Digite  o nome da 1 pessoa: '))
    dados['idades'].append(input('Digite  a Idade da 1 pessoa: '))    
    dados['nomes'].append(input('Digite  o nome da 2 pessoa: '))
    dados['idades'].append(input('Digite  a Idade da 2 pessoa: '))
    dias = int(input("Dias de estadia: "))
    if valor_quartos == "simples":
     valor_reserva = (dias * 100.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "duplo":
     valor_reserva = (dias * 150.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "luxo":
     valor_reserva = (dias * 250.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)

elif quantidade_de_pessoas == 3:
    dados['nomes'].append(input('Digite  o nome da 1 pessoa: '))
    dados['idades'].append(input('Digite  a Idade da 1 pessoa: '))    
    dados['nomes'].append(input('Digite  o nome da 2 pessoa: '))
    dados['idades'].append(input('Digite  a Idade da 2 pessoa: '))    
    dados['nomes'].append(input('Digite  o nome da 3 pessoa: '))
    dados['idades'].append(input('Digite  a Idade da 3 pessoa: '))    
    dias = int(input("Dias de estadia: "))
    if valor_quartos == "simples":
     valor_reserva = (dias * 100.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "duplo":
     valor_reserva = (dias * 150.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)
    elif valor_quartos == "luxo":
     valor_reserva = (dias * 250.00)*quantidade_de_pessoas
     print ('O Valor da reserva é:',valor_reserva)

else:
    print('Digite algo válido... ')



