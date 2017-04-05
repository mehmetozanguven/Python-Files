correct = True
while correct: #with this while loop i am checking that whether first DNA longer than second DNA
    input1 = raw_input("Please enter a DNA==")
    input2 = raw_input("Please enter a 2. DNA.PAY ATTENTION!! Your second DNA can not be longer than your first DNA==")
    dna_1 = input1.upper()
    dna_2 = input2.upper()
    list_dna_1 = list(dna_1)
    list_dna_2 = list(dna_2)
    if len(list_dna_1) >= len(list_dna_2):
        correct = False
    else:
        print "Remember!! Your second DNA can not be longer than your first DNA"

def checking_DNA_and_RNA(list_1,list_2):
    if "U" in list_1:  #if "U" in the list,it means entered input from user shows that it is a RNA
        print "False.We are turning of -Your First Input- RNA to DNA"
    elif "U" not in list_1:
        print "True"
    if "U" in list_2 :
        print "False.We are turning of -Your Second Input- RNA to DNA"
    else:
        print "True"
checking_DNA_and_RNA(list_dna_1,list_dna_2)

def converting_nucleoside(list_1,list_2):
    if "U" in list_1:
        i = 0
        while i < len(list_1):   #these while loops convert RNA to DNA
            if list_1[i] == "G":
                list_1[i] = "C"
            elif list_1[i] == "C":
                list_1[i] = "G"
            elif list_1[i] == "A":
                list_1[i] = "T"
            elif list_1[i] == "U":
                list_1[i] = "A"
            i = i + 1
        print "Your first RNA converted to DNA:"
        print "".join(list_1)
    if "U" in list_2:
        i = 0
        while i < len(list_2):
            if list_2[i] == "G":
                list_2[i] = "C"
            elif list_2[i] == "C":
                list_2[i] = "G"
            elif list_2[i] == "A":
                list_2[i] = "T"
            elif list_2[i] == "U":
                list_2[i] = "A"
            i = i + 1
        print "Your second RNA converted to DNA:"
        print "".join(list_2)
converting_nucleoside(list_dna_1,list_dna_2)

similarity_list = []#i will append each similarity values this list
def similarity_between_two_DNAs(list_1,list_2):
    lenght_of_list_1 = len(list_1)
    lenght_of_list_2 = len(list_2)
    count = 0
    while lenght_of_list_2 <= lenght_of_list_1 :
        checking_for_similarity = list_1[count:lenght_of_list_2]
        i = 0
        common_nucleodid = 0
        while i < len(checking_for_similarity):
            if checking_for_similarity[i]== list_2[i]:
                common_nucleodid= common_nucleodid + 1
            i = i + 1
        similarity = ((float(common_nucleodid)/float(len(list_2)))*100)
        similarity_list.append(similarity)
        count = count + 1
        lenght_of_list_2 = lenght_of_list_2 + 1
similarity_between_two_DNAs(list_dna_1,list_dna_2)
similarity_list.sort() #for the taking maxiumun value
print "The maximum similarity is %",similarity_list[-1] # using[-1], i am calling last number of the similarity list

#Mehmet Ozan Guven
#220201036

