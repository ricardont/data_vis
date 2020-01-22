import json 
import requests

class Inegi:
    def __init__(self):
        #Llamado al API
        url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/6bb38c8c-0c38-64aa-3e42-38d896399bd1?type=json'
        response= requests.get(url)
        if response.status_code==200:
            content= response.json()
            Series=content['Series'][0]['OBSERVATIONS']     
        #Obtención de la lista de observaciones 
        Observaciones=[]
        for obs in Series:  Observaciones.append(float(obs['OBS_VALUE']));    
        #Generación del promedio de la lista de observaciones 
        sum=0.0
        for i in range(0,len(Observaciones)): sum=sum+Observaciones[i];  
        resultado=sum/len(Observaciones);
        self.poblacion = Series