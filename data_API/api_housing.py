import requests
import json
from time import sleep

class housing:
		
	def house(city,varr):
		# url = "https://cities-cost-of-living-and-average-prices-api.p.rapidapi.com/cost_of_living"

		# querystring = {"country":"united-states","city":city+'-'+postal}

		# headers = {
		# 	"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
		# 	"X-RapidAPI-Host": "cities-cost-of-living-and-average-prices-api.p.rapidapi.com"
		# }

		# response = requests.request("GET", url, headers=headers, params=querystring)
		# response = response.json()
		

		url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"

		querystring = {"city_name":f"{city}","country_name":"united states"}
		# key1= '74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea'
		# key2 = '0f836e441fmshf4cdccc8232af9cp1e5fedjsn9a65410fcd80'
		# key3 = '3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0'
		headers = {
			"content-type": "application/octet-stream",
			"X-RapidAPI-Key": varr,
			"X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)

		response = response.json()


		return response
	with open('crimes.json','r') as myfile:
		data = json.load(myfile)
	
	
	lst1,lst2,lst3,lst4,lst5,lst6,lst7 =[],[],[],[],[],[],[]
	
	for i in range(58,62):
		try:
			val=house(data[i]['city name'],'3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0')
			print(i)
			
			lst1.append(val['prices'][26]['avg'])
			lst2.append(val['prices'][35]['avg'])
			lst3.append(val['prices'][49]['avg'])
			lst4.append(val['prices'][51]['avg'])
			lst5.append(val['prices'][42]['avg'])
			lst6.append(val['prices'][48]['avg'])
			lst7.append(data[i]['city name'])
			sleep(0.3) 
		except:
			print('key error')
			continue

	final_list = []
	for i in range(len(lst1)):
		fin=[lst7[i],lst1[i],lst2[i],lst3[i],lst4[i],lst5[i],lst6[i]]
		final_list.append(fin)


	dictt = {'data':final_list}
	final = {
		'city':lst7,
		'One bedroom apartment in city centre':lst1,
		'Meal in Inexpensive Restaurant':lst2,
		'Internet, 60 Mbps or More':lst3,
		'Dress in a Chain Store':lst4,
		'One-way Ticket, Local Transport':lst5,
		'Basic utilities':lst6

	}
	print(dictt)
	with open("housing_list3.json", 'w') as myfile:
                myfile.write(json.dumps(dictt,indent = 4))
		
	
	# lst1,lst2,lst3,lst4,lst5,lst6,lst7 =[],[],[],[],[],[],[]
	# print(len(data))
	# for i in range(10,20):
	# 	val=house(data[i]['city name'],'3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0')
	# 	print(i)
	# 	lst1.append(val['prices'][26]['avg'])
	# 	lst2.append(val['prices'][35]['avg'])
	# 	lst3.append(val['prices'][49]['avg'])
	# 	lst4.append(val['prices'][51]['avg'])
	# 	lst5.append(val['prices'][42]['avg'])
	# 	lst6.append(val['prices'][48]['avg'])
	# 	lst7.append(data[i]['city name'])

	# for i in range(len(lst1)):
	# 	fin=[lst1[i],lst2[i],lst3[i],lst4[i],lst5[i],lst6[i]]
	# 	final_list.append(fin)


		

