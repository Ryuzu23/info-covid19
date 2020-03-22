import json
import requests

print ('# Corona Virus Information is based on the Python Programming Language')
print ('# Created by Ari Ardana')
print ('# Contact Me: https://facebook.com/arie.ganz.96\n')

api = 'https://covid19.mathdro.id/api/countries/'
last = 'https://covid19.mathdro.id/api'

negara = (input('Cari negara/''Search Country'': '))

url = api + negara
json_data = requests.get(url).json()
last_data = requests.get(last).json()

last_update = last_data['lastUpdate']
print ('\nLast Update: ' + str(last_update))

confirmed = json_data['confirmed']['value']
print ('\nTerkonfirmasi/Confirmated: ' + str(confirmed))

recovered = json_data['recovered']['value']
print ('Sembuh/Recovered: ' + str(recovered))

death = json_data['deaths']['value']
print ('Meninggal/Deaths: ' + str(death))
