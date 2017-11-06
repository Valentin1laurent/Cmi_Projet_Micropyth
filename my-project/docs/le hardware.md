# LE MATERIEL


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

###Etape 4
##Support pour L'ESP.

Pour connecter notre projet a un ordinateur et pour pouvoir connecter l'ecran oled plus simplement.





## Alimentation.

Nous voulions alimenter notre projet avec une cellule photovoltaique. Le probleme qui c'est poser a nous a ete le choix de la cellule photovoltaique
nous avions a notre disposition une cellule de 5 Volts et une cellule de 10 Volts, hors notre microcontrolleur requiert 3.3 Volt en entree. Pour contrer ce probleme nous avons
introduits un regulateur de tension.
Pour le bon fonctionnement du regulateur nous avons du ajouter des capacites pour eviter les discontinuite de tension aux bornes du regulateur.

