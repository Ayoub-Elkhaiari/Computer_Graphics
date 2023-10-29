import matplotlib.pyplot as plt 
from matplotlib.pyplot import ginput

# function for line generation 
def bresenham(x1, y1, x2, y2): 
  
    
    dx = x2 - x1 
    dy = y2 - y1 

    stepx = 1 if dx > 0 else -1 
    stepy = 1 if dy > 0 else -1 

    s = 2*dy - dx
    x = x1
    y = y1

    xcoords = [x]
    ycoords = [y]

    while x != x2 :
        x = x + stepx
        if s >= 0 :
            y = y + stepy
            s = s + 2*dy - 2*dx
        else:
            s = s + 2*dy
            

        plt.plot(x,y)
     #   xcoords.append(x)
    #    ycoords.append(y)
   # plt.plot(xcoords, ycoords)
  
# Driver code 
if __name__ == '__main__': 
    #x1 = 3
    #y1 = 2
    #x2 = 15
    #y2 = 5
    plt.title("Graphics")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.grid()

    plt.show()
    x1, y1 = ginput(1)[0]
    x2, y2 = ginput(1)[0]
  
    # Function call 
    bresenham(x1, y1, x2, y2) 
  
