"""
Programme réalisé par nom, prénom, classe
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("salle-a-manger.jpg")
image3=pygame.image.load("cuisine.jpg")
text1 = font.render("Vous vous trouvez dans le vestibule", True, (0, 255, 0))
text2 = font.render("Vous vous trouvez dans la salle à manger", True, (0, 255, 0))
text3 = font.render("Vous vous trouvez dans la cuisine", True, (255, 0, 255))


dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,300))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,300))



def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='n':
        if piece==1:
            piece=2
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==2:
            piece=1
    #E : le personnage désire aller à l'est
    elif direction=='e':
        if piece==2:
            piece=3
    #O : le personnage désire aller à l'ouest
    elif direction=='o':
        if piece==3:
            piece=2
    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

