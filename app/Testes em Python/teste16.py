from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from tqdm import tqdm
import time

geolocator = Nominatim(user_agent="geolocalização")
#location = geolocator.geocode("RUA JUSCELINO KUBITCHEK, SAO BENTO")
#print((location.latitude, location.longitude))

#LER OS DADOS DA PLANILHA
planilhageo=pd.read_excel(r'app\Testes em Python\novaplanilha.xlsx')
     
#EXPORTA A PLANILHA COM AS INFORMAÇÕES SALVAS
print(planilhageo['endereco_geolocalizado'].isna().sum())

