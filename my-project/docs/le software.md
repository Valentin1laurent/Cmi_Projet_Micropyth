#Codage et informatique lie au projet

Ici nous detaillerons les differents codes que nous avons developpes pour la realisation du projet.


##Librairies utilises avec PYTHON

###Utilisation de Requests

	>>>> import requests

	>>> url="..."

	>>> r=requests.get(url) 

Ces quelques lignes de codes permettent de recuperer les donnees d'une page web.
Il suffit de remplacer le trou laisser dans la variable URL pour notifier la page web ou l'on souhaite recuperer les informations.


	>>> import requests

	>>> url="https://www.wikipedia.org/"

	>>> r=requests.get(url)

	>>>print(r) 

L'exemple au dessus permet de charger les informations de la page d'acceuil de WIKIPEDIA.

###Utilisation d'une API 
Pour notre projet nous avons besoin de recuperer des donnees sur la meteo a des endroits precis du globe,
pour cela nous nous sommes tournes vers le site:  


OPENWEATHERMAP.ORG  



	>http://api.openweathermap.org/data/2.5/forecast?id={ID}&APPID={APIKEY}

La ligne de code precedente permet de recuperer les donnees meteorologique sur le site a l'aide d'une API.Pour pouvoir utiliser celle ci nous nous sommes
inscrits sur le site et nous avons recu une APIKEY. Cette APIKEY nous permet d'obtenir les donnees meteorologiques legalement pour permettre le bon fonctionnement de notre projet.


###Utilisation du format json 

Les donnees sous le format JSON apparaissent sous la forme d'un dictionnaire.
On sait qu'un dictionnaire marche grace a la combinaison d'un 'id' et d'une 'cle'.
On peut donc extraire la donnee souhaitee si l'on connait les 'liens' propre a ce dictionnaire.
Voici un petit exemple qui montre comment marche un dictionnaire.

	>>>mon_dictionnaires={'mot de passe': '*', 'pseudo': '6pri1'}

	>>>mon_dictionnaire['mot de passe']

	>>>'*'

	>>>mon_dictionnaire['pseudo']

	>>>'6pri1' 


Devant la simplicite d'utilisation du format JSON nous avons decide d'incorporer dans notre code la fonction JSON
qui permettra de crer une arborescence plus simple des donnees et qui nous facilitera l'acces a celles-ci.

Le code va de nouveau se modifier pour devenir:

	>>>> import requests

	>>>import json

	>>> url="http://api.openweathermap.org/data/2.5/forecast?id={ID}&appid={APIKEY}"

	>>> r=requests.get(url)

	>>>data=r.json()

##Algorithme de recuperation des donnees meteorologiques

###Recuperation de la temperature et de la description du temps
Dans un fichier texte sur le site OPENWEATHERMAP il est possible de connaitre l'arborescence des differents dictionnaires
Nous avons donc pu deduire les 2 prochaines lignes de code:
	
	>>>temp0=int(data['list'][0]['main']['temp']-273)  (donne la temperature)

	>>>desc0=data['list'][0]['weather'][0]['description'] (donne la description du temp)


###Comment avoir les donnees de la ville de LILLE
Maintenant que nous savons comment recuperer les differentes donnees il faut que l'on trouve un moyen pour n'obtenir que les donnees pour la ville de lille.
Reprenons l'url qui nous permet d'acceder aux donnees:

	
	>>>http://api.openweathermap.org/data/2.5/forecast?id={ID}&appid={APIKEY}

On remarque que deux donnees sont a rentrer,nous avons deja aborder la premiere qui est APIKEY.  
La seconde represente un code rattacher a une ville.Le lien entre les villes et leur code est fournis par le site 
OPENWEATHERMAP via un fichier texte qui regroupe toute les ville et leur ID. 

Apres quelque recherche Il s'avere que l'ID par laquel la ville de Lille est repertorier est : 2998323.  

On obtient donc l'url finale :
	
	>>>>http://api.openweathermap.org/data/2.5/forecast?id=2998323&appid={APIKEY}

##Utilisation de micropython

Pour coder sur le microcontroleur nous avons importer le langage 'Micropython'.C'est un langage simplifier de python:
il ne contient pas toutes les librairies disponibles sur python mais il permet de retrouver quelque librairie de base. Ce langage est surtout utilise pour 
coder des microcontroleurs.
## Comment 'flasher' l'ESP8266 et installer micropython

Pour flasher le microcontroleur il faut mettre la borne GPIO0 a la masse.
A partir de PIP il faut installer ESPTOOL.py
En tapant la commande: 
	>>>>pip install esptool
grace a esptool.py on peux effacer ce qui etait jusqu'a present sur l'esp en
tapant la commande:

 
	>>>>esptool.py --port /dev/ttyUSB0 erase_flash
Pour installer le nouveau firmware on tape la commande:


	>>>>esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
###Librairies utiles a notre projet

	>>>>import urequests
	>>>>import json
	>>>>import machine
	>>>>import ssd1306
	>>>>import network

-Urequest: elle possede le meme fonctionnement que la librairie request de python,c'est a dire
qu'elle est utile lors de la recherche d'url.

-Json: il possede le meme fonctionnement qu'en python , c'est a dire qu'il va creer un dictionnaire de liste.

-Machine:cette librairie servira dans la plupart des cas a connecter l'ecran avec la librairie propre
a l'ecran SSD1306.

-Network:cette librairie sera utilisee pour connecter l'esp par wi-fi a internet.


###Connectique et affichage.

Dans un premier temps nous voulions recuperer les donnees meteorologique en ligne il etait essentiel de connecter l'esp a internet.
Nous avons utiliser la librairie NETWORK importer precedemment et nous avons obtenu le code suivant:


	>>>>sta_if=network.WLAN(network.STA_IF)
	>>>>sta_if.active(True)
	>>>>sta_if.connect('<username>','<password>')

Ce code permet de connecter notre esp a un reseau sans fil.Pour cela il faut remplacer 
la variable 'username' par le nom du reseau et la variable 'password' par le mot de passe du reseau. 


Dans un second temps pour pouvoir afficher les donnees issue d'internet sur un ecran il faut creer une variable 
pour l'ecran et le configurer sur le microcontroleur:

	>>>>i2c=machine.I2C(sc1=machine.pin(2), sda=machine.Pin(0))
	>>>>oled= ssd1306.SSD1306_I2C(128, 64, i2c)

###Recuperation des donnees en micropython.

Les lignes de code suivantes permettent d'executer le meme programme qu'en python:
C'est a dire qu'on va recuperer l'API donc l'URL du site  et ensuite  mettre les donnees en format json.


	>>>>url="http://api.openweathermap.org/data/2.5/weather?id6454414&APPID={APIKEY}
	>>>>r=urequest.get(url)
	>>>>data=r.json()
	>>>>ville=data["name"]
	>>>>degre=data["main"]["temp"]-273.15
	>>>>description=data["weather"][0]["description"]
	>>>>degree=str(int(degre))

Comme dans le code python on identifie les informations que l'on a besoin d'afficher a l'aide des proprietes d'un dictionnaire.
On identifie donc le nom de la ville ,la temperature en degres et la decription du temps.

###Affichage des informations

Il ne nous reste plus qu'a afficher les informations precedemment obtenues sur l'ecran:

	>>>>oled.fill(0)
	>>>>oled.show()
	>>>>oled.text('City: '+ville, 30, 10)
	>>>>oled.text('Temp: '+degree, 20, 30)
	>>>>oled.text(description, 10, 50)
	>>>>oled.show()


On commence par faire un 'clear'(on supprime les informations precedemment afficher au cas ou
elle serait encore afficher) ensuite on ecrit ce que l'on veut a l'aide de la commande "text"
et enfin on les affiches a l'aide de la fonction oled.show()


#CODE PYTHON

Voici le code PYTHON en un seul bloc:

	>>>import requests
	>>>import json
	>>>#Http requests
	>>>url="http://api.openweathermap.org/data/2.5/forecast?id=2998323&appid={APIKEY}"
	>>>r=requests.get(url)
	>>>data=r.json()
	>>>#Temperature et Descritpion
	>>>temp0=int(data['list'][0]['main']['temp']-273)
	>>>desc0=data['list'][0]['weather'][0]['description']
	>>>temp1=int(data['list'][1]['main']['temp']-273)
	>>>desc1=data['list'][1]['weather'][0]['description']

 
Il permet de recuperer les donnes meteorologiques immediate et les previsions pour 3 heures.

#CODE MICROPYTHON

Voici le code MICROPYTHON en un seul bloc:

	>>>>import urequests
	>>>>import json
	>>>>import machine
	>>>>import ssd1306
	>>>>import network
	>>>>sta_if=network.WLAN(network.STA_IF)
	>>>>sta_if.active(True)
	>>>>sta_if.connect('<username>','<password>')
	>>>>i2c=machine.I2C(sc1=machine.pin(2), sda=machine.Pin(0))
	>>>>oled= ssd1306.SSD1306_I2C(128, 64, i2c)
	>>>>url="http://api.openweathermap.org/data/2.5/weather?id6454414&APPID={APIKEY}"
	>>>>r=urequest.get(url)
	>>>>data=r.json()
	>>>>ville=data["name"]
	>>>>degre=data["main"]["temp"]-273.15
	>>>>description=data["weather"][0]["description"]
	>>>>degree=str(int(degre))
	>>>>oled.fill(0)
	>>>>oled.show()
	>>>>oled.text('City: '+ville, 30, 10)
	>>>>oled.text('Temp: '+degree, 20, 30)
	>>>>oled.text(description, 10, 50)
	>>>>oled.show()

Apres avoir flasher le microcontroleur avec le langage Micropython utiliser le code ci-dessus permettra de
recuperer les donnees meteorologique sur le site internet OPENWEATHERMAP et de permettre avec
un ecran SSD1306 d'afficher les informations tirees du site.  
