import json 
import requests

class Inegi:
    def __init__(self):
        #Llamado al API
        url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/6bb38c8c-0c38-64aa-3e42-38d896399bd1?type=json'
        # https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1006000039/es/15/false/BISE/2.0/6bb38c8c-0c38-64aa-3e42-38d896399bd1?type=json < accidentes viales
        response= requests.get(url)
        if response.status_code==200:
            content= response.json()
            Series=content['Series'][0]['OBSERVATIONS']     
        #Obtención de la lista de Observations 
        Observations=[]
        for obs in Series:  Observations.append(float(obs['OBS_VALUE']));    
        #Generación del promedio de la lista de Observations 
        sum=0.0
        for i in range(0,len(Observations)): sum=sum+Observations[i];  
        result=sum/len(Observations);
        self.population = Series
        
class Corona:
    def __init__(self):
        url_confirmed='https://api.covid19api.com/live/country/mexico/status/confirmed'
        url_deaths='https://api.covid19api.com/live/country/mexico/status/deaths'
        url_recovered='https://api.covid19api.com/live/country/mexico/status/recovered'
        resp_confirmed=requests.get(url_confirmed)
        resp_deaths=requests.get(url_deaths)
        resp_recovered=requests.get(url_recovered)
        if resp_recovered.status_code==200:
            confirmed=resp_confirmed.json()[1]["Cases"]
            deaths=resp_deaths.json()[1]["Cases"]
            recovered=resp_recovered.json()[1]["Cases"]
            # active = resp_recovered - (deaths+recovered) 
            active = 5 
            self.totals = {'confirmed': confirmed, 'deaths': deaths, 'recovered': recovered, 'active': active }
