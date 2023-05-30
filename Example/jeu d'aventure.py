"""
Programme réalisé par nom, prénom, classe
"""
#desciption des pièces en fonction du numéro
def decrireLaPiece(piece):
    if piece==1:
        print("vous vous trouvez dans le vestibule")
    elif piece==2:
        print("vous vous trouvez dans la salle à manger")
    elif piece==3:
        print("vous vous trouvez dans la cuisine")

#la fonction decision ou "machine a état" permettant de se déplacer
#ou non en fonction de la pièce ou l'on se situe
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
        print("Deplacement impossible")
    return piece

#programme principal
dansQuellePierceEstLePersonnage=1   #variable très explicite
menu='0'
while menu!='q':
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    dansQuellePierceEstLePersonnage=decision(menu,dansQuellePierceEstLePersonnage)

print("Au revoir")


