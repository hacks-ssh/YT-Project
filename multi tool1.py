import os
import colorama
from colorama import Fore
import time
import sys
import requests
import json

def lookup():
	global menu
	print(f"""
╦╔═╗  ╦  ┌─┐┌─┐┬┌─┬ ┬┌─┐
║╠═╝  ║  │ ││ │├┴┐│ │├─┘
╩╩    ╩═╝└─┘└─┘┴ ┴└─┘┴  
""")

	ip = input("Enter the ip>")

	geoip = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query")
	data = geoip.json()

	cont = data["continent"]
	continent = data["continentCode"]
	location = data["country"]
	reg = data["region"]
	regionn = data["regionName"]
	cit = data["city"]
	dis = data["district"]
	zipcode = data["zip"]
	latu = data["lat"]
	lonu = data["lon"]
	time = data["timezone"]
	ispn = data["isp"]
	orgn = data["org"]
	prox = data["proxy"]
	host = data["hosting"]

	print(f"Ip Address: {ip}\nContinent: {cont}\nContinent Code: {continent}\nCountry: {location}\nCity: {cit}\nZip Code: {zipcode}\nRegion: {reg}\nRegion Name: {regionn}\nDistrict: {dis}\nLat: {latu}\nLon: {lonu}\nTimezone: {time}\nIsp: {ispn}\nOrg: {orgn}\nProxy: {prox}\nHosting: {host}")

	input()
def menu():
	global onstart
	print(f"""{Fore.RED}
╔╦╗┬ ┬┬ ┌┬┐┬  ╔╦╗┌─┐┌─┐┬  
║║║│ ││  │ │   ║ │ ││ ││  
╩ ╩└─┘┴─┘┴ ┴   ╩ └─┘└─┘┴─┘

[0] EXIT
[1] IP Lookup
""")

	command = input("User1@MultiTool>")

	if command == "0":
		print("Exiting")
		time.sleep(1)
		sys.exit(0)
	elif command == "1":
		os.system("cls && title Youtube Project")
		lookup()

def onstart():
	os.system("cls && title Youtube Project")
	menu()
onstart()
