"""
Programme réalisé par nom, prénom, classe
"""
import pygame

#variables du niveau
NB_TILES = 32   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=21       #hauteur du niveau
hauteur=18       #largeur du niveau
tiles=[]       #liste d'images tiles

#variables de gestion du pacman
pacX=10          #position x y du pacman dans le niveau
pacY=11
compteurBilles=0

#variables de gestion du fantome
FRAMERATE_FANTOME=12      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME=45   #le fantome se deplace sur 9 cases
positionFantome=1
frameRateCounterFantome=0
posfX=2     #position initiale du fantome
posfY=16

#definition du niveau

niveau=[[1,5,5,5,5,5,2,0,0,6,31,6,0,0,1,5,5,5,5,5,2],
     [6,12,12,12,12,12,6,0,0,6,0,6,0,0,6,12,12,12,12,12,6],
     [6,12,23,10,2,12,3,5,5,4,0,3,5,5,4,12,1,10,24,12,6],
     [6,12,12,6,6,12,12,12,12,12,12,12,12,12,12,12,6,6,12,12,6],
     [3,2,12,6,3,5,5,5,5,2,12,1,5,5,5,5,4,6,12,1,4],
     [1,4,12,3,5,5,5,5,5,9,12,7,5,5,5,5,5,4,12,3,2],
     [6,12,12,12,12,12,12,12,12,25,12,25,12,12,12,12,12,12,12,12,6],
     [6,12,1,2,12,1,2,12,12,0,0,0,12,12,1,2,12,1,2,12,6],
     [6,12,6,6,12,6,6,12,1,5,5,5,2,12,6,6,12,6,6,12,6],
     [6,12,6,6,12,6,6,12,6,0,16,0,6,12,6,6,12,6,6,12,6],
     [6,12,6,6,12,6,6,12,3,5,5,5,4,12,6,6,12,6,6,12,6],
     [6,12,6,6,12,6,6,12,12,12,0,12,12,12,6,6,12,6,6,12,6],
     [6,12,3,4,12,3,8,24,12,23,10,24,12,23,8,4,12,3,4,12,6],
     [6,12,12,12,12,12,12,12,12,12,6,12,12,12,12,12,12,12,12,12,6],
     [3,2,12,1,5,5,10,5,24,12,25,12,23,5,10,5,5,2,12,1,4],
     [1,4,12,3,5,5,4,12,12,12,12,12,12,12,3,5,5,4,12,3,2],
     [6,12,12,12,12,12,12,12,1,2,0,1,2,12,12,12,12,12,12,12,6],
     [3,5,5,5,5,5,5,5,4,6,30,6,3,5,5,5,5,5,5,5,4]]

fantome=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,12,13,14,15,16,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,11,0,0,0,17,0,0,0,0,0,0,0,0],
     [0,0,4,5,6,7,8,9,10,0,0,0,18,19,20,21,22,23,24,0,0],
     [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0],
     [0,0,2,0,0,0,0,39,38,37,36,35,34,33,0,0,0,0,26,0,0],
     [0,0,1,44,43,42,41,40,0,0,0,0,0,32,31,30,29,28,27,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))


def affichePac(numero):
    """
    affiche le pacman en position pacX et pacY
    """
    fenetre.blit(tiles[numero],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render(str(score), True, (255, 255, 255))
    fenetre.blit(scoreAafficher,(525,575))

def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coodFantome=x,y
    return coodFantome          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome(fantome):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome
    global positionFantome
    global posfX,posfY
    if frameRateCounterFantome==FRAMERATE_FANTOME:      #ralenti la viteese du fantome
        posfX,posfY=rechercheFantome(fantome,positionFantome)   #deballage du tuple coordonnées du fantome
        positionFantome+=1
        if positionFantome==NB_DEPLACEMENT_FANTOME:     #un tour est fait donc on passe à la 1ere position
            positionFantome=1
        frameRateCounterFantome=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[15],(posfX * TITLE_SIZE,posfY * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome+=1                          #incrémentation du compteur de vitesse


chargetiles(tiles)  #chargement des images

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                posY = pacY - 1             #on deplace le pacman vituellement
                posX = pacX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                orientation=29
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 30 or numeroTile == 31):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacY -= 1                               #on monte donc il faut décrémenter pacY
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                orientation=27
                print("down",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 30 or numeroTile == 31):
                    pacY += 1
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")
            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                posY = pacY
                posX = pacX + 1
                numeroTile = niveau[posY][posX]
                orientation=14
                print("right",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 30 or numeroTile == 31):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX += 1                               #on monte donc il faut décrémenter pacY
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                posY = pacY
                posX = pacX - 1
                numeroTile = niveau[posY][posX]
                orientation=28
                print("left",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 30 or numeroTile == 31):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX -= 1                               #on monte donc il faut décrémenter pacY
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            if (numeroTile==12):  #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la bille dans le niveau
                print("nouvelle bille")
            else:
                print("fond noir")
            if (numeroTile==30):
                pacY=1
            elif (numeroTile==31):
                pacY=16

    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    affichePac(14)          #affiche la pacman et le score
    deplaceFantome(fantome) #mettre un commentaire pour desactiver le déplacement du fantome
    afficheScore(compteurBilles)
    pygame.display.update() #mets à jour la fentre graphique
    #-----------------------------------------------------------------------------------------------------------------
    #Other stuffs
    #-----------------------------------------------------------------------------------------------------------------




pygame.quit()

