import random
import sys
import time
sys.setrecursionlimit(10**6)  # Aumentando el limite de recursiones

carsList = []
destinationDic = {'Los Angeles': 0,'New Orleans': 1, 'Miami': 2, 'New York': 3} # Dado el destino (String) retorna su indice de orden correspondiente (Int)
colorDic = {'Red': 0, 'Green': 1, 'Blue': 2} # Dado el color (String) retorna su indice de orden correspondiente (Int)

# Clase Car (Tiene la estructura que necesita el carro)
class Cars:
    __slots__ = ['serialNumber', 'color', 'destination']

    def __init__(self, serialNumber, color, destination):
        self.serialNumber = serialNumber
        self.color = color
        self.destination = destination
    carsList = []

def createCars(): # Genera la cantidad de carros dada en el rango
    for x in range(12000):
        # Escoge un color aleatorio del arreglo
        randomColor = str(random.choice(['Red', 'Green', 'Blue']))
        # Escoge un destino aleatorio del arreglo
        randomDestination = str(random.choice(
            ['Los Angeles', 'New Orleans', 'Miami', 'New York']))
        currentCar = Cars((x+1), randomColor, randomDestination)
        carsList.append(currentCar)

def quickSort(List, dic):
    if(len(List) <= 1):
        return List
    else:
        lef = []
        right = []
        pivotCar = List.pop()
        if dic == destinationDic:
            pivotValue = dic[pivotCar.destination]
            for car in List:
                if(dic[car.destination] > pivotValue):
                    right.append(car)
                else:
                    lef.append(car)
        else:
            pivotValue = dic[pivotCar.color]
            for car in List:
                if(dic[car.color] > pivotValue):
                    right.append(car)
                else:
                    lef.append(car)
        return quickSort(lef, dic)+[pivotCar]+quickSort(right, dic)

def Sort(ListByDestination):
    global colorDic
    sortedList = []  # Contiene todo ya ordenado
    tempCarList = []
    for i in range(len(ListByDestination)):
        Currentdestination = ListByDestination[i].destination
        tempCarList.append(ListByDestination[i])
        if ((i+1) < len(ListByDestination)):
            if(Currentdestination != ListByDestination[(i+1)].destination):
                sortedList += quickSort(tempCarList, colorDic)
                tempCarList = []
        else:
            sortedList += quickSort(tempCarList, colorDic)
            tempCarList = []
    return sortedList

def generateTxtFile(list, name):
    fh = open(name, 'w')
    for car in list:
        fh.write((str(car.serialNumber)+" "+str(car.color) +" "+str(car.destination)+"\n"))
    fh.close()
    print(str(name)+" "+'Created')

start = time.time()
print('--------------------------')
createCars()#create all the cars
print('Cars created')
print('---------------------------')
generateTxtFile(carsList, "cars.txt")# generates the unsorted list
generateTxtFile(Sort(quickSort(carsList, destinationDic)),"sorted_colors.txt")# generates the sorted list
end = time.time()
print('El tiempo necesario fue :'+str(round(end - start))+" Segundos")

