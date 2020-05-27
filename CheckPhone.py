#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import sys
import urllib
import json

#color
k = '\033[93m'
u = '\033[95m'
n  = '\033[94m'
m = '\033[91m'
h = '\033[92m'
p = '\033[00m'

os.system ('clear')

#banner
os.system('termux-open-url https://www.youtube.com/channel/UCEfhV5UhYgaPuGrddcsDCRg')                      
os.system('toilet Phone --gay')
os.system('toilet Checker --gay')
print (k+'CodedBy @Berdasi')
print (m+'Team : BerdasiCyberTeam')
print (m+'Support : [BL4CKH4T CYBER TEAM')
print (h+'Blogs : berdasi17.blogspot.com')
print
#input number
number = raw_input(p+"Masukan Nomor : ")
print
#data
key = "9810ba5ae4fe74c2930842025d11bc58"
url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=&format=1"
output = requests.get(url)
result = output.text
js = json.loads(result)
#running
country_code = js['country_code']
country_name = js['country_name']
location = js['location']
carrier = js['carrier']
line_type = js['line_type']

os.system('termux-open-url https://berdasi17.blogspot.com/?m=0#')
os.system('clear')
print k+"["+m+"+"+k+"]"  +h+"Hasil Output!!!"
os.system('toilet Hasil --gay')
print k+" [?]" +h+"Phone number: " +str(number)
print k+" [!]" +h+"Country: " +str(country_code)
print k+" [+]" +h+"Country Name: " +str(country_name)
print k+" [!]" +h+"Location: " +str(location)
print k+" [?]" +h+"Carrier: " +str(carrier)
print k+" [+]" +h+"Device: " +str(line_type)
email = raw_input("\033[0;38mEnter To exit ")
os.system('clear')
os.system('toilet DONASI --gay')
print (m+"Coded By Python2.7")
print (u+"Support By Paypal")
print (h+"Donate Paypal")
print (p+"paypal.me/Berdasi")
os.system('xdg-open https://www.paypal.me/Berdasi')
os.system('exit')
