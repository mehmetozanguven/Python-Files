def function_0():
    in_file = open("nucleic_acid.txt","r")
    lines =in_file.readlines()
    list_1 = []
    for i in lines:
        list_1.append(i.split())
    in_file.close()
    return list_1
first_uptade_list = function_0()

#when i check nucleic acid valid or not (it is checking function_1),i divided two to problem
#first part is checking whether x or y in the list(i know the nucleic.acid.txt and also i know
#which one string cause problems)
def function_1_part_1(list_1, index, boundary):
    if index < 0 :#base case,when index < 0,it means,i checked all elements in the list
        return list_1#if i continue,i will check again all elements in the list
    else:
        for i in boundary:#thansk to loop boundary,i am checking each elements in the list
            if "X" in list_1[index][i]:#when i find X...
                b = "".join(list_1[index][1]) + " " + str(-1)
                list_1[index][1]=b
        for j in boundary:
            if "Y" in list_1[index][j]:#when i find Y
                b = "".join(list_1[index][1]) + " " + str(-1)
                list_1[index][1]=b
        return function_1_part_1(list_1, index - 1, [0, 1])
second_uptade_list =function_1_part_1(first_uptade_list, len(first_uptade_list)-1,[0,1])
#for the second part if T and U exist in any elements of list,i will take the elements
#and uptade the elements with -1
def function_1_part_2(list_1, index_1, boundary_2):
    if index_1 < 0:  #base case,when index < 0,it means,i checked all elements in the list
        return list_1 #if i continue,i will check again all elements in the list
    else:
        for i in boundary_2:
            if "U" in list_1[index_1][i]:
                if "T" in list_1[index_1][i]:
                    b = "".join(list_1[index_1][1]) + " " + str(-1)
                    list_1[index_1][1]=b
        return function_1_part_2(list_1, index_1 - 1, boundary_2)
third_uptade_list=function_1_part_2(second_uptade_list, len(second_uptade_list)-1, [0,1])

print "Pay Attention! If nucleic acid has U,it means that RNA and we are going to write False\n" \
      "The others case,it means that DNA and we are goint to write True"
#with fucntion_2,i am checking which elements in the list DNA or RNA,then i return with print False or True
def function_2(list_1, index, boundary_2):
    if index < 0:  #base case,when index < 0,it means,i checked all elements in the list
        return list_1  #if i continue,i will check again all elements in the list
    else:
        for i in boundary_2:
            if "-1" in list_1[index][1]:#it is not necessary checking elements which have -1
                continue                #because these acid are not valid
            elif "U" in list_1[index][i]:
                print "Your",index+1,". nucleic acid",i+1,". part is RNA",False
            else:

                print "Your",index+1,".nucleic acid",i+1,".part is DNA",True
        return function_2(list_1, index - 1, [0, 1])
fourth_uptade_list = function_2(third_uptade_list,len(third_uptade_list)-1,[0,1])

#with fucntion 3,i am converting DNA to RNA
def function_3(list_1, index, boundary):
    if index < 0: #base case,when index < 0,it means,i checked all elements in the list
        return list_1 #if i continue,i will check again all elements in the list
    else:
        for i in boundary:
            if "-1" in list_1[index][1]:#it is not necessary checking elements which have -1
                continue                #because these acid are not valid
            elif "T" in list_1[index][i]:#if any element has T,it means that DNA
                continue
            else:

                j = 0
                while j < len(list_1[index][i]):
                    if list_1[index][i][j]== "G":
                        for_convert = list(list_1[index][i])# i can not change any elements without converting list
                        for_convert[j]="C"   #That's why first i am converting list then again converting string
                        string="".join(for_convert)
                        list_1[index][i] = string

                    elif list_1[index][i][j] == "C":
                        for_convert = list(list_1[index][i])
                        for_convert[j]="G"
                        string="".join(for_convert)
                        list_1[index][i] = string

                    elif list_1[index][i][j] == "A":
                        for_convert = list(list_1[index][i])
                        for_convert[j]="T"
                        string="".join(for_convert)
                        list_1[index][i] = string

                    elif list_1[index][i][j] == "U":
                        for_convert = list(list_1[index][i])
                        for_convert[j]="A"
                        string="".join(for_convert)
                        list_1[index][i] = string
                    j = j + 1
        return function_3(list_1,index - 1, boundary)
fifth_uptade_list= function_3(fourth_uptade_list,len(fourth_uptade_list)-1,[0,1])


#with fucntion 4,i am finding difference between two DNAS
def function_4(list_1,index):
    if index > 9:#base case:when index 9,it means i checked all elements in the list
        return list_1 #if i go on,python will give error(list index out of range)
    else:
            if "-1" in list_1[index][1]:#i do not care about elements which has -1
                pass
            else:#first i have decided which elements' len longer
                if len(list_1[index][0]) >= len(list_1[index][1]):
                    first_dna = list_1[index][0]
                    second_dna = list_1[index][1]
                else:
                    first_dna = list_1[index][1]
                    second_dna =list_1[index][0]
                j = 0
                similarity =0#then i calculated similarity between two DNAs
                while j < len(second_dna):
                    if first_dna[j]==second_dna[j]:
                        similarity =similarity + 1
                    j = j + 1
                difference_between_two_DNAs=len(first_dna)-similarity#after that subtrack longer one from similarity
                string = "".join(list_1[index][1])+" "+str(difference_between_two_DNAs)
                list_1[index][1] = string #finally i am adding to element
            return function_4(list_1,index+1)
sixth_uptade_list= function_4(fifth_uptade_list,0)
#permanently for each functions,the list is upgrading

def function_6(list_1):#with this function i write last uptade list in the nucleic_acid.txt
    new_file = open("nucleic_acid.txt","w")
    for index in range(len(list_1)):
        new_file=open("nucleic_acid.txt","a")#for each loop i open nucleic acid with "a"
        new_file.write(list_1[index][0]+" ")
        new_file.write(list_1[index][1]+"\n")
    new_file.close()
function_6(sixth_uptade_list)
exit()
