list_1=[]
def read_text():
    in_file = open("student_grades.txt","r")
    for line in in_file:
        list_1.append(line.splitlines())
    in_file.close()
read_text()

i = 0
for elements in list_1:
    string="".join(elements)#before delete i have to convert string
    delimeter = ";" #first i delete this ";"
    nElement=string.split(delimeter)
    string_2 ="".join(nElement)
    delimeter_2 = ":"#then i delete this ":"
    n2Element=string_2.split(delimeter_2)
    newElement ="".join(n2Element)#before delete i have to convert string
    list_1[i]=newElement.split()
    i = i + 1

list_average_midterm = []
def average_grades_midterms(index, alist):
    if index > 19:#base case:when i come 20,there is no 20. element in the list.That's why python will give an error
        return list_average_midterm
    else:
        #first i am collecting,then *20/100
        average_midterm=(float(alist[index][1])+float(alist[index][2]))*20.0/100.0
        list_average_midterm.append(average_midterm)
        return average_grades_midterms(index + 1, alist)
average_grades_midterms(0, list_1)

list_average_final = []
def average_grades_final(index,alist):
    if index > 19 :
        return list_average_final
    else:
        average_final = float(alist[index][3])*40/100
        list_average_final.append(average_final)
        return average_grades_final(index+1,alist)
average_grades_final(0,list_1)

list_average_homeworks=[]
def average_grades_homeworks(index,alist):
    if index > 19:#base case:when i come 20,there is no 20. element in the list.That's why python will give an error
        return list_average_homeworks
    else:#first i am collecting,then *5/100
        average_homeworks=(float(alist[index][4])+float(alist[index][5])+float(alist[index][6])+
                           float(alist[index][7]))*5/100
        list_average_homeworks.append(average_homeworks)
        return average_grades_homeworks(index+1,alist)
average_grades_homeworks(0,list_1)

totally_grades = []
j = 0
while j < len(list_1):
#when i found each notes(homework,midterm  and final),then i am collecting 1.element of  list_homework final and midterm
#it goes like that
    totally =list_average_homeworks[j]+list_average_final[j]+list_average_midterm[j]
    totally_grades.append(totally)
    j = j + 1

with_letter_grades=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#i defined empty list which is same list_1
def letter_grades(alist,index,list_1):
    if index > 19 :#base case:when i come 20,there is no 20. element in the list.That's why python will give an error
        return with_letter_grades
    else:#up to here i did not sort my list.It means, first element of totally_grades belongs to first name of list_1
        #which i calculated when i am reading txt
        if totally_grades[index]<= 49 and totally_grades[index]>=0:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("FF")
        elif totally_grades[index]<= 59 and totally_grades[index]>49:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("FD")
        elif totally_grades[index]<=64 and totally_grades[index] >59:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("DC")
        elif totally_grades[index]<=74 and totally_grades[index]>64:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("CC")
        elif totally_grades[index]<=79 and totally_grades[index]>74:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("CB")
        elif totally_grades[index]<=84 and totally_grades[index]>79:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("BB")
        elif totally_grades[index]<=89 and totally_grades[index]>84:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("BA")
        elif totally_grades[index]<=100 and totally_grades[index]>89:
            with_letter_grades[index]= list_1[index][0] + str(":"), str(totally_grades[index]), ";" + str("AA")
        #lines 70-85 this part for letter grades
        return letter_grades(alist,index+1,list_1)
letter_grades(with_letter_grades,0,list_1)

def sort_list(alist,index):#then i sort my last uptade list
    if index > 19 :#base case:when i come 20,there is no 20. element in the list.That's why python will give an error
        return alist
    else:#buble sort
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i][1]>alist[i+1][1]:
                    temp=alist[i]
                    alist[i]=alist[i+1]
                    alist[i+1]=temp
        return sort_list(alist,index+1)
sort_list(with_letter_grades,0)
final_list=with_letter_grades[::-1]#with_letter_grades is sorted from lower point to high point
#but we want to ask opposite way.

for each_student in final_list:
    print each_student #this my last uptade list

def re_write(alist):
    new_file=open("student_grades.txt","w")#i open same file with "w"
    for index in range(len(alist)):
        new_file=open("student_grades.txt","a")#for each loop i am uptading file.
        new_file.write(alist[index][0]+alist[index][1]+alist[index][2]+"\n")
    new_file.close()
re_write(final_list)
exit()

#Name=Mehmet Ozan
#Surname=Guven
#Student ID=220201036