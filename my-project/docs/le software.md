#LE SOFTWARE

Ici nous detaillerons les differents code que nous avons developper pour la realisation du projet.


##Outils utilises avec PYTHON

###Utilisation de Requests

	>>>> import requests

	>>> url="..."

	>>> r=requests.get(url) 

Ces quelques ligne de code permettent de recuperer les donnes d'une page web.
Il suffit de remplacer le trou laisser dans la variable URL pour notifier la page web ou l'on souhaite recuperer les infos.


	>>> import requests

	>>> url="https://www.wikipedia.org/"

	>>> r=requests.get(url)

	>>>print(r) 

L'exemple au dessus permet de charger les informations de la page d'acceuil de WIKIPEDIA.

###Utilisation d'une API 
Pour notre projet nous avons besoin de recuperer des donnees sur la meteo a des endroits precis du globe,
pour cela nous nous sommes tourner vers le site:  


OPENWEATHERMAP.ORG  



	>http://api.openweathermap.org/data/2.5/forecast?id={ID}&APPID={APIKEY}

La ligne de code precedente permet de recuperer les donnees meteorologique sur le site.

###Utilisation du format json 

Les donnees sous le format JSON apparaissent sous la forme d'un dictionnaire.
On sait qu'un dictionnaire marche grace a la combianaison d'un 'id' et d'une 'cle'.
On peut donc extraire la donnee souhaite si l'on connait les 'liens' de ce dictionnaire.
Voici un petit exemple qui montre comment marche un dictionnaire.

	>>>mon_dictionnaires={'mot de passe': '*', 'pseudo': '6pri1'}

	>>>mon_dictionnaire['mot de passe']

	>>>'*'

	>>>mon_dictionnaire['pseudo']

	>>>'6pri1' 


Devant la simplicite d'utilisation du format JSON nous avons decide d'incorporer dans notre code la fonction JSON
qui permettra de crer une arborescence plus simple des donnees et qui nous facilitera l'acces a celle-ci.

Le code va de nouveau se modifier pour devenir:

	>>>> import requests

	>>>import json

	>>> url="http://api.openweathermap.org/data/2.5/forecast?id={ID}&appid={APIKEY}"

	>>> r=requests.get(url)

	>>>data=r.json()

##Algorithme de recuperation des donnees meteorologiques

###Recuperation de la temperature et de la description du temps
Dans un fichier texte sur le site OPENWEATHERMAP il est possible de conaitre l'arborescence des differents dictionnaires
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
	
	>http://api.openweathermap.org/data/2.5/forecast?id=2998323&appid={APIKEY}

##Developpement en MICRO-PYTHON


###Connexion a internet
Pour reussir a connecter le microcontroleur a internet il a fallut inserer dans celui ci le code suivant:

	>>>def do_connect():
	>import network
	>sta_if = network.WLAN(network.STA_IF)
	>if not sta_if.isconnected():
	>print('connecting to network...')
	>sta_if.active(True)
	>sta_if.connect('id', 'mdp')
	>while not sta_if.isconnected():
	>pass
	>print('network config:', sta_if.ifconfig())
	>do_connect() 

A la 7 eme ligne il faut remplacer id par le nom du reseau et mdp par la cle de securite de ce reseau.







#CODE

Voici le code en un seul bloc:

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