valor=int(input('Qual número de tabuada que você quer?'))
aux = 0

print('='*16)
print('Tabuada de {}'.format(valor))
print('='*16)
while(aux <=10):
    print('{0} X {1} = {2}'.format(aux,valor,(aux*valor)))
    aux = aux+1

