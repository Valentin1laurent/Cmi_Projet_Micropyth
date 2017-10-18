import urequests
import json
import machine
import ssd1306
import network
i2c=machine.I2C(scl=machine.Pin(2), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


try:
    import urequests as requests
except ImportError:
    import requests
import json

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('iPhone de Salma', 'salmajari')


   
url="http://api.openweathermap.org/data/2.5/weather?id=6454414&APPID=315d144374a3f4eca1610c24b0bd5d77"
r=urequests.get(url)
data=r.json()


ville=data["name"]
degre=data["main"]["temp"]-273.15
description=data["weather"][0]["description"]
degree=str(int(degre))

oled.fill(0)
oled.text('City: '+ville, 30, 10)
oled.text('Temp: '+degree, 20, 30)
oled.text(description, 10, 50)
oled.show()


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

