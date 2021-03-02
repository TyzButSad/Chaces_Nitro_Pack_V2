#!/usr/bin/env python

import random
import requests
import string
import os
import time
import threading
from fake_useragent import UserAgent


# By Tyz
# Discord : Tyz#9999
# 2019

RED     =  "\033[1;31m"
BLUE    =  "\033[1;34m"
CYAN    =  "\033[1;36m"
GREEN   =  "\033[0;32m"
RESET   =  "\033[0;0m"
BOLD    =  "\033[;1m"
REVERSE =  "\033[;7m"
YELLOW  =  "\033[33m"
HEADER  =  "\033[95m"

invalid = YELLOW + "Invalid" + RESET
valid = GREEN + "Valid" + RESET
error = RED + "Error" + RESET
denied = CYAN + "Denied" + RESET

ua = UserAgent()

headers = {
    'User-Agent' : ua.random,
    'Content_Type' : 'multipart/form-data',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}


def Nitrx(code, headers, proxy, g, b, s):
    url = "https://discordapp.com/api/v6/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true".format(code)
    gencode = code
    code = HEADER+code+RESET
    try:
        rr = s.get(url, headers=headers, proxies=proxy)
        if "Unknown Gift Code" in rr.text:
            print(code+"          "+invalide)
            b.write(gencode+"\n")
        elif "subscription_plan" in rr.text:
            print(code+"          "+valid)
            g.write(gencode+"\n")
        elif "You are being rate limited" in rr.text:
            print(code+"          "+error+"          Limited")
        elif "Access denied" in rr.text:
            print(code+"          "+denied)
        else:
            print(code+"          "+error+"          SSL")
    except requests.exceptions.ProxyError:
        print(code+"          "+error+"          Proxies")
        return
    except requests.exceptions.SSLError:
        pass
    except requests.exceptions.ConnectionError:
        print(code+"          "+error+"          Network")
    g.close()
    b.close()

def uslist():
    file = input("     [?] Nom Du Fichier: ")
    if os.path.isfile(file):
        pass
    else:
        exit(RED+"     [?] Fichier Invalide")
    p = open(file, "r")
    lines = p.readlines()
    p = open("proxy.txt", "r")
    ips = p.readlines()
    for i in lines:
        code = i.strip()
        g = open('gods.txt', 'a')
        b = open('bads.txt', 'a')
        s = requests.session()
        ip = random.choice(ips)
        ip = str(ip).replace('\n', '')
        hts = "https://"+ip
        ht = "http://"+ip
        proxy = {
            "https":hts,
            "http":ht
        }
        headers['User-Agent'] = ua.random
        time.sleep(0.01)
        x = threading.Thread(target=Nitrx, args=(code, headers, proxy, g, b, s,))
        x.start()


def Generator():
    file = open('Nitro Codes.txt', 'a')
    try:
        amount = int(input("     [?] Quantité de codes : "))
        cln = int(input("     [?] Nombre De Caractères: "))
    except:
        exit("     [? Invalid input]")
    fix = 1
    while fix <= amount:
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=cln))
        print(code)
        fix += 1
        file.write(code+"\n")
    file.close()
    exit(BLUE+"     [+] Create By Tyz")


def auto():
    p = open("proxy.txt", "r")
    lines = p.readlines()
    amount = int(input("     [?] Quantité De Codes: "))
    cln = int(input("     [?] Taille Du Code: "))
    fix = 1
    print(GREEN+"     [?] Table info : Code - Status - Type\n")
    while fix <= amount:
        g = open('gods.txt', 'a')
        b = open('bads.txt', 'a')
        s = requests.session()
        ip = random.choice(lines)
        ip = str(ip).replace('\n', '')
        hts = "https://"+ip
        ht = "http://"+ip
        proxy = {
            "https":hts,
            "http":ht
        }
        headers['User-Agent'] = ua.random
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=cln))
        a = open("bads.txt", "r")
        time.sleep(0.001)

        if code in a.read():
            pass
        else:
            fix += 1
            x = threading.Thread(target=Nitrx, args=(code, headers, proxy, g, b, s,))
            x.start()


if __name__ == "__main__":
    msg = """
    {}
████████      █     █      ███████
   ██          █   █             █
   ██            █             █
   ██            █           █
   ██            █         █
   ██            █         ██████\n
                {}Create By {}Tyz\n

        1{}- {}[{}Auto{}]{} Generator Et Scan
        {}2{}- {}Check Les Nitro {}[{}LIST{}]
        {}3{}- {}Juste Les Nitro {}[{}Generator{}]{}\n

    """.format(HEADER,YELLOW,RED,GREEN,YELLOW,BOLD,
        YELLOW,BLUE,RED,GREEN,BLUE,YELLOW,BOLD,YELLOW,RED,
        GREEN,BLUE,YELLOW,BOLD,YELLOW,RESET)

    for i in msg:
        time.sleep(0.005)
        print(i, end='')
    try:
        opi = int(input("\n     " + RED + "[?] Choisi: "+GREEN))
    except:
        exit('     [?] Option Invalide..')
    if opi == 1:
        auto()
    elif opi == 2:
        uslist()
    elif opi == 3:
        Generator()
    else:
        exit('     [?] Option Invalide..')
