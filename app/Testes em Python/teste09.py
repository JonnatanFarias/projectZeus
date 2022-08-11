import cx_Oracle

conect = cx_Oracle.connect ('farias01/rapadura@//192.168.10.2:1521/WINT.WORLD')


cur = conect.cursor()  
cur.execute('select codveiculo,descricao,placa from pcveicul order by codveiculo')    
res = cur.fetchall()
for r in res:            
    print (r)    
conect.close()


          




           

              














        
