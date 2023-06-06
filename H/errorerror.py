word=" " # mot à chercher
blankword=" " # mot à deviner les étoiles seront remplacées au fur et à mesure
guletters=0 # compteur du nombre de lettres saisies par l'utilisateur

def hangman(letter,word,blankword):
    newword=""
    error=0
    for i in range(len(word)):
        if word[i]==letter:
            newword+=letter
        else:
            newword+=blankword[i]
    return newword

while guletters<15 and blankword.count('*')!=0:
    letter=input("your letter")
    guletters+=1
    blankword=hangman(letter,word,blankword)
    print(blankword)
    print(guletters)

if blankword.count('*')==0:
    print("congrats, lowlife. You must feel real proud of yourself")
else:
    print("random guesses can only get you so far")
