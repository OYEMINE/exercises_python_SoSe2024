def steigung_function(liste):
        x1 = liste[0]
        y1 = liste[1]
        x2 = liste[2]
        y2 = liste[3]
        dy = y2-y1
        dx = x2-x1
        if x1 == x2:
            print("Die Steigung ist nicht definiert")
        else:
            print(dy/dx)
