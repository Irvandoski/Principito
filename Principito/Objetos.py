from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Objetos():
     def __init__(self,escalar):
        self.escalaX = 1 * escalar;
        self.escalaY = 16/9 * escalar
     def cuadro_pequeño(self):
        glClear(GL_COLOR_BUFFER_BIT)
        #fondo cabello
        glColor3ub(240, 240, 240)
        glBegin(GL_QUADS)
        glVertex2f(-0.40 * self.escalaX,  0.25 * self.escalaY)
        glVertex2f( 0.40 * self.escalaX,  0.25 * self.escalaY)
        glVertex2f( 0.40 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f(-0.40 * self.escalaX, -0.25 * self.escalaY)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.07 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f( 0.16 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f( 0.20 * self.escalaX, -0.43 * self.escalaY)
        glEnd()
        glFlush()
     def cuadro_grande(self):
        #fondo cabello
        glColor3ub(119, 66, 3)
        glBegin(GL_POLYGON)
        glVertex2f(-0.99, -0.61)
        glVertex2f(-0.99, -0.85)
        glVertex2f(-0.90, -0.99)
        glVertex2f( 0.90, -0.99)
        glVertex2f( 0.99, -0.85)
        glVertex2f( 0.99, -0.61)
        glVertex2f( 0.90, -0.47)
        glVertex2f(-0.90, -0.47)
        glEnd()
        glColor3ub(240, 240, 240)
        glBegin(GL_POLYGON)
        glVertex2f(-0.96, -0.61)
        glVertex2f(-0.96, -0.85)
        glVertex2f(-0.88, -0.94)
        glVertex2f( 0.88, -0.94)
        glVertex2f( 0.96, -0.85)
        glVertex2f( 0.96, -0.61)
        glVertex2f( 0.88, -0.52)
        glVertex2f(-0.88, -0.52)
        glEnd()
        glFlush()
