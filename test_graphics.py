import matplotlib.pyplot as plt
from matplotlib.pyplot import ginput
import sys

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")



plt.grid()

def bres(x1, y1, x2, y2):
  xcoords = []
  ycoords = []
  dx = x2 - x1
  dy = y2 - y1

  # Determine increment direction
  x_inc = 1 if dx > 0 else -1
  y_inc = 1 if dy > 0 else -1

  # Handle if x1 > x2 or y1 > y2
  if dx < 0:
    dx = -dx
  if dy < 0:
    dy = -dy

  # Initialize decision parameter
  p = 2*dy - dx

  x = x1
  y = y1

  # Plot initial point
  xcoords.append(x)
  ycoords.append(y)
  # Iterate through line
  while x != x2:
    x += x_inc
    if p > 0:
      y += y_inc
      p += 2*dy - 2*dx
    else:
      p += 2*dy

    # Plot point
    xcoords.append(x)
    ycoords.append(y)

  try:
    plt.plot(xcoords, ycoords)
    plt.show()
  except Exception as e:
    print("Plot error:", e)


def main():
    #x1 = int(input("Enter the Starting point of x: "))
    #y1 = int(input("Enter the Starting point of y: "))
    #x2 = int(input("Enter the end point of x: "))
    #y2 = int(input("Enter the end point of y: ")) 
    
    if len(sys.argv) != 5:
        sys.exit("Hint: x1 y1 x2 y2")

    coords = sys.argv[1:] 

    x1 = int(coords[0])
    y1 = int(coords[1])
    x2 = int(coords[2]) 
    y2 = int(coords[3])
    try:
         bres(x1, y1, x2, y2)
       # bres(int(coords[0]),int( coords[1]),int( coords[2]),int( coords[3]))
    except Exception as e:
        print("Error in bres():", e)

if __name__ == "__main__":
    main()


