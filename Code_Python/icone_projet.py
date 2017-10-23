# -*- coding: cp1252 -*-
def icone():
    import requests
    import json
    import urllib
    from PIL import Image
    #Http requests
    url="http://api.openweathermap.org/data/2.5/forecast?id=2998323&appid=315d144374a3f4eca1610c24b0bd5d77"
    r=requests.get(url)
    data=r.json()
    #Temperature et Descritpion
    temp0=int(data['list'][0]['main']['temp']-273)
    desc0=data['list'][0]['weather'][0]['description']
    temp1=int(data['list'][1]['main']['temp']-273)
    desc1=data['list'][1]['weather'][0]['description']
    #Obtention des URL images
    icon0='http://openweathermap.org/img/w/'
    icon1=data['list'][0]['weather'][0]['icon']+'.png'
    icon2=data['list'][1]['weather'][0]['icon']+'.png'
     #Icone
    url1=icon0+icon1
    urllib.urlretrieve(url1,"icon.png")
    ic= Image.open("icon.png")
    #Icone2    
    url2=icon0+icon2
    urllib.urlretrieve(url2,"icon3.png")
    ic= Image.open("icon3.png")
 
    
   
    
    
    


    
