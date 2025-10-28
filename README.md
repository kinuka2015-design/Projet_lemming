# Projets POO - Terminale NSI
Lemmings
Lemmings est un jeu vidéo de réflexion développé par le studio écossais DMA Design [...].
Le joueur doit guider des dizaines de lemmings, minuscules créatures écervelées, dans des
niveaux alambiqués truffés de dangers mortels. Le jeu est fondé sur le mythe populaire
selon lequel les lemmings, petits rongeurs bien réels des régions arctiques, se livreraient
au suicide collectif en se jetant des falaises. - Wikipedia
L’objectif de ce projet est d’adapter ce jeu à plusieurs niveaux. Nous allons représenter ce jeu
à l’aide d’une grille en 2D (tableau à deux dimensions), dont chaque case est soit un mur, soit
un espace vide pouvant accueillir un lemming maximum à un instant donné. Les lemmings
apparaissent l’un après l’autre à une position de départ et disparaissent lorsqu’ils atteignent
une case de sortie. Chaque lemming a une coordonnée verticale et une coordonnée horizontale
désignant la case dans laquelle il se trouve. Les lemmings se déplacent à tour de rôle, toujours
dans leur ordre d’introduction dans le jeu, de la manière suivante :

• Si l’espace immédiatemment en dessous est vide, le lemming tombe d’une case.
• Sinon, si l’espace immédiatement devant est vide, le lemming avance d’une case.
• Sinon (= si aucune des deux autres solutions n’est possible) le lemming se retourne.

## I - Avoir un jeu fonctionnel
Pour l’instant, nous allons limiter au maximum les interactions de l’utilisateur. Il pourra
uniquement faire apparaître de nouveaux lemmings et faire tourner le jeu. On va donc
simplement voir évoluer une colonie de lemmings dans le terrain de jeu.
Le code sera structuré en 3 classes :
1. Une classe Case contenant un attribut terrain, un caractère représentant la
caractéristique du terrain de cette case (mur, vide ou sortie), et un attribut lemming
contenant l’éventuel lemming présent dans cette case (None si la case est vide).
Ces méthodes seront à implémenter dans cette classe :
- __str__(self) : renvoie le caractère à afficher pour représenter cette case ou son
occupant.
- libre(self) : renvoie le booléen « La case peut recevoir un lemming », c’est à dire
qu’elle n’est ni un mur, ni occupée.
- depart(self): retire le lemming présent (on veut être sûr qu’il y a bien un lemming).
- arrivee(self, lem) : place le lemming lem sur la case ou le fait sortir du jeu si la case
est une sortie.

2. Une classe Lemming contenant des attributs entiers ligne et colonne indiquant la ligne et
la colonne auxquelles se trouvent le lemming ainsi qu’un attribut direction valant 1 ou
-1 selon que le lemming est tourné vers la droite ou vers la gauche.
Cette classe fournit (entre autres) les méthodes suivantes :
- __str__(self) : renvoie < ou > selon que le lemming est tourné vers la droite ou vers
la gauche.
- action(self) : exécute une action pour le lemming (tomber, avancer ou reculer).
- sort(self) : retire le lemming du jeu.
  
3. Une classe principale Jeu contenant un attribut grotte représentant le terrain de jeu au
travers d’une liste de listes de Cases et un attribut lemmings contenant la liste des
lemmings actuellement en jeu. Son constructeur initialise la grotte à partir d’une
variable globale pour l’instant : par exemple, # pour un mur, O pour la sortie et
quelques espaces pour une case vide.
Cette classe implémentera les méthodes suivantes :
- affiche(self) : affiche la carte avec les positions et directions de tous les lemmings
en jeu. On évitera d’utiliser __str__(self) ici par commodité (c’est la pratique en POO).
- tour(self) : exécute un tour de jeu en faisant bouger chaque lemming une fois et en
affichant le nouvel état du jeu.
- demarre(self) : lance une boucle infinie attendant des commandes de l’utilisateur.
Exemples : L pour ajouter un lemming, Q pour quitter, Entrée pour jouer un tour…
On jouera donc à Lemmings en créant une instance de la classe Jeu, puis en exécutant
monJeu.demarre().

## II – Ajouter de la modularité
Cette partie a pour objectif de faire en sorte que le jeu soit plus intéressant à jouer.
Vous pouvez par exemple :
• Traiter des cartes à partir de fichiers textes, pour qu’elles soient plus faciles à construire
(voire même à générer aléatoirement?)
• Ajouter de l’interaction avec l’utilisateur : dans le jeu vidéo, on peut donner un
« métier » à un lemming (regardez sur Internet), accélérer le temps, mettre en pause,
faire apparaître les lemmings automatiquement…
• Construire un système de niveaux où on passe par plusieurs cartes au fil du temps.
• Ajouter des objectifs (temps imparti, nombre de lemmings à sauver…)
•
...

## III – Faire un rendu graphique
La dernière partie a pour but de rendre ce jeu ✨fancy . Renseignez-vous sur la bibliothèque ✨
Tkinter pour monter une belle interface graphique à l’aide de vos talents de graphistes !
L’utilisation de cette bibliothèque n’est pas au programme, c’est donc que du bonus.
