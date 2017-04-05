import random #for the random select

in_file = open("men_heroes.txt","r")
general_list_men = []
lines_men = in_file.readlines()
line_count = 0
while line_count<len(lines_men):
    list_2 = [] #firs i am appending list_2 then appending general_list_men
    for i in lines_men[line_count].split(":"): #for the seperate man and their preference list
        list_2.append(i)
    general_list_men.append(list_2)
    line_count = line_count + 1
i = 0
while i < len(general_list_men):
    a = "".join(general_list_men[i][1])
    b = a.split(",") #just i want each string elements to make list's elements
    general_list_men[i][1]=b

    i = i + 1
in_file.close()


in_file = open("women_heroes.txt","r")
general_list_women = []
lines_women = in_file.readlines()
line_count_2 = 0
while line_count_2 < len(lines_women):
    list_3 = []
    for j in lines_women[line_count_2].split(":"):
        list_3.append(j)
    general_list_women.append(list_3)
    line_count_2 = line_count_2 + 1
j = 0
while j < len(general_list_women):
    c = "".join(general_list_women[j][1])
    d = c.split(",")
    general_list_women[j][1] = d
    j = j + 1
in_file.close()




randomly_select_men = []
randomly_select_women = []
def randomly_select():
    all_men = []
    all_women = []
    count = 0
    while count < len(general_list_men):
        all_men.append(general_list_men[count][0])
        all_women.append(general_list_women[count][0])
        count = count + 1
    for i in range(5): #5 person,it means 5 random choice
        random_men = random.choice(all_men)
        random_women = random.choice(all_women)
        randomly_select_men.append(random_men)
        randomly_select_women.append(random_women)

randomly_select()
print "Invited Males==",randomly_select_men
print "Invited Females==",randomly_select_women

uptadeList = []
def uptade():

    for men in randomly_select_men:
        each_men_uptadeList=["","","","","","","","",""]
        k = 0
        while k < len(general_list_men):
            if general_list_men[k][0] == men:
                for women in randomly_select_women:
                    women = " "+str(women) #if i do not use " "+str(women),any women element won't match
                                            #general_list_men[k][1][z]
                    z = 0
                    while z <= 9:
                        if general_list_men[k][1][z] == women:
                            each_men_uptadeList[z] = women
                        z = z + 1
            k = k + 1
        uptadeList.append(each_men_uptadeList)
uptade()


q = 0
while q < len(uptadeList):
    p = 0
    while p < len(uptadeList[q]):
        if uptadeList[q][p] == " ": #just i want to delete "" this sign from my each_men_uptadeList
            del uptadeList[q][p]
        p = p + 1
    q = q + 1

one_marvel_man = 0
their_best_list = 0
while one_marvel_man < len(randomly_select_men):
    print "For","".join(randomly_select_men[one_marvel_man]),"his uptade list",uptadeList[their_best_list]
    their_best_list=their_best_list + 1
    one_marvel_man = one_marvel_man + 1



#Mehmet Ozan Guven
#220201036

