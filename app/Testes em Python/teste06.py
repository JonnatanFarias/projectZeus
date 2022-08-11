import pandas as pd

venda = {'data':['15/02/2021','16/02/2021'],
          'valor':[500,300],
          'produto':['feijão','arroz'],
          'qtde':[50,60]}
venda_df =pd.DataFrame(venda)

print('Sistema de mensagens whatsapp do cpd')
print(venda_df)

