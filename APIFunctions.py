import json
import requests
import APIFunctions
import pprint 
import random 

#--- api url , key, and specific request TEST---
api_url = ("https://www.thecocktaildb.com/api/json/v2/9973533/")
request = ("search.php?s=gin")

# --- just print url and response code --- 
#print(api_url+request)
#response = requests.get(api_url+request)

# Json attributes and store dict in data
"""
print(response.status_code)
print ("cotent type:" + response.headers['content-type'])
data = response.json()
print(type(data))

# iterate through dictionary (based on gin drinks) and printing out certain keys 

i = 0 
for drink in data['drinks']:
	print(data["drinks"][i]["idDrink"])
	print(data["drinks"][i]["strDrink"])
	print(data["drinks"][i]["strCategory"])
	print(data["drinks"][i]["strAlcoholic"])
	print(data["drinks"][i]["strGlass"])
	print(data["drinks"][i]["strInstructions"])
	print(data["drinks"][i]["strDrinkThumb"])
	print("")
	i = i + 1
"""
# --- FUNCTION : format JSON data to view ONLY --- 
def jprint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

#jprint(response.json())

#------------------------------------------------------

# --- Alcoholic or non alchoholic function --- 
def alcoholic(ans):
	#ans = ans.casefold()
	if ans == "no":
		#Alcoholic_dict = {}
		request = ("filter.php?a=Non_Alcoholic")
		response = requests.get(api_url+request)
		data = response.json()
		return data
		#i = 0
		#for drink in data['drinks']:
			#Alcoholic_dict[data["drinks"][i]["idDrink"]] = data["drinks"][i]["strDrink"]
			#i = i + 1
		#print(Alcoholic_dict)
	else: 
		#Alcoholic_dict = {}
		request = ("filter.php?a=Alcoholic")
		response = requests.get(api_url+request)
		data = response.json()
		return data
		#i = 0
		#for drink in data['drinks']:
			#Alcoholic_dict[data["drinks"][i]["idDrink"]] = data["drinks"][i]["strDrink"]
			#i = i + 1
		#print(Alcoholic_dict)

# --- Category function --- 
def category(ans, ans2):
	drink_counter = 0
	#category_dict = {}
	#request_id = ans2 
	#request = ("lookup.php?i="+request_id)
	category_data = alcoholic(ans)
	#category_response = requests.get(api_url+request)
	for drink in category_data["drinks"]:
		request_id = category_data["drinks"][drink_counter]["idDrink"]
		request = ("lookup.php?i="+request_id)
		category_response = requests.get(api_url+request)
		category_response_data = category_response.json()
		#print(category_response_data)
		#print(request_id)
		#print(request)
		if category_response_data['drinks'][drink_counter - 1]["strCategory"] == ans2:
			del category_response_data['drinks'][drink_counter]
			print("matches")
		drink_counter += 1
	print(category_response_data)
	
		#category_dict[category_data["drinks"][drink_counter]["idDrink"]] = category_data["drinks"][drink_counter]["strDrink"]
		#x = x + 1 

	#print(category_dict)

	'''
	request = ("filter.php?c="+ans)
	response = requests.get(api_url+request)
	data = response.json()
	i = 0
	for drink in data['drinks']:
		print(data["drinks"][i]["idDrink"])
		print(data["drinks"][i]["strDrink"])
		print(data["drinks"][i]["strDrinkThumb"])
		print("")
		i = i + 1
		'''

"""
	elif ans == "cocktail":
		request = ("filter.php?c=Cocktail")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	elif ans == "Milk / Float / Shake":
		request = ("filter.php?c=Milk_/_Float_/_Shake")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	elif ans == "Other / Unknown":
		request = ("filter.php?c=Other_/_Unknown")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	elif ans == "Cocoa":
		request = ("filter.php?c=Cocoa")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	elif ans == "Shot":
		request = ("filter.php?c=Milk_/_Float_/_Shake")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	elif ans == "Coffee / Tea":
		request = ("filter.php?c=Coffee_/_Tea")
		response = requests.get(api_urlkey+request)
		json_data = json.loads(response.content)
		print(json_data)
	else:
		print("End of it")

"""
def popular_drinks():
	reqeuest = ("popular.php")
	response = requests.get(api_url+request)
	popular_drinks_selection = response.json()
	return popular_drinks_selection

# --- Yelp API --- 

yelp_key = "bc6utOfTROBnI9OqigAJDY5Kh0nY7K5y3h5TCMWCobHpq0DZZVTj1QsdMw0ZTgZikrk3sutTE5waspolZnH-YoCJWuut0J_Sagvf3ZPbABUxmWDmnJiZ4tMpQBh5XXYx"
headers = {'Authorization': 'Bearer %s' % yelp_key}
yelp_url='https://api.yelp.com/v3/businesses/search'

def planmynight(zip):
	# random bar based on zipcode
	random_bar_counter = 0 
	random_drink_counter = 0 
	params = {'term':'bar','location' : zip}
	req = requests.get(yelp_url, params=params, headers=headers)
	yelp_data = json.loads(req.content)
	while random_bar_counter <= 5:
		random_bar = random.choice(yelp_data['businesses'])
		#return random_bar
		pprint.pprint(random_bar)
		random_bar_counter += 1 
	# random drink 
	request = ("random.php")
	response = requests.get(api_url+request)
	while random_drink_counter <= 5:
		random_drink = response.json()
		pprint.pprint(random_drink)
		#return random_drink
		random_drink_counter += 1
	#pprint.pprint(random_bar)