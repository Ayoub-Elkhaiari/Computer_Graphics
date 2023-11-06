#!/usr/bin/python3

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

if len(sys.argv) != 5:
    sys.exit("Hint: xd yd xf yf <four_arguments>")

coords = sys.argv[1:]
xd = int(coords[0])
yd = int(coords[1])
xf = int(coords[2])
yf = int(coords[3])

def setup_opengl():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham Line")
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 500, 0, 500)

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
    return list(zip(xcoords, ycoords))
# Draw points
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    pixels = bresenham(xd, yd, xf, yd)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)  # blue
    for x, y in pixels:
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    setup_opengl()  # Set up the OpenGL context
    glutDisplayFunc(draw)
    glutMainLoop()
    input("Press Enter to exit...")

main()

