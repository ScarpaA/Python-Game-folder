word="bonjour" # mot à chercher
blankword="*******" # mot à deviner les étoiles seront remplacées au fur et à mesure
guletters=0 # compteur du nombre de lettres saisies par l'utilisateur

def hangman(letter,word,blankword):
    newword=""
    error=0
    for i in range(len(word)):
        if letter==word[i]:
            blankword[i]==letter
            newword=blankword
        else:
            error+=1
    return newword

while guletters<10 and blankword.count('*')!=0:
    letter=input("your letter")
    guletters+=1
    blankword=hangman(letter,word,blankword)
    print(blankword)
    print(error)
