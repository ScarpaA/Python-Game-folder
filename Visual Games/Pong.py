"""
Programme affichage
"""
import pygame
from random import *

#constantes de la fenêtre d'affichage
LARGEUR=800       #hauteur de la fenêtre
HAUTEUR=600      #largeur de la fenêtre
NWHITE=(254,254,254)     # définition de 3 couleurs
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Ball game")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
random=randint(0,1)
if random==0:
    vecteurBalleX=3
else:
    vecteurBalleX=-3
vecteurBalleY=1
Pong1X=LARGEUR-70
Pong2X=0+70
PongY1=HAUTEUR//2
PongY2=HAUTEUR//2
vectorPongY1=0
vectorPongY2=0

def ShowRect1(x1,y1,length1,height1):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, WHITE, [x1, (PongY1), length1, height1])

def ShowRect2(x2,y2,length2,height2):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, WHITE, [x2, (PongY2), length2, height2])

def afficheBalle():
    """
    affiche un cercle aux coordonnées x,y avec un rayon
    """
    pygame.draw.circle(fenetre, NWHITE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY

def MoveRect1():
    global PongY1
    PongY1=PongY1+vectorPongY1

def MoveRect2():
    global PongY2
    PongY2=PongY2+vectorPongY2

def collision():
    global vecteurBalleX, vecteurBalleY
    color=fenetre.get_at((balleX,balleY))[:3]
    if color==(255,255,255):
        vecteurBalleX=vecteurBalleX*-1
        vecteurBalleY=randint(1,5)
    if balleX>LARGEUR-RAYONBALLE or balleX<0+RAYONBALLE:
        vecteurBalleX=vecteurBalleX*-1
    if balleY>HAUTEUR-RAYONBALLE or balleY<0+RAYONBALLE:
        vecteurBalleY=vecteurBalleY*-1

def points(x,y,txt):
    texteAfficher = font.render(str(txt), True, NWHITE)
    fenetre.blit(texteAfficher,(x,y))

def Rectcollision():
    global PongY
    if PongY>HAUTEUR:
        PongY=HAUTEUR
    if PongY<0:
        PongY=0


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:
        vectorPongY1=-2.5
    elif keys[pygame.K_DOWN]:
        vectorPongY1=2.5
    else:
        vectorPongY1=0
    if keys[pygame.K_w]:
        vectorPongY2=-2.5
    elif keys[pygame.K_s]:
        vectorPongY2=2.5
    else:
        vectorPongY2=0

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    ShowRect1(Pong1X,PongY1,20,100)
    ShowRect2(Pong2X,PongY2,20,100)
    MoveRect1()
    MoveRect2()
    collision()
    points(100,50,str(balleX)+' '+str(balleY))
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()