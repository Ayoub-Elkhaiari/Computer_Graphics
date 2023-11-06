#!/usr/bin/python3



import matplotlib.pyplot as plt 
import math
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
        plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
        plt.scatter(x,y, color="green")
        while x != xf :
            x = x+inc_x
            
            if s >= 0:
                y = y+inc_y
                s = s + 2*(dy-dx)
                xcoords.append(x)
                ycoords.append(y)
                plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
                plt.scatter(x,y, color="red")
            else :
                s = s + 2 * dy
                xcoords.append(x)
                ycoords.append(y)
                plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
                plt.scatter(x, y, color="red")
            
    else :
        s = 2 * dx - dy
        xcoords.append(x)
        ycoords.append(y)
        plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
        plt.scatter(x, y, color="red")        
        while y != yf :
            y = y+inc_y
            
            if s >= 0 :
                x = x+inc_x
                s = s + 2 * (dx - dy)
                xcoords.append(x)
                ycoords.append(y)
                plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
                plt.scatter(x, y, color="red")
            else:
                s = s +2 * dx
                xcoords.append(x)
                ycoords.append(y)
                plt.annotate(f"({x}, {y})", (x, y), size=8, bbox=dict(boxstyle="round", fc=(1.0, 1.0, 1.0, 0.0)))
                plt.scatter(x, y, color="red")
            
    print(xcoords)
    print(ycoords)
    plt.scatter(xf, yf, color="green")
    plt.plot(xcoords, ycoords, color="red")
   # return list(zip(xcoords, ycoords))
    new_list = []
    new_list.append(xcoords)
    new_list.append(ycoords)
    #return new_list 
   # print(list(zip(xcoords, ycoords)))
    


def draw_and_rotate(xd, yd, xf , yf, num_duplicates, theta):
    for _ in range(num_duplicates):
        bresenham(xd, yd, xf, yf)
        xf = xf*math.cos(theta) - yf*math.sin(theta)
        yf = xf*math.sin(theta) - yf*math.cos(theta)

def draw_and_duplicate(xd, yd, xf, yf, num_duplicates):
    lines = []
    for _ in range(num_duplicates):
        bresenham(xd, yd, xf, yf)
        xd += 1
    
        xf += 1
        
    

    
    


#def draw(xd, yd, xf, yf):
 #   bresenham(xd, yd, xf, yf)
  #  duplicate(xd, yd, xf, yf)
   # bresenham(xd, yd, xf, yf)
    



def main():

    if len(sys.argv) != 5:
        sys.exit("Hint: xd yd xf yf <four_arguments>")

    coords = sys.argv[1:]

    xd = int(coords[0])
    yd = int(coords[1])
    xf = int(coords[2])
    yf = int(coords[3])

    
    #draw_and_duplicate(xd , yd, xf, yf, 6)
    draw_and_rotate(xd, yd, xf, yf, 6 , 45)
    plt.show()




main() 
