
import json, requests

print ('#############################################')
print ('#              Info COVID-19 V2             #')
print ('#            Author : Ari Ardana            #')
print ('#     https://facebook.com/arie.ganz.96     #')
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

#Menu
print ('\n1. Data COVID-19 di Provinsi Indonesia')
print ('2. Data COVID-19 Global')
print ('3. Keluar')
pilih = input('Pilih Opsi >>> ')



if pilih == '1':
	prov = 'https://api.kawalcorona.com/indonesia/provinsi/'
	respon = requests.get(prov).json()
	data_prov = respon['attributes'][0]['Provinsi']
	print ('\n[*] Provinsi : ' + (data_prov))
	data_pos = respon['attributes'][0]['Kasus_Posi']
	print ('[*] Positif    : ' + str(data_pos))
	data_sem = respon['attributes'][0]['Kasus_Semb']
	print ('[*] Sembuh     : ' + str(data_sem))
	data_men = respon['attributes'][0]['Kasus_Meni']
	print ('[*] Meninggal  : ' + str(data_men))
	print ('-'*30)
elif pilih == '2':
	data_global = 'https://api.kawalcorona.com'
	respon = requests.get(data_global).json()
	data_neg = respon['attributes'][0]['Last_Update']
	print ('Negara : ' + str(data_neg))
	global_con = respon['attributes'][0]['Confirmed']
	print ('Terkonfirmasi : ' + str(global_con))
	global_pos = respon['atrributes'][0]['Active']
	print ('Positif : ' + str(global_pos))
	global_sem = respon['attributes'][0]['Recovered']
	print ('Sembuh : ' + str(global_sem))
	global_men = respon['attributes'][0]['Deaths']
	print ('Meninggal : ' + str(global_men))
	print ('-'*30)
elif pilih == '3':
	exit()
else:
	print ('Input Salah!')
	exit()

