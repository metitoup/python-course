#!/usr/bin/python
#on déclare sa classe...
class game:
    
    def insert_new_game(self):
    #Je prends un input pour taper mon entrée
    #je déclare mes variables avec self car j'en ai besoin plus loin dans ma classe
        self.name= input ("Name :")
        self.length= input ("Length :")
        self.max_players= input ("Max Players :")
        # J'appelle une méthode pour imprimer ce que j'ai rentré dans la meme classe
        self.print_game()
        
    
    def print_game(self):
        #Je print juste ce que je renvoie avec les variables 'self' qui sont disponibles ici
        print (self.name)
        # je demande à la méthode insert_in_dict de mettre ca dans un dictionnaire
        self.insert_in_dict()

    def insert_in_dict(self):
    #je déclare mon dictionnaire puis je donne une valeur aux clés
        game_dict={}
        game_dict ["Name"] = self.name
        game_dict ["Length"] = self.length
        game_dict ["Max Players"] = self.max_players
        
                
        print ("RAW Dic",game_dict)
        print ("Dict Items : ", game_dict.items())
        
        print("Keys:", list(game_dict.keys()))
        print("Values:", list(game_dict.values()))
        
        
        for key, value in game_dict.items():
            print ("For key",key)
            print ("For Value", value)
        
        print (game_dict['Name'])
        print (game_dict["Length"])
        #houuu attention ici j'ai pas déclaré en self le dictionnnaire donc je l'envoie dans l'appel de la fonction qui va écrire un fichier
        self.insert_in_file(game_dict)
        
    def insert_in_file(self,game_dict):
    #j'ouvre en write j'insère le nom dedans et je le ferme mais je fais un try pour éviter des erreurs comme un file en read only
    #essaye de le faire tourner une nouvelle fois en mettant le fichier en read only dans ton explorateur windows
    #si tu ouvres en "a" au lieu de "w" il écrira à la suite du fichier == append
        print ("J'écris dans mon fichier")
        try:
            myfile=open("mydicfile.txt","w")
            myfile.write(game_dict['Name'])
            myfile.close()
            
        except PermissionError : 
            print("ERROR : File readonly")
            exit()
        except :
            print("Something else is wrong")
        
        else:
            print ("Operation succeeded")
            
        
        
    def read_from_file(self):
    #j'ouvre le fichier en read et je lis ce qu'il y'a dedans ici je pourrais catcher l'erreur ou le fichier n'existe pas/plus
        print ("Je viens lire le fichier depuis mon Main")
        try:
            myfile=open("mySchrödingerdicfile.txt","r")
            print (myfile.readline())#lit une ligne en string
            myfile.close()
            myfile=open("mydicfile.txt","r")
            print (myfile.readlines())#renvoie un tableau avec tout ce qu'il a lu
            
        except FileNotFoundError :
            print("dommage le fichier n'existe pas : change le nom par mydicfile.txt à la ligne 70")
            
        except :
            print("Erreur bizarre ici")
        else: 
            print ("tout est bien qui finit bien")

#je crée une classe qui hérite de game
class videogame(game):
#une méthode qui va rajouter une plateforme 
    def set_platform(self):
        #je reprend la méthode insert de l'autre classe
        
        super().insert_new_game
    # je vais tenter de te faire un truc compréhensible mais la je vais faire dodo    


if __name__ == '__main__':
#on fait une instance de game et on insère un nouveau game
    mygame=game()
    mygame.insert_new_game()
    #et je peux aller lire le fichier
    mygame.read_from_file()
    #j'instancie un autre jeu mais vidéo cette fois et j'appelle la fonction de son papa
    myvgame=videogame()
    print("J'insère un jeu vidéo")
    myvgame.insert_new_game()
