#!/usr/bin/python3



import matplotlib.pyplot as plt
import sys

plt.title("bresenham")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid()

def bresenham(xd, yd, xf, yf):

    
    #dx = abs(xf - xd)
    #dy = abs(yf - yd)
    dx = xf - xd 
    dy = yf - yd 
    inc_x = 1 if dx > 0 else -1
    inc_y = 1 if dy > 0 else -1

    if dx < 0 :
        dx = -dx
    if dy < 0 :
        dy = -dy


    xcoords = []
    ycoords = []

    x = xd 
    y = yd 
    
     

    if dx > dy  :

        s = 2*dy - dx
        xcoords.append(x)
        ycoords.append(y)
        
        while x != xf :
            x = x+inc_x
            
            if s >= 0:
                y = y+inc_y
                s = s + 2*(dy-dx)
                xcoords.append(x)
                ycoords.append(y)
            else :
                s = s + 2 * dy
                xcoords.append(x)
                ycoords.append(y)
            
    else :
        s = 2 * dx - dy
        xcoords.append(x)
        ycoords.append(y)
                
        while y != yf :
            y = y+inc_y
            
            if s >= 0 :
                x = x+inc_x
                s = s + 2 * (dx - dy)
                xcoords.append(x)
                ycoords.append(y)
            else:
                s = s +2 * dx
                xcoords.append(x)
                ycoords.append(y)
            
    print(xcoords)
    print(ycoords)
    plt.plot(xcoords, ycoords)
    plt.show()
        

    
    
    



def main():

    if len(sys.argv) != 5:
        sys.exit("Hint: xd yd xf yf <four_arguments>")

    coords = sys.argv[1:]

    xd = int(coords[0])
    yd = int(coords[1])
    xf = int(coords[2])
    yf = int(coords[3])


    bresenham(xd, yd, xf, yf)

    #plt.show()




main() 
