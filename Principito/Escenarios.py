from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
class Escenas(object):
    def __init__(self):
        self.escalaX = 1 
        self.escalaY = 16/9 
 
    def escena1(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3ub(255, 255, 250)
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(-1,  1)
        glColor3ub(77, 102, 255)
        glVertex2f( 1,  1)
        glVertex2f( 1, -1)
        glEnd()
        glFlush()