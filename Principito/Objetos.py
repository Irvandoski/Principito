from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Objetos():
     def __init__(self,escalar,w,h):
        self.escalaX = 1 * escalar;
        self.escalaY = 16/9 * escalar
        self.w = w
        self.h = h
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
     def Avioneta(self):
        #fondo cabello
        glColor3ub(255, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.30 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w, -0.07 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w, -0.13 * self.escalaY + self.h)
        glEnd()
        glColor3ub(200, 18, 18)
        glBegin(GL_POLYGON)
        glVertex2f( 0.28 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.23 * self.escalaX + self.w, -0.18 * self.escalaY + self.h)
        glVertex2f(-0.35 * self.escalaX + self.w, -0.08 * self.escalaY + self.h)
        glVertex2f(-0.27 * self.escalaX + self.w,  0.07 * self.escalaY + self.h)
        glVertex2f( 0.24 * self.escalaX + self.w,  0.23 * self.escalaY + self.h)
        glVertex2f( 0.30 * self.escalaX + self.w,  0.42 * self.escalaY + self.h)
        glVertex2f( 0.37 * self.escalaX + self.w,  0.27 * self.escalaY + self.h)
        glVertex2f( 0.33 * self.escalaX + self.w,  0.08 * self.escalaY + self.h)
        glEnd()
        glColor3ub(255, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.05 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w,  0.18 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.25 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w,  0.12 * self.escalaY + self.h)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.05 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w,  0.18 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.25 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w,  0.12 * self.escalaY + self.h)
        glEnd()
        glColor3ub(120, 120, 120)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.15 * self.escalaX + self.w,  0.08 * self.escalaY + self.h)
        glVertex2f(-0.12 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)

        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.13 * self.escalaX + self.w, -0.23 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.30 * self.escalaY + self.h)
        
        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.54 * self.escalaX + self.w, -0.12 * self.escalaY + self.h)
        glVertex2f(-0.52 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glEnd()