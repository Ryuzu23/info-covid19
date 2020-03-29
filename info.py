
import json, requests, os

print ('#############################################')
print ('#             Author : Ari Ardana           #')
print ('#              Info COVID-19 V2             #')
print ('#          ariardana192@gmail.com           #')
print ('#        https://github.com/Ryuzu23         #')
print ('#############################################\n')
print ('API Source : https://kawalcorona.com/api\n')

#Jumlah Positif Global
positif_global = 'https://api.kawalcorona.com/positif'
respon = requests.get(positif_global).json()
oi = respon['value']
print ('Total Positif Global   : ' + str(oi))

#Jumlah Sembuh Global
sembuh_global = 'https://api.kawalcorona.com/sembuh'
respon = requests.get(sembuh_global).json()
oi = respon['value']
print ('Total Sembuh Global    : ' + str(oi))

#Jumlah Meninggal Global
meninggal_global = 'https://api.kawalcorona.com/meninggal'
respon = requests.get(meninggal_global).json()
oi = respon['value']
print ('Total Meninggal Global : ' + str(oi))

def tampil(data,Provinsi=False,world=False):
	if Provinsi:
		print ('[*] Provinsi : ' + data["attributes"]["Provinsi"])
		print ('[*] Positif : ' + str(data["attributes"]["Kasus_Posi"]))
		print ('[*] Sembuh : ' + str(data["attributes"]["Kasus_Semb"]))
		print ('[*] Meninggal : ' + str(data["attributes"]["Kasus_Meni"]))
		print ('-'*30)
	if world:
		print ('[*] Negara : ' + data['attributes']['Country_Region'])
		print ('[*] Last Update : ' + str(data['attributes']['Last_Update']))
		print ('[*] Terkonfirmasi : ' + str(data['attributes']['Confirmed']))
		print ('[*] Positif : ' + str(data['attributes']['Active']))
		print ('[*] Sembuh : ' + str(data['attributes']['Recovered']))
		print ('[*] Meninggal : ' + str(data['attributes']['Deaths']))
		print ('-'*30)
#Menu
print ('\n1. Data COVID-19 di Provinsi Indonesia')
print ('2. Data COVID-19 Global')
print ('3. Keluar')
pilih = input('Pilih Opsi >>> ')



if pilih == '1':
	prov = 'https://api.kawalcorona.com/indonesia/provinsi/'
	data = requests.get(prov).json()
	for x in data:
		tampil(x,Provinsi=True)

elif pilih == '2':
	data_global = 'https://api.kawalcorona.com'
	data = requests.get(data_global).json()
	for x in data:
		tampil(x,world=True)
	
elif pilih == '3':
	exit()
else:
	exit('Input Salah!')
