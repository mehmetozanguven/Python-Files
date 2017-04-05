import random
player_1_list = []
player_2_list = []

def random_list_each_player():
    all_equiments= []
    in_file=open("pokemon_list.txt","r")
    for line in in_file:
        property_list = []
        for token in line.split():
            try:
                int_token = int(token)
                property_list.append(int_token)
            except:
                property_list.append(token)
        all_equiments.append(property_list)
    in_file.close()
    print "Welcome to our game"

    for player_1 in range(3): #for this loop i choice 3 pokemons
        random_player_1 = random.choice(all_equiments[1:])
        #i am starting choose from elements 1 because elements 0 is:
        #Pokemon 	HP 	Attack_Points	Type	Weakness
        player_1_list.append(random_player_1)


    for player_2 in range(3):
        random_player_2 = random.choice(all_equiments[1:])
        #i am starting choose from elements 1 because elements 0 is:
        #Pokemon 	HP 	Attack_Points	Type	Weakness
        player_2_list.append(random_player_2)

random_list_each_player()

print "Please enter a name player 1:"
player_1 = raw_input()
print "Please enter a name player 2:"
player_2 = raw_input()
print "Before the start,we have to decide which player can be first player.\n" \
      "We can decide with HEADS OR TAILS"
print player_1,"Write down HEADS OR TAILS"
head_or_tails = raw_input()
headOrTails = head_or_tails.upper()
list_head_tails = ["HEADS","TAILS"]
choose_head_tails = random.choice(list_head_tails)

if headOrTails == choose_head_tails: #for randomly start
    print "You won",player_1,".You first"
    gamer_1 =player_1
    gamer_2 = player_2
else:
    print "Sorry!!Your guess is wrong.\n",player_2,"You first"
    gamer_1 = player_2
    gamer_2 = player_1
print  gamer_1.upper(),"your pokemons list==",player_1_list
print  gamer_2.upper(),"your pokemons list ==",player_2_list
print "First element of list,there is name of your pokemons.\n" \
      "Second element,there is HP.\n" \
      "Third element,there is attack point.\n" \
      "Fourth element,there is TYPE.\n" \
      "Fifth element,there is weakness.\n" \

print "If the player's pokemon has a weakness his/her rival's pokemon then the pokemon gets an extra +10 attack points"

def duringFight():
    count_for_player1 = 3
    count_for_player2 = 3
    correct_1 =True
    while correct_1 :


        print "Please select your pokemon" ,gamer_1.upper()," (enter numbers between 1",count_for_player1,")"
        select_pokemon_player_1 = input()
        if select_pokemon_player_1 < 1 or select_pokemon_player_1 > count_for_player1:
            #with this if statement i am checking that whether select_pokemon_player interval numbers between or not.
            print "You entered wrong number"
            print "Game Over"
            exit()
        print "Please select your pokemon",gamer_2.upper(),"(enter numbers between 1",count_for_player2,")"
        select_pokemon_player_2 = input()
        if select_pokemon_player_2 < 1 or select_pokemon_player_2 > count_for_player2:
            #with this if statement i am checking that whether select_pokemon_player interval numbers between or not.
            print "You entered wrong number"
            print "Game Over"
            exit()
        print gamer_1.upper(),"your pokemon is",player_1_list[select_pokemon_player_1 - 1]
        print gamer_2.upper(),"your pokemon is",player_2_list[select_pokemon_player_2 - 1]

        correct_2 = True
        while correct_2:
            if player_1_list[select_pokemon_player_1 - 1][3] == player_2_list[select_pokemon_player_2- 1 ][4]:
                player_1_list[select_pokemon_player_1 - 1][2] = player_1_list[select_pokemon_player_1 - 1][2] + 10
                #this is for speacial case(+10 attack points)
                print "Your pokemon has a power ",gamer_1.upper(),player_1_list[select_pokemon_player_1 - 1]
                correct_2 = False
            if player_2_list[select_pokemon_player_2 - 1][3]== player_1_list[select_pokemon_player_1 - 1][4]:
                player_2_list[select_pokemon_player_2 - 1][2] =player_2_list[select_pokemon_player_2 - 1][2] + 10
                #this is for speacial case(+10 attack points)
                print "Your pokemon has a power",gamer_2.upper(),player_2_list[select_pokemon_player_2 - 1]
                correct_2 = False

            correct_3 = True
            while correct_3 :
                print "After",gamer_1.upper(),"attack's"
                player_2_list[select_pokemon_player_2-
                              1][1]=player_2_list[select_pokemon_player_2-1][1]-player_1_list[select_pokemon_player_1-1][2]
                print gamer_2.upper(),"your list",player_2_list[select_pokemon_player_2 - 1 ]
                if player_2_list[select_pokemon_player_2 - 1][1] <= 0:
                    #if there is no hp,it means he has been defeated
                    print gamer_2.upper(),"your pokemon has been defeated Please select new one"
                    del player_2_list[select_pokemon_player_2 - 1] #for delete items in the list
                    print "Now your pokemon list",gamer_2.upper(), player_2_list
                    count_for_player2 = count_for_player2 - 1
                    if count_for_player2 == 0:
                        #count_for_player2 = 0,it means that all pokemons player have been defeated by the other player
                        print  gamer_1.upper(),"YOU HAVE BECOME A POKEMON MASTER!!!"
                        print gamer_2.upper(),"YOU HAVE TO TRAIN YOUR POKEMON HARDER"
                        print "GAME OVER"
                        exit()
                    print "Please select your pokemon",gamer_2.upper(),"(enter numbers between 1",count_for_player2,")"
                    select_pokemon_player_2 = input()
                    if select_pokemon_player_2 < 1 or select_pokemon_player_2 > count_for_player2:
                        print "You entered wrong number"
                        print "Game Over"
                        exit()
                print "After",gamer_2.upper(), "attack's"
                player_1_list[select_pokemon_player_1-1][1]=player_1_list[select_pokemon_player_1-1][1]-player_2_list[select_pokemon_player_2-1][2]
                print gamer_1.upper() ,"Your list",player_1_list[select_pokemon_player_1-1]
                if player_1_list[select_pokemon_player_1-1][1]<= 0:
                    #if there is no hp,it means he has been defeated
                    print gamer_1.upper(),"Your pokemon has been defeated Please select new one"
                    del player_1_list[select_pokemon_player_1-1]
                    print "Now your pokemon list",gamer_1.upper(),"==",player_1_list
                    count_for_player1 = count_for_player1 - 1
                    if count_for_player1 == 0:
                        #count_for_player1 = 0,it means that all pokemons player have been defeated by the other player
                        print gamer_2.upper(), "YOU HAVE BECOME A POKEMON MASTER!!!"
                        print gamer_1.upper(),"YOU HAVE TO TRAIN YOUR POKEMON HARDER"
                        print "GAME OVER"
                        exit()

                    print "Please select your pokemon",gamer_1.upper(),"(enter numbers between 1",count_for_player1,")"
                    select_pokemon_player_1 = input()
                    if select_pokemon_player_1 < 1 or select_pokemon_player_1 > count_for_player1:
                        print "You entered wrong number"
                        print "Game Over"
                        exit()
        continue

duringFight()


#Mehmet Ozan Guven
#220201036