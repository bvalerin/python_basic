def saludar(stringName):
    print("Hola " + stringName + "! Como estas?")

def printData(iterableItem):
    for item in iterableItem:
        print(item)

def getPiValue():
    print(3.14)

list = []
printData(list)

mi_tupla = (1, 2, 3, 1, "Hola", True)
printData(mi_tupla)

mySet = {1, 2, 3, 3}
printData(mySet) #Cuando llamo a la funcion le debo enviar un objeto iterable

def isEven(number):
    if number % 2 == 0 :
         return str(number) + " es par" 
    return str(number) + " es impar"

numbers = [1,2,3,4,5,6,7,8,9,10] #Cuales con pares?
for num in numbers:
    print(isEven(num))


print(sumar(4, 5))


















