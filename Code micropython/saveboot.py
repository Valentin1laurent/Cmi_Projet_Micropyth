import ssd1306
import machine

i2c = machine.I2C(scl=machine.Pin(2), sda=machine.Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c) #creation instance

f=open('lille1.txt')#ouverture image binaire format texte

listline=f.readlines() #lit et stock toutes les lignes du fichier
f.close()

oled.fill(0)
#oled.invert(True) #True si image a inverser
for j in range(len(listline)):#j est donc le numero de ligne
 compteur=0
 for i in listline[j]:#i est donc le numero de colonne
  if i !='\n':
   if int(i)!=0:
    oled.pixel(compteur,j+10,int(i))
   compteur=compteur+1
oled.show()
