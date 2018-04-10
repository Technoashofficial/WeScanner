#!/usr/bin/python
'''
This Tool Is Only Educational Purpose 
It's Your Own Risk 

'''

import os
import sys
from colorama import Fore as F, Back as B, init
from urllib.request import urlopen
from urllib.error import URLError



a = sys.argv[0]
x = []
os.system("clear")
init(autoreset=True)

def catch(url, decoding='utf-8'):
    return urlopen(url).read().decode(decoding)

'''def m():
    print(" \n")
def h():
    print(F.GREEN+" ")
    print(" ")'''


logo = '''
__            __  ______
\/\          /\/()______()
 \/\        /\/ ()___   
  \/\      /\/  ()___()
   \/\/\/\/\/   ()______
    \/_/\_\/    ()______() v 1.0
    	
'''

about = '''
Author       : 3P1C
Team         : SkyKnight
Email        : EPIC.SkyKnight@gmail.com
'''
about2 = '''
Tools Name    : WEScanner
Version       : 1.0
Script In     : Python3
Created Date  : 03/04/2018
Where Is Tool : '''+a
print(F.YELLOW+ logo)
print(F.RED+ about)
print(F.GREEN+ about2)
print("-x----------------------------------x-")
print(" ")
url = input(F.GREEN+"Website"+F.YELLOW+" & "+F.CYAN+"Ip >> " )
os.system("clear")
print(F.GREEN+ logo)
print(F.CYAN+ about2)
print(" ")
print(F.MAGENTA+"           ["+url+"]    ")
print(" ")
def whois():
    print(B.YELLOW+" Whois Lookup ","\n")
    print(F.GREEN+catch("http://api.hackertarget.com/whois/?q="+url))
    print(" ")
def http():
    print(B.YELLOW+" HTTP Header Check ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/httpheaders/?q="+url))
    print(" ")
def usr():
    init(autoreset=False)
    print(B.YELLOW+" User Agent ","\n")
    print(F.GREEN+" ")
    os.system("nmap -p80 --script http-useragent-tester.nse "+url)
    init(autoreset=True)
    print(" ")
def zone():
    print(B.YELLOW+" ZoneTransfer ","\n")
    print(F.GREEN+catch("http://api.hackertarget.com/zonetransfer/?q="+url))
    print(" ")
def trace():
    print(B.YELLOW+" Traceroute ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/mtr/?q="+url))
    print(" ")
def ping():
    print(B.YELLOW+" Ping Test ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/nping/?q="+url))
    print(" ")
def dns():
    print(B.YELLOW+" DNS Lookup ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/dnslookup/?q="+url))
    print(" ")
def rdns():
    print(B.YELLOW+" Reverse DNS Lookup ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/reversedns/?q="+url))
    print(" ")
def finda():
    print(B.YELLOW+" Find (A) Records ","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/hostsearch/?q="+url))
    print(" ")
def page():
    print(B.YELLOW+" Page Links","\n")
    print(F.GREEN+catch("https://api.hackertarget.com/pagelinks/?q="+url))
def mobile():
    print(B.YELLOW+" Mobile Version Website"," \n")
    os.system("nmap -p80 --script http-mobileversion-checker.nse "+url)
    print(" ")
def robot():
    print(B.YELLOW+" Robots.txt Scanner "," \n")
    print(catch("http://"+url+"/robots.txt"))
    print(" ")
'''def sitemap():
    print(B.YELLOW+" Sitemap "," \n")
    site = catch("http://"+url+"/sitemap.xml")
    if site in "sitemap":
        print(site)
    else:
        print("Sitemap Not Found")'''
    
whois()
http()
usr()
robot()
#sitemap()
zone()
trace()
ping()
dns()
rdns()
finda()
page()
mobile()
print(F.MAGENTA+"Thanks For Using Me :) \n\t\t\tGood Bye Dear.")
print(F.RED+" ANY ERROR PLEASE CONTACT ME :-", F.GREEN+"epic.skyknight@gmail.com")
sys.exit()

