# \ Coded by Volt#1672 /

import requests
import threading
import random
import string
import sys

def randchar(num):
       return ''.join(random.choice(string.ascii_letters) for x in range(num))

if len(sys.argv)<2:
  print("\nWrong usage! Usage: python3 " + sys.argv[0] + " <threads> <request rate>\n")
  exit()

threads = sys.argv[1]
reqrate = sys.argv[2]

def det():

  if int(threads)<1:
    print("\nNo Threads specified! Specify more than 1.\n")
    exit()
  
  elif int(reqrate)<1:
    print("\nNo Request rate specified! Specify more than 1.\n")
    exit()

  if int(threads) and int(reqrate)>0:
    start()


def attack(): # Main scraping
  while True:
   sessyes = requests.Session()
   for _ in range(int(reqrate)): # Requests rate, higher = faster scraping, lower = slower scraping
     try:
      url = "https://i.imgur.com/" + (randchar(7)) + ".png"
      req = sessyes.get(url, timeout=8)
      if not "https://i.imgur.com/removed.png" in (req.request.url):
        with open("imgur.txt","a") as img:
          img.write(str(url) + "\n")
          img.close()
        print("\nFound!\nURL: " + str(url) + "\n")
     except:
       pass

def start():
  print("\n\ Coded by Volt#1672 /")
  print("\nStarting, this might take a while...")
  for _ in range(int(threads)):
    threading.Thread(target=attack).start()

det()
