import math
from math import cos, sin, tan
from math import exp, pi



def	teilbar(x, y):
        if  y == 0:
            print("Es ist nicht möglich durch 0 zu teilen")
        elif x % y == 0 and x != y:
            print(str(x) + " ist durch " + str(y) + " teilbar")
        elif x % y != 0:
            print(str(x) + " ist nicht durch " + str(y)  + " teilbar")
        else:
            print(str(x) + " und " + str(y) + " sind gleich")
    
#Code voin derm Dozenten:

def teilen(x,y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x == y:
        print("x und y sind gleich")
    else: 
        if x % y == 0:
            print("x ist durch y durch y teilbar")
        else: 
            print("x ist nicht durch y teilbar")
