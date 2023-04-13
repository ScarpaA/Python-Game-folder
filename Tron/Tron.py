"""
Programme du tron
nom(s), prÃ©nom(s), classe(s)
"""
import pygame
from random import *

#constantes de la fenÃªtre d'affichage
LARGEUR=800       #hauteur de la fenÃªtre
HAUTEUR=600      #largeur de la fenÃªtre
RED=(255,0,0)     # dÃ©finition de 3 couleurs
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)

#Utilisation de la bibliothÃ¨que pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenÃªtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractÃ¨res
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//2-20
motoY=HAUTEUR//2
motoX2=LARGEUR//2
motoY2=HAUTEUR//2
motoX=LARGEUR//2+20
motoY=HAUTEUR//2
direction = 'gauche'
direction2 = 'up'
direction2 = 'right2'
tempsPartie=0
player=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, RED, [1, 1, LARGEUR-1, HAUTEUR-1],1)
    for i in range(0,50):
        x=randint(0,LARGEUR)
        y=randint(0,HAUTEUR)
        pygame.draw.circle(fenetre, RED, (x,y), randint(5,20))      #cercle plein aux coord x,y de rayon 10
    for i in range(0,70):
        x=randint(0,LARGEUR)
        y=randint(0,HAUTEUR)
        pygame.draw.rect(fenetre, BLUE, [x, y, randint(5,20), randint(5,20)],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnÃ©es x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), GREEN)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminÃ©e

def deplacementmoto2():
    """
    deplace la moto si c'est possible
    """
    global motoX2,motoY2
    touche2=False
    if direction2=='up':
        x2=motoX2
        y2=motoY2-1
        touche2=collisionMur(x2,y2)
    elif direction2=='down':
        x2=motoX2
        y2=motoY2+1
        touche2=collisionMur(x2,y2)
    elif direction2=='right':
        x2=motoX2+1
        y2=motoY2
        touche2=collisionMur(x2,y2)
    elif direction2=='left':
        x2=motoX2-1
        y2=motoY2
        touche2=collisionMur(x2,y2)
    if touche2==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX2=x2
        motoY2=y2
    fenetre.set_at((x2, y2), YELLOW)
    return touche2           #retourne la variable booleenne touche pour savoir si la partie est terminÃ©e

def deplacementmoto3():
    """
    deplace la moto si c'est possible
    """
    global motoX3,motoY3
    touche3=False
    if direction3=='up2':
        x3=motoX3
        y3=motoY3-1
        touche3=collisionMur(x2,y2)
    elif direction3=='down2':
        x3=motoX3
        y3=motoY3+1
        touche3=collisionMur(x2,y2)
    elif direction3=='right2':
        x3=motoX3+1
        y3=motoY3
        touche3=collisionMur(x2,y2)
    elif direction3=='left2':
        x3=motoX3-1
        y3=motoY3
        touche3=collisionMur(x2,y2)
    if touche3==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX3=x3
        motoY3=y3
    fenetre.set_at((x3, y3), YELLOW)
    return touche2           #retourne la variable booleenne touche pour savoir si la partie est terminÃ©e


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenÃªtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupÃ©ration des touches appuyÃ©es en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'
    elif keys[pygame.K_z]:    #est-ce la touche UP
        direction2 = 'up'
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        direction2 = 'down'
    elif keys[pygame.K_d]:  #est-ce la touche RIGHT
        direction2 = 'right'
    elif keys[pygame.K_q]:  #est-ce la touche LEFT
        direction2 = 'left'
    elif keys[pygame.K_i]:    #est-ce la touche UP
        direction3 = 'up2'
    elif keys[pygame.K_j]:  #est-ce la touche DOWN
        direction3 = 'down2'
    elif keys[pygame.K_k]:  #est-ce la touche RIGHT
        direction3 = 'right2'
    elif keys[pygame.K_l]:  #est-ce la touche LEFT
        direction3 = 'left2'

    if deplacementmoto()==True:
        loop=False
    if deplacementmoto2()==True:
        loop=False
        player+=1
    frequence.tick(90)
    pygame.display.update() #mets Ã  jour la fenÃªtre graphique
    tempsPartie+=1
pygame.quit()
print('Game Over')
print('Your time was',tempsPartie)
if player==1:
    print('Player 2 wins')
else:
    print('Player 1 wins')