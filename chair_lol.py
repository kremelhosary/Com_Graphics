from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
global x
global y
global z

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,15,25,0,0,0,0,1,0)

def cube(x,y,z,r,g,b):
    glPushMatrix()
    glColor(r,g,b)
    glScale(x,y,z)
    glutWireCube(2)
    glPopMatrix()

def chair(x,y,z):
    glPushMatrix()
    glTranslate(x,y,z)
    cube(4, 1, 3, 0, 0, 0)
    glTranslate(0, 4, -2)
    cube(4, 3, 1, 0, 0, 0)
    glLoadIdentity()
    glTranslate(x,y,z)
    glTranslate(3.5, -3, 2.5)
    cube(0.5, 2, 0.5, 0, 0, 0)
    glLoadIdentity()
    glTranslate(x, y, z)
    glTranslate(3.5, -3, -2.5)
    cube(0.5, 2, 0.5, 0, 0, 0)
    glLoadIdentity()
    glTranslate(x, y, z)
    glTranslate(-3.5, -3, -2.5)
    cube(0.5, 2, 0.5, 0, 0, 0)
    glLoadIdentity()
    glTranslate(x, y, z)
    glTranslate(-3.5, -3, 2.5)
    cube(0.5, 2, 0.5, 0, 0, 0)
    glPopMatrix()

def draw():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)


    chair(-3,0,0)
    chair(8,0,0)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"looool")
myinit()
glutDisplayFunc(draw)
#glutIdleFunc(draw)
glutMainLoop()

