from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
move=0
f=False

def deadmau5():
 #   global move
  #  global f
   # glClearColor(0.1,0.1,0.1,0)
    glColor(0.55, 0.8, 0)
    glBegin(GL_POINTS)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = 0.4 * cos(theta)
        y = 0.3 * sin(theta)
        glVertex2d(x-0.5, y+0.7)
    glEnd()
    glFlush()

    glColor(0.55, 0.8, 0)
    glBegin(GL_POINTS)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = 0.4 * cos(theta)
        y = 0.3 * sin(theta)
        glVertex2d(x+0.5, y +0.7)
    glEnd()
    glFlush()
#his ears looool


    glColor(0.05, 0.05, 0.05)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.1):
        x = 0.45 * cos(theta)
        y = 0.35 * sin(theta)
        glVertex2d(x, y +0.5)
    glEnd()
    glFlush()
###### his face


    glColor(0.87, 0, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.1):
        x = 0.14 * cos(theta)
        y = 0.11 * sin(theta)
        glVertex2d(x+0.28, y +0.55)
    glEnd()
    glFlush()


    glColor(0.87, 0, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.1):
        x = 0.14 * cos(theta)
        y = 0.11 * sin(theta)
        glVertex2d(x - 0.28, y + 0.55)
    glEnd()
    glFlush()

    glColor(0,1,0)
    glBegin(GL_LINES)
    glVertex(0.37,0.65)
    glVertex(0.19, 0.45)
    glVertex(0.17,0.65)
    glVertex(0.39, 0.45)

    glVertex(-0.37,0.65)
    glVertex(-0.19, 0.45)
    glVertex(-0.17,0.65)
    glVertex(-0.39, 0.45)


    glEnd()
    glFlush()


########### His eyes

    glColor(0,1 , 0.8)
    glBegin(GL_POLYGON)
    for theta in np.arange(0,-pi, -0.01):
        x = 0.37 * cos(theta)
        y = 0.28 * sin(theta)
        glVertex2d(x  , y+0.43)
    glEnd()
    glFlush()
######     HIS Mouth

    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3,0.145)
    glVertex2d(0.3,0.145)
    glVertex2d(0.3,-0.25)
    glVertex2d(-0.3, -0.25)
    glEnd()
    glFlush()

    glColor(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.2, 0.141)
    glVertex2d(0.2, 0.141)
    glVertex2d(0, -0.11)
    glEnd()
    glFlush()


    glColor(1,0 , 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.1, 0.14)
    glVertex2d(0,0.1)
    glVertex2d(0.1,0.14)
    glVertex2d(0.1,0.05)
    glVertex2d(0,0.08)
    glVertex2d(-0.1, 0.05)
    glEnd()
    glFlush()
############## his Body

    glColor(0.2,0.2,0.2)
    glBegin(GL_POLYGON)
    glVertex2d(0.3,-0.1)
    glVertex2d(0.5,-0.1)
    glVertex2d(0.5,-0.45)
    glVertex2d(0.3,-0.45)
    glEnd()
    glFlush()

    glColor(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.1)
    glVertex2d(-0.3, -0.1)
    glVertex2d(-0.3, -0.45)
    glVertex2d(-0.5, -0.45)
    glEnd()
    glFlush()

### HIS LEGS - WHEELS LOL -
    glColor(1,0.7,0)
    glBegin(GL_LINES)
    glVertex(0.3,-0.15)
    glVertex(0.5,-0.15)
    glVertex(0.3,-0.2)
    glVertex(0.5,-0.2)
    glVertex(0.3,-0.3)
    glVertex(0.5,-0.3)
    glVertex(0.3,-0.25)
    glVertex(0.5,-0.25)
    glVertex(0.3,-0.35)
    glVertex(0.5,-0.35)
    glVertex(0.3,-0.4)
    glVertex(0.5,-0.4)

    glVertex(-0.3,-0.15)
    glVertex(-0.5,-0.15)
    glVertex(-0.3,-0.2)
    glVertex(-0.5,-0.2)
    glVertex(-0.3,-0.3)
    glVertex(-0.5,-0.3)
    glVertex(-0.3,-0.25)
    glVertex(-0.5,-0.25)
    glVertex(-0.3,-0.35)
    glVertex(-0.5,-0.35)
    glVertex(-0.3,-0.4)
    glVertex(-0.5,-0.4)

    glEnd()
    glFlush()
#### LINES LOL
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3,0.145)
    glVertex2d(0.6, 0.3)
    glVertex2d(0.55,0.2)
    glVertex2d(0.3,0.1)

    glEnd()
    glFlush()


    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.6, 0.3)
    glVertex2d(0.55, 0.2)
    glVertex2d(0.75,0.05)
    glEnd()
    glFlush()

    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3, 0.145)
    glVertex2d(-0.6, 0.3)
    glVertex2d(-0.55, 0.2)
    glVertex2d(-0.3, 0.1)

    glEnd()
    glFlush()

    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.6, 0.3)
    glVertex2d(-0.55, 0.2)
    glVertex2d(-0.75, 0.05)
    glEnd()
    glFlush()


    glColor(0, 1, 0.8)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*pi, 0.01):
        x = 0.05 * cos(theta)
        y = 0.05 * sin(theta)
        glVertex2d(x+0.75, y + 0.05)
    glEnd()
    glFlush()

    glColor(0, 1, 0.8)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*pi, 0.01):
        x = 0.05 * cos(theta)
        y = 0.05 * sin(theta)
        glVertex2d(x-0.75, y + 0.05)
    glEnd()
    glFlush()

    glColor(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*pi, 0.001):
        x = 0.04 * cos(theta)
        y = 0.04 * sin(theta)
        glVertex2d(x-0.75, y + 0.035)
    glEnd()
    glFlush()

    glColor(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2*pi, 0.001):
        x = 0.04 * cos(theta)
        y = 0.04 * sin(theta)
        glVertex2d(x+0.75, y + 0.035)
    glEnd()
    glFlush()

#####HIS HANDS  &  ARMS
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global move
    global f
    glRotate(move,0,0,1)
    deadmau5()
''''''
    if move >20:
        f=True
    if move < -20:
        f=False
    if f:
        move-=0.5
    else:
        move+=0.5



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,600)
glutCreateWindow(b"k")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()