import requests

ip = input("Enter the skids ip: ")

response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query')

data = response.json()

ipaddress = data['query']
continett = data['continent']
countryy = data['country']
zipcode = data['zip']
latt = data['lat']
lonn = data['lon']
ispp = data['isp']
orgg = data['org']
proxyy = data['proxy']
hostingg = data['hosting']

print(f'IP: {ipaddress}\nContinet: {continett}\nCountry: {countryy}\nZip Code: {zipcode}\nLat: {latt}\nLon: {lonn}\nIsp: {ispp}\nOrg: {orgg}\nProxy: {proxyy}\nHosting: {hostingg}')
