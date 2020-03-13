import json
from urllib.request import urlopen

#Making sure entered choice is integer.
while True:
    try:
        choice = input("1. Info on own IP\n2. Info about other IP\n")
        break
    except ValueError:
        print("Please enter an integer!")

#Modifying URL as well as the text to be printed as per requirement.
if int(choice) == 1:
    url = 'http://ipinfo.io/json'
    printDetails = '\nYour IP details'
elif int(choice) == 2:
    userIP = input("Enter IP: ")
    url = 'http://ipinfo.io/' + userIP + '/json'
    printDetails = '\nEntered IP details'

#Getting HTTPResponse in bytes.
response = urlopen(url)
#Converting bytes to string and decoding as per utf-8 standard.
str_response = response.readall().decode('utf-8')
#Finally able to use string response to load data into my variable.
data = json.loads(str_response)

#Storing values from each key into variables. Need to apply Exception for KeyError, because host name is not a key that is always present.
IP = data['ip']
try:
    hostName = data['hostname'] #Does not work for all IP addresses
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']

    print(printDetails)
    print('IP: {4} \nHost Name: {5} \nRegion: {1} \nCountry: {2} \nCity: {3} \nOrg: {0}'.format(org, region, country, city, IP, hostName))
except KeyError:
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']

    print(printDetails)
    print('IP: {4} \nRegion: {1} \nCountry: {2} \nCity: {3} \nOrg: {0}'.format(org, region, country, city, IP))
