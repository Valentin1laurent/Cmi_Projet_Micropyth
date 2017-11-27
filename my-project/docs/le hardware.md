# Conception et realisation des composantes electronique du projet


Cette partie reprend donc la realisation ainsi que la conception des differents circuits du projet.Pour cela nous introduirons d'abord le logiciel que nous avons utilise pour concevoir les differents circuits puis nous detaillerons les 2 circuits principale de notre projet.


## Rappel pour l'utilisation de EAGLE.

Voici un petit tutoriel pour utiliser EAGLE-Autodesk.Eagle etant un FREECIEL en anglais. 

###Etape 1
On telecharge le logiciel grace au lien suivant:

	>https://www.autodesk.com/products/eagle/free-download
	
###Etape 2
On cree un nouveau projet qui servira a enregistrer les differents schemas et composants: 

	> File-> new project

Ensuite on va cree une librairie qui regroupera les differentes structures pour les nouveau composants que nous allons crees pour notre projets.

	> new library

###Etape 3
Dans cette etape nous allons participer a la creation des differents composants car malgres le faite que la bibliotheque de EAGLE soit dense on ne trouvera pas toujours les composants que nous utiliserons reelement.

Premierement nous allons creer un 'package' qui permet la creations des pins a implementer sur le circuit imprime.

	> File -> New Package.

Une fois le nouveau package creer on double clique dessus et on se retrouve sur un page avec 4 onglets disponible:  

-Device  

-Package  

-3D Package  

-Symbol 

En bas de ces onglets on clique sur 'ADD ...'.  


#### ADD PACKAGE.  

Dans cette partie on va chercher a creer les 'Trous' qui seront sur le circuit imprime. 

	> Icone : ADD pins.
	> Les pins carre sont utilise pour l'entree de la tension.
	> Les pins rond pour les differentes sorties du composant.
	> Pour simplifier les etapes suivantes donner des noms marquants a ces sorties.
	> Sauvegarder


#### ADD SYMBOL.  
Dans cette partie nous allons creer les symboles qui serviront a placer les composants sur le circuit. 

	>Dessiner la forme du composants.
	>Ajouter les differentes pattes.
	>Changer les noms des pattes de manieres a se reperer.
	>Sauvegarder.

#### ADD DEVICE.  
Dans cette partie nous allons combiner et connecter les symboles a leur packages.

	> On va chercher d'un cote le symbole creer pour le composant et de l'autre le packages.
	> On clique sur le bouton connect.
	> SI l'on a choisis des noms parlants on va pouvoir lier simplement les pattes aux 'trous'.
	> Sauvegarder.


##Support  de connexion pour L'ESP.

Pour connecter notre projet a un ordinateur nous avons du connecter le microcontrolleur a un circuit imprimer realiser par nos soins. Cette connexion s'effectue par le biais d'un cable FTDI.
Il fallait veiller a ce que chaque partie se connecte au bonne endroit pour eviter tous risque de court circuit.
Nous avons donc du respecter le schema de connexion ci dessous:

	> Le RX du FTDI au TX de l'ESP8266
	> Le TX du FTDI au RX de l'ESP8266
	>Le GND du FTDI au GND de l'ESP8266
	>Le VCC du FTDI au VCC de l'ESP8266

Ensuite pour permettre l'affichage des donnees en reel nous avons connecter un ecran OLED sur le meme circuit imprimer.
Il a de nouveau fallu verifier les connectique pour qu'elle respecte le schema suivant:

	> Le SDA du SSD1306 au GPIO0 de l'ESP8266
	> Le SCK du SSD1306 au GPIO2 de l'ESP8266
	> Le GND du SSD1306 au GND de l'ESP8266
	> Le VCC du SSD1306 au 3.3V de l'ESP8266

##Circuit pour le projet final.

Dans le cadre de notre projet nous devions rendre cette objet connecte.Il fallait aussi trouver un moyen de lire les donnees recuperer et de pouvoir alimenter le tous 
sans avoir besoin d'etre constamment brancher a un ordinateur.
Il fallait subvenir au besoin electrique de l'ESP 8266 et de l'ecran oled.
Nous avons donc concu un circuit imprimer capable d'alimenter tous ces composants.
L'utilisation d'un panneau solaire nous paraissait etre la plus adapter pour repondre au besoin du projet mais pour fournir le courant minimal necessaire a l'alimentation du projet
il fallait mettre un panneau delivrant une grande tension. Il est apparu un risque pour les composants. Nous
avons donc appris comment contourner ce problemes en utilisant un regulateur de tension.
 
	
