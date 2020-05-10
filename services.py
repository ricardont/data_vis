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
        url='https://api.covid19api.com/summary'
        types_tot = [{'type_src': 'TotalConfirmed', 'type': 'confirmed', 'cases': 9999, "color":"orange",  "new":0},
                     {'type_src': 'NewConfirmed',   'type': 'confirmed_new', 'cases': 9999, "color":"orange" , "new":1},
                     {'type_src': 'TotalRecovered', 'type': 'recovered', 'cases': 9999, "color":"green"  , "new":0},
                     {'type_src': 'NewRecovered',   'type': 'recovered_new', 'cases': 9999, "color":"green"  , "new":1},
                     {'type_src': 'TotalDeaths',    'type': 'deaths', 'cases': 9999, "color":"red"    , "new":0},
                     {'type_src': 'NewDeaths',      'type': 'deaths_new', 'cases': 9999, "color":"red"    , "new":1}]
        call=requests.get(url)
        if call.status_code==200:
            cases_mx=call.json()["Countries"][108]
            for i in range(len(types_tot)):
                types_tot[i]["cases"] = cases_mx[types_tot[i]["type_src"]]
        self.totals = types_tot
