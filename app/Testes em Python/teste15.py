from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from tqdm import tqdm
import time

geolocator = Nominatim(user_agent="geolocalização")
#location = geolocator.geocode("RUA JUSCELINO KUBITCHEK, SAO BENTO")
#print((location.latitude, location.longitude))

#LER OS DADOS DA PLANILHA
planilhageo=pd.read_excel(r'F:\projectZeus\app\Testes em Python\CLIENTES.xlsx')

# CONCATENA AS COLUNAS DO ARQUIVO EXECEL
planilhageo['endereco_completo'] = planilhageo['ENDERCOB'] + ',' + \
            planilhageo['MUNICCOB']  + ' - PB'

#CRIAÇÃO DE NOVAS COLUNAS E SETANDO AS INFORMAÇÕES DE GEOLOCALIZAÇÃO
print('INICIANDO GERAÇÃO DE PLANILHA')
with tqdm(total=100) as progresso:
    for i in range(10):
        time.sleep(1)
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        planilhageo['endereco_geolocalizado'] = planilhageo['endereco_completo'].apply(geocode)
        planilhageo['endereco_latitude'] = planilhageo['endereco_geolocalizado'].apply(lambda loc: loc.latitude if loc else None)
        planilhageo['endereco_longitude'] = planilhageo['endereco_geolocalizado'].apply(lambda loc: loc.longitude if loc else None)
        planilhageo['ponto_endereco']=planilhageo['endereco_geolocalizado'].apply(lambda loc: tuple(loc.point) if loc else None)
        progresso.update(10)
#EXPORTA A PLANILHA COM AS INFORMAÇÕES SALVAS
planilhageo['endereco_geolocalizado'].isna().sum()
exportar = pd.DataFrame(planilhageo)
exportar.to_excel(r'F:\projectZeus\app\Testes em Python\novaplanilha.xlsx')

