base = [["M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","D","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","M","M","M","M","M","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","M","M","M","A","A","A","A","A","A","A","A","A","A","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","B7","A","F","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","B6","M","M","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","B5","M","M","M"],
         ["M","M","M","M","A","A","A","A","A","M","M","M","A","A","A","A","B4","M","M","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","C","B3","M","M","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","A","A","A","C","B2","M","M","M"],
         ["M","A","A","A","A","A","A","A","A","A","A","A","M","M","M","C","B1","M","M","M"],
         ["M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M"]]

lemming = []

class Case :
    
    def __init__(self, terrain, ligne, colonne, lemming = None):
        self.terrain = terrain
        self.lemming = lemming
        self.x = ligne
        self.y = colonne
    
    def __str__(self):
        if self.lemming is not None :
            return "lemming"
        
        if self.terrain != "M":
            return "#"
        
        
    def libre(self):
        if self.lemming is not None and self.terrain is not["M"]:
            return True


    def arrivee (self, lemming):
        if self.terrain == ["F"]:
            self.lemming = None
            return 0
        
        else :
            self.lemming = lemming

class Jeu:

    def __init__(self, grotte):
        self.grotte = [[Case(base[x][y], x, y) for x in range(len(base))]for y in range(len(base[0]))] 
    
    def affichage(self, x, y, grotte):
         for x in self.grotte:
 #            for x in range(len(base)):
 #                for y in range(len(base[0])):
                        print(self.grotte(x,y))
                    
                    
    def tour(self, terrain):
        for lem in lemming:
            lemming.lem.action()


    def demarre(self):
        if terrain == ["D"]: # remplacer par for d in grotte pour voir la case départ de la carte
            if self.lemming == None:
                lemming.append(Lemming())
                
        user = input("\tQ : Quitter\n\tL: Ajouter un Lemming\tJ: Jouer un Tour")

        while user != "Q":
            print(carte)

# ! Modifier les paramètres de l'append de lemming aux coordonnées de la case de départ
            if user == "L":
                lemming.append(Lemming(1, 0, 1))
                user = input("\tQ : Quitter\n\tL: Ajouter un Lemming\tJ: Jouer un Tour")
            
            if user == "J":
                self.tour()
                user = input("\tQ : Quitter\n\tL: Ajouter un Lemming\tJ: Jouer un Tour")

class Lemming:
    
    # instancie un lemming avec ses coordonnées et sa direction
    def __init__(self, ligne, colonne, direction):
        self.x = ligne
        self.y = colonne
        self.direction = direction
        self.nom = "L"+str(len(lemming))

        """
        if direction == 1:
            self.direction = ">"
        
        else:
            self.direction = "<"
        """
    
    # retourne la direction du lemming 
    def __str__(self): # type: ignore

        if self.direction == 1:
            return ("Le lemming est de direction droite '>'")
        
        if self.direction == -1:
            return ("Le lemming est de direction gauche '<'")

    # avance, recule ou tombe par plusieurs conditions par rapport aux coordonnées du lemming
    def action(self, carte):
        
        # Vérifie si la case du bas du lemming n'est pas de l'air
        if carte[self.y][self.x+1] == "M" :
            self.direction = -1
        
        if carte[self.y][self.x-1] == "M":
            self.direction = 1
        
        if carte[self.y+1][self.x] != "A":
            
            if carte[self.y][self.x+1] != "M" and self.direction == 1:
                self.x += 1
        
            if carte[self.y][self.x-1] != "M" and self.direction == -1:
                self.x -= 1
            
        else:
            self.y += 1

    # enlève le lemming de la liste et imprime un message     
    def sort(self):
        lemming.remove(self.nom)
        return "Un Lemming est sorti du jeu"
    
"""
carte = [["M","A","A","M"],
         ["M","A","A","M"],
         ["M","A","A","M"],
         ["M","M","M","M"]]

lems = Lemming(1, 2, 1)
print(lems.x, lems.y)
lems.action(carte)
print(lems.x, lems.y)
lems.action(carte)
print(lems.x, lems.y)
"""
a = []
a.append(Lemming(1,0,1))
print(a[0])

# jeu = Jeu(base)

a = ""
a += str(len(lemming))
print(a)
print(len(lemming))