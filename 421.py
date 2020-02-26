### PARTIE 1 ###

# la ligne suivante permet d'ajouter au langage Python des commandes graphiques
# utiles pour créer des applications, par exemple, des petits jeux
from tkinter import *

# création d'une fenêtre graphique
fen=Tk()
fen.title('Tirage de trois dés')

# nous allons créer trois zones d'affichage pour nos dés
# chaque zone fait 60 sur 60,
# découpée en 9 cases de 20x20 pouvant contenir chacune un point blanc
# exemple : pour un dé donnant un trois

#  ----- ----- -----
# |  O  |     |     |
#  ----- ----- -----
# |     |  O  |     |
#  ----- ----- -----
# |     |     |  O  |
#  ----- ----- -----

# <----><----><---->
#   20    20    20

zone1=Canvas(fen,bg='dark gray',height=60, width=60)
zone1.pack(side = LEFT)

zone2=Canvas(fen,bg='dark gray',height=60, width=60)
zone2.pack(side = LEFT)

zone3=Canvas(fen,bg='dark gray',height=60, width=60)
zone3.pack(side = LEFT)


### PARTIE 2 ###

def dessiner_point(zone_choisie, x, y):
    zone_choisie.create_oval(x-8, y-8, x+8, y+8, fill='white')


def dessiner_de1(zone):
    dessiner_point(zone, 30, 30)

def dessiner_de2(zone):
    dessiner_point(zone, 10, 10)
    dessiner_point(zone, 50, 50)





def dessiner_de(zone, numero):
    zone.delete("all")
    if numero == 1:
        dessiner_point(zone, 30, 30)
    elif numero == 2:# elif est une contraction de else et if : sinon si
        dessiner_point(zone, 10, 10)
        dessiner_point(zone, 50, 50)
#   continuez ici


### PARTIE 3 ###




### PARTIE 4 ###

def est_42(de1, de2):
    if (de1 == 4 and de2 == 2) or (de1 == 2 and de2 == 4):
        print("Gagné ! C'est bien un 42.")
    else:# sinon
        print("Perdu... Ce n'est pas un 42.")



### PARTIE 5 ###

