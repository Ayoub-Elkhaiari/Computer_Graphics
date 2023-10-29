#!/usr/bin/python3



import matplotlib.pyplot as plt 
import sys






plt.xlabel("X")
plt.ylabel("Y")

plt.grid()

def bresenham(x1, y1, x2, y2):

  dx = x2 - x1
  dy = y2 - y1

  # hna ghankhtaro wach n icrementiw wela la 
  x_inc = 1 if dx > 0 else -1
  y_inc = 1 if dy > 0 else -1

  # l rapport dyalhom bach nakhdo decision 
  steep = abs(dy) > abs(dx)

  if steep:
    # hna bedelna dx b dy bach fblast man decrementiw x fl 2eme octant n incrementiw y
    dx, dy = dy, dx

  # initialisina x hna 
  d = 2*dx - dy

  # Start at (x1, y1)
  x = x1
  y = y1

  # 7atina awal no9ta o derna liha scatter fl graph bach nchofo wach droite kaydoz mnha 
  xcoords = [x]
  ycoords = [y]
  plt.scatter(x, y)  

  # Main loop
  while x != x2:
    x += x_inc

    # 3la 7ssab rapport dyal dy / dx ghanakhdo decision ya3ni kaykon ima true wela false bach n3arfo rassna ina cas ina octant 
    if steep:
      if d <= 0:
        d += 2*dx
      else:
        d += 2*(dx - dy)
        y += y_inc
    else:
      if d >= 0:
        d += 2*dy
      else:
        d += 2*dy
        y += y_inc

    # Plot point
    xcoords.append(x)
    ycoords.append(y)
    plt.scatter(x, y)

  print(xcoords)
  print(ycoords)
  try:
    plt.plot(xcoords, ycoords)
    plt.show()
  except Exception as error :
      print("<Error> in plot: ", error)


def main():


    if len(sys.argv) != 5:
        sys.exit("Hint: x1 y1 x2 y2 <four_arguments>")
    coords = sys.argv[1:]



    x1 = int(coords[0])
    y1 = int(coords[1])
    x2 = int(coords[2])
    y2 = int(coords[3])
    
    try:
        bresenham(x1, y1, x2, y2)
    except Exception as error :
        print("<ERROR> in bresenham(): ", e)

    




main()
