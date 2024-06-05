#!/usr/bin/python
#je crée une variable globale, un dictionnaire vide mais tu peux déjà mettre des trucs dedans
#l'idée est d'y stocker tous les nouveaux jeux créés et les sauver lorsque tu quittes le programme
#juste le add_games a changé et le main()
#listofdicts=[{'Name': 'catane', 'Duration': '60', 'Maxplayers': '5'}, {'Name': 'carcassonne', 'Duration': '60', 'Maxplayers': '4'}]
listofdicts=[]

class game():
    
    def add_game(self):
    #on crée un dictionnaire pour stocker les infos du jeu avant de le mettre en DB
        dict_game={}
        game_name=input("Nom du jeu : ")
        game_duration=input("Durée du jeu : ")
        game_maxplayers=input("Nombre de joueurs : ")
        dict_game ["Name"]=game_name
        dict_game ["Duration"]=game_duration
        dict_game ["Maxplayers"]=game_maxplayers
        listofdicts.append(dict_game)
    #et on envoie dans la méthode de sauvegarde
        
    
    def save_game(self,dict_game):
    #on ouvre un fichier en append
        myfile=open("Gamedb.txt","a")
    #on y écrit les infos du dictionnaire en rajoutant des tabulations
        for key,value in dict_game.items():
            myfile.write(key+"\t")
            myfile.write(value+"\t")
        myfile.write("\n")
    #et on ferme le fichier
        myfile.close()
        
    def list_game(self):
    #on ouvre le fichier db en read
        myfile=open("Gamedb.txt","r")
    #on parcours le fichier jusqu'a la fin
        result= (myfile.readlines())
    #on print les valeurs en se basant sur les tabulations
        for value in result:
            print (value.split("\t")[1])
        myfile.close()
    #et on ferme le fichier
    
    #on définit une méthode avec une variable    
    def game_details(self,detgame):
        myfile=open("Gamedb.txt","r")
        result= (myfile.readlines())
        for item in result:
            if detgame in item:
            #on affiche les résultats en évitant un retour chariot (\n sur windows \r sous unix linux macos)
                print (item.strip("\n"))
        myfile.close()

#on déclare une classe qui hérite de game
class extension(game):
    def add_extension(self):
    #on déclare un dictionnaire
        dict_game={}
        game_name=input("Nom de l'extension : ")
        game_base=input("Jeu de Base : ")
        dict_game ["Extension"]=game_name
        dict_game ["Base"]=game_base
    #on utilise la fonction save_game de la classe parente
        self.save_game(dict_game)

def print_menu():
    print_separator()
    print ("1. Ajouter Jeu")
    print ("2. Lister Jeu")
    print ("3. Détails Jeu")
    print ("4. Afficher Menu")
    print ("5. Ajout Extension")
    print ("99. Erase Database")
    print ("0. Quitter ")
    print_separator()
    
def print_separator():
    return(print ("___________________"))

def choose_game():
    #on donne le nom du jeu à chercher
    detgame=input("Jeu à chercher: ")
    #On instancie un game
    mygame=game()
    #on affiche les détails du jeu choisi
    mygame.game_details(detgame)

def erase_database():
    # on s'assure que c'est le bon choix
    rusure=input("Etes-vous sûr ? Y/n : ")
    if rusure=="Y" :
        myfile=open ("Gamedb.txt",'w')
    else : pass        

def select_option(selection):
    #nouveauté de python3  on compare la selection envoyée et on lance l'option du menu
    match selection:
        case "1":
        #on instancie un game
            mygame=game()
        #on ajoute un jeu
            mygame.add_game()
        case "2":
        #on instancie un game
            mygame=game()
        #on liste les games a partir du fichier (== db)
            mygame.list_game()
        case "3":
        #on choisit un jeu avec la méthode idoine
            choose_game()
        case "4":
            print ("Afficher Menu")
        case "5":
        #On inancie une extension
            myext=extension()
        #On rajoute une extension
            myext.add_extension()
        case "99":
        #on remet le fichier à 0
            erase_database()
            print ("Erase Database")
        case "0":
            print ("Quitter et Sauver")
        case _:
            print ("Mauvaise selection")

if __name__ == '__main__':
    # On déclare selection pour qu'il existe et qu'on puisse le tester
    selection=1
    #Tant que selection n'est pas 0 on lance la possibilité de choisir dans le menu
    while (selection!='0'):
        #on lance la def qui imprime le menu on peut ainsi le lancer n'importe où au besoin
        print_menu()
        selection=input("Votre choix : ")
        #la fonction separator met des ___ pour espacer l'output
        print_separator()
        #on lance la méthode avec la selection
        select_option(selection)

#je parse le dictionnaire global tout est en mémoire
for item in listofdicts: 
    print (item ['Name'])
    print (item ['Duration'])
#et je vais tout taper dans le fichier en itérant
mygame=game()
for item in listofdicts:
    mygame.save_game(item)
#tu vois ici la puissance de l'orienté objet tu peux facilement utiliser ta classe pour faire des appels à des méthodes sans devoir ré écrire
#après ici l'utilisation du dict pour tout mettre en mémoire c'est pas top tu es susceptible de perdre facilement beaucoup de données c'est juste pour la manipulation des
#dictionnaires en gros ca peut te faire une "base de données" temporaire