car_list=[['BMW',4,False,200],['Mercedes',3,False,250],['Renault',2,False,150],['Audi',3,False,180]]

def add_new_car(brand,horsepower,carlist):
    added_car = []
    number = 0
    for car in carlist:
        for j in car:
            if j == brand:
                carlist[number][1] += 1
                return carlist

        number = number + 1
    else:
        added_car.append(brand)    #first i am adding new car to added_car list then i will add car_list
        added_car.append(1)
        added_car.append(False)
        added_car.append(horsepower)
        carlist.append(added_car)
        return carlist
#print add_new_car(..,..,..,)

def sell_car(brand,carlist):
    count = 0
    for car in carlist:     #first count = 0 and i control brand if it does not find ,loop again now count = 1 and i
        for i in car :      #control again brand.this fucntion repeat this if i find brand
            if i == brand:
                carlist[count][1] = carlist[count][1]- 1
                if carlist[count][1] < 0:
                    print "We do not have",brand,"car"
                    exit()
                break
        count = count +1
    return carlist


def rent_car (brand,carlist):
    count = 0
    for car in carlist:
        for i in car:
            if i == brand:
                carlist[count][2] = "True"
                if carlist[count][1] <= 0:
                    print "We do not have",brand,"car"
                    exit()
                break
        count = count +1
    return carlist




def return_car (brand,carlist):
    count = 0
    for car in carlist:
        for i in car:
            if i == brand:
                if carlist[count][2] == "True":
                    carlist[count][1] += 1
                    carlist[count][2] = "False"
        count = count + 1
    return carlist



def give_car_list (upper,lower,carlist):
    suggested_car=[]
    count = 0
    for car in carlist:
        if lower <= carlist[count][3] <= upper:
            suggested_car.append(carlist[count])

        count = count + 1
    return suggested_car



#Name and Surname = Mehmet Ozan Guven
#Student ID =220201036
































