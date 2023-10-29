import matplotlib.pyplot as plt
from matplotlib.pyplot import ginput

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.xlim(0, 100)
plt.ylim(0, 100)

plt.grid()

def bres(x1,y1,x2,y2):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    s = 2*dy - dx
    i = 1
    xcoordinates = [x]
    ycoordinates = [y]
    while i <= dx:
        if s >= 0:
            x = x+1 
            y = y+1
            s = s + 2*(dy-dx)
            i = i+1
            xcoordinates.append(x)
            ycoordinates.append(y)
        else:
            x = x+1
            s = s + 2*dy
            i = i+1
            xcoordinates.append(x)
            ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))
    bres(x1, y1, x2, y2)



main()


