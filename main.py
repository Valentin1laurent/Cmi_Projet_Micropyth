import ssd1306Mod as ssd1306
import machine

try:
    import urequests as requests
except ImportError:
    import requests
import json

i2c = machine.I2C(scl=machine.Pin(2), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c) #creation instance

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        oled.fill(0)
        oled.text('connecting to network...',0,0)
        oled.show()
        wlan.connect('esp211', 'p46029esp211')
        while not wlan.isconnected():
            pass

do_connect()

url="http://api.openweathermap.org/data/2.5/weather?q=Lille,fr&APPID=8bf0f03a173c80a7c71dbf92ca5cf290"
content=requests.get(url)
data=content.json()
t=data['main']['temp']
oled.fill(0)
oled.text('Lille:'+str(t-273.15)+'°C'),0,0)

f=open('cmi.txt')#ouverture image binaire format texte

listline=f.readlines() #lit et stock toutes les lignes du fichier
f.close()

oled.hw_scroll(True)

#oled.invert(True) #True si image a inverser
for j in range(len(listline)):#j est donc le numero de ligne
 compteur=0
 for i in listline[j]:#i est donc le numero de colonne
  if i !='\n':
   if int(i)!=0:
    oled.pixel(compteur,j+20,int(i))
   compteur=compteur+1

oled.show()

