import random


words = ["stack", "queue", "tree", "linked list", "software",
                 "hardware", "operating systems", "algorithm", "computer", "network"]


def randomly():
    guess_word=random.choice(words)
    list_guess_word = list(guess_word)
    return list_guess_word


def initializing_word():
    initializing_word = "-" * len(a)
    list_initializing_word = list(initializing_word)
    for i in range(len(a)):
        if " " == a[i]: #this if statement was used for to remove "-" "operating system and linked list"
            list_initializing_word[i] = " "
    return list_initializing_word


def replace_word():
    remaining = 6
    while remaining >= 0:
        take_word = raw_input("Plesea enter the word or one letter ==")
        if len(take_word) == 1:
            if take_word not in a:
                remaining = remaining - 1
                if remaining == 0:
                    print name.upper(),",You have lost.Our world would be","".join(a)
                    break
                print "You have ",remaining,"remainings"

            if take_word in a:
                for i in range (len(a)):
                    if take_word == a[i]:
                        b[i] = take_word
                if b == a: #this if condition was used for if all letter ,which gets user,
                           # form a word,then program says that "YOU WIN"
                    print name.upper(),",Congratulations!Our world is","".join(a)
                    break
            print b

        else:
            if take_word == "".join(a):
                print name.upper(), ",Congratulations! Our word is",take_word.upper()
                remaining = -1 #this line was used for out of the loop
            if take_word != "".join(a):
                print name.upper(),",You have lost.Our word would be","".join(a)
                remaining = -1  #this line was used for out of the loop

print "Welcome to our game.Please enter a name then game will be started\n" \
      "Pay attention!!If you want to guess all word,you have just one guess\n" \
      "If you want to guess by one by,you have 6 guesses"
print


name = raw_input("Please enter a your name \n")
print "Welcome ",name.upper()
correct = True
while correct:

    a = randomly()
    b = initializing_word()
    print "This is the list"
    print b
    replace_word()
    print "Do you want to play again?If you do not please enter 1 if you do enter 2"
    x = input()
    if x == 1:
        correct = False #this line,i am using like break
    else:
        correct = True


#Mehmet Ozan Guven
#220201036