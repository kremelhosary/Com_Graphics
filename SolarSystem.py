from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

theta = 0
alpha = 0


def init():
    glClearColor(0.051, 0.051, 0.051, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(90, 1, 1, 3050)
    gluLookAt(50, 10, 100, 0, 0, 0, 0, 1, 0)
   # glEnable(GL_DEPTH_TEST)

zx=0
def SolarSystem():
    glClear(GL_COLOR_BUFFER_BIT )
    global zx
    global theta
    global alpha




    glLoadIdentity()
    glColor(1,1,1)
    glTranslate(0, 0, 0)
    glRotate(zx,0,0,1)
    glTranslate(0,0,0)
    glutWireSphere(4, 10, 10)

    glLoadIdentity()
    glColor(0,0,0)
    glTranslate(0, 0, 0)
    glRotate(zx,0,0,1)
    glTranslate(0,0,0)
    glutSolidSphere(4, 30, 30)  # el nayzak

    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(1, 1, 0)
    glutSolidSphere(4, 30, 30)  # Sun



    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(0.7, 0.5, 0.5)
    glRotate(-theta, 0, 1, 0)
    glTranslate(5.5, 0, 0)
    glRotate(theta * 1.5, 0, 1, 0)
    glutSolidSphere(0.5, 10, 10)  # 3tard


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 7.5, 50, 50)


    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(1, 0.7, 0)
    glRotate(-theta / 1.2, 0, 1, 0)
    glTranslate(7.5, 0, 0)
    glRotate(theta * 1.5, 0, 1, 0)
    glutSolidSphere(0.75, 20, 20)  # elzohra


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 11, 50, 50)

    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glRotate(-theta / 1.5, 0, 1, 0)
    glTranslate(11, 0, 0)
    glColor(0, 0.5, 1)
    glScale(2.5,0.5,2.5)
    glutSolidSphere(1,20,20)  # Earth


    #glRotate(theta, 0, 1, 0)
    #glutSolidSphere(1, 30, 30)  # Earth

    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glRotate(-theta / 1.5, 0, 1, 0)
    glTranslate(11, 0, 0)
    glColor(0.8, 0.8, 0.8)
    glRotate(-theta, 0, 1, 1)
    glRotate(20, 0, 0, 1)
    glTranslate(1.5, 0, 0)
    glRotate(theta * 4, 0, 1, 0)
    glutSolidSphere(0.25, 15, 15)  # Moon


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 15, 50, 50)


    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(1, 0.2, 0)
    glRotate(-theta / 1.7, 0, 1, 0)
    glTranslate(15, 0, 0)
    glRotate(theta * 1.5, 0, 1, 0)
    glutSolidSphere(0.6, 10, 10)  # Mars


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 20, 50, 50)

    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(1, 0.1, 0)
    glRotate(-theta / 2, 0, 1, 0)
    glTranslate(20, 0, 0)
    glRotate(theta * 1.5, 0, 1, 0)
    glutSolidSphere(2.7, 30, 25)  # Jupiter


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 26, 50, 50)

    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(0.8, 0, 0)
    glRotate(-theta / 2.5, 0, 1, 0)
    glTranslate(26, 0, 0)
    glRotate(theta * 1.8, 0, 1, 0)
    glutSolidSphere(2.5, 30, 25)  # Saturn


    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
    glColor(0.5,0.5,0.5)
    glRotate(-theta/2.5,0,1,0)
    glTranslate(26,0,0)
    glRotate(-theta,0,1,0)
    glRotate(30, 0, 1, 0)
    glRotate(90, 1, 0, 0)
    glScale(1, 1, 0.01)
    glutSolidTorus(0.4,3.2,20,20)    #saturn belt


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 35, 50, 50)


    glLoadIdentity()
    glRotate(zx,0,1,0)
    glTranslate(50,0,0)
#    glScale(0.2,0.2,0.2)
    glColor(0.0, 0.5, 0.7)
    glRotate(-theta / 3, 0, 1, 0)
    glTranslate(35, 0, 0)
    glRotate(theta * 1.8, 0, 1, 0)
    glutSolidSphere(1.2, 30, 25)


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(zx, 0, 1, 0)
    glTranslate(50, 0, 0)
    glRotate(90,1,0,0)
    glutSolidTorus(0.01, 31, 50, 50)


    glLoadIdentity()

 #   glScale(0.2,0.2,0.2)
    glColor(0.1, 0.1, 0.7)
    glRotate(-theta / 2.8, 0, 1, 0)
    glTranslate(31, 0, 0)
    glRotate(theta * 1.8, 0, 1, 0)
    glutSolidSphere(1.5, 30, 25)


    theta = theta + 0.1
    alpha = alpha + 0.01

    zx=zx+0.01


def draw():
    SolarSystem()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(700, 700)
glutCreateWindow(b"my Solar... mine")
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
