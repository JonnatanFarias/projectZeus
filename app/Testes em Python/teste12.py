#phonenumbers é um dos módulos que fornece vários recursos,
#como o fornecimento de informações básicas de um número de telefone,
#validação de um número de telefone, etc.
import phonenumbers
from phonenumbers import carrier , geocoder
import time

tempoinit = time.time()
#Número aleatório inválido.
numtel = "+55219991111111111"
#Convertendo String para o formato de número de telefone.
numtelconv = phonenumbers.parse(numtel)
#Validar número de telefone se é True ou False.
validar = phonenumbers.is_valid_number(numtelconv)
if validar == True:
    print("Este número de telefone é válido >>" , validar)
else:
    print("Este número de telefone é inválido >>" , validar)
#Descobrindo operadora e região de um número de telefone.
operadora = carrier.name_for_valid_number(numtelconv, "pt-BR")
cidade = geocoder.description_for_valid_number(numtelconv, "pt-BR")
print(operadora)
print(cidade)
timeend = time.time()
print(f"Demorou {int(timeend-tempoinit)} segundos")






  







