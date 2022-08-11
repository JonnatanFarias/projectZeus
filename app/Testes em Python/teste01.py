print()
print('Olá bem vindo a calculadora de IMC')
print('*'*35)
nome=input('Qual é o seu nome? = ')
idade=int(input('Por informe sua idade = '))
altura=float(input('Sua altura (ex 0.00) = '))
peso=int(input('Seu peso = '))
imc = peso / altura**2
print()

if imc < 16: 
	print('O Resultado foi...\n'+'*'*20)
	print('Magreza grave\n'+'*'*20)
elif imc < 17:
	print('O Resultado foi...\n'+'*'*20)
	print('Magreza moderada\n'+'*'*20) 
elif imc < 18.5:
	print('O Resultado foi...\n'+'*'*20)
	print('Magreza leve\n'+'*'*20)
elif imc < 25:  
	print('O Resultado foi...\n'+'*'*20) 
	print('Saudável\n'+'*'*20)
elif imc < 30:       
	print('O Resultado foi...\n'+'*'*20)
	print('Sobrepeso\n'+'*'*20)
elif imc < 35:       
	print('O Resultado foi...\n'+'*'*20)
	print('Obesidade Grau I\n'+'*'*20)
elif imc < 40:     
	print('O Resultado foi...'+'*'*20)   
	print('Obesidade Grau II (severa)\n'+'*'*20)
else:        
	print('O Resultado foi...'+'*'*20)
	print('Obesidade Grau III (mórbida)\n'+'*'*20)
print()
print('Dados coletados com sucesso')
print('Nome informado : '+ nome)
print('Idade informada : ',idade)
print('Altura informada : ',altura)
print('Peso informado : ',peso)
print('Valor índice de massa corporal : ',imc)

print()
sair=input('Para fechar a janela , aperte Enter.')
print(sair)