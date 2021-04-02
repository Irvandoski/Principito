from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Principito(object):
    def __init__(self,escalar):
        self.escalaX = 1 * escalar;
        self.escalaY = 16/9 * escalar

    def PrincipitoFront(self):
        #SOLAPA ROJA
        glColor3ub(181, 54, 65)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.85 * self.escalaX, -0.85 * self.escalaY)
        glVertex2f( 0.80 * self.escalaX, -0.73 * self.escalaY)
        glVertex2f( 0.00 * self.escalaX,  0.00 * self.escalaY)
        glEnd()
        #TORSO
        glColor3ub(255, 255, 255)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX,  0.38 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.38 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX, -0.37 * self.escalaY)
        glVertex2f(-0.05 * self.escalaX, -0.37 * self.escalaY)
        glEnd()
        #PIERNA DERECHA
        glColor3ub(235,235,235)
        glBegin(GL_QUADS)
        glVertex2f( 0.08 * self.escalaX, -0.06 * self.escalaY)
        glVertex2f( 0.20 * self.escalaX, -0.37 * self.escalaY)
        glVertex2f( 0.08 * self.escalaX, -0.62 * self.escalaY)
        glVertex2f(-0.06 * self.escalaX, -0.37 * self.escalaY)
        glEnd()
        #PIERNA IZQUIERDA
        glColor3ub(255, 255, 255)
        glBegin(GL_QUADS)
        glVertex2f(-0.08 * self.escalaX, -0.06 * self.escalaY)
        glVertex2f(-0.20 * self.escalaX, -0.37 * self.escalaY)
        glVertex2f(-0.08 * self.escalaX, -0.62 * self.escalaY)
        glVertex2f( 0.06 * self.escalaX, -0.37 * self.escalaY)
        glEnd()
        #BOTITAS
        glColor3ub(38, 74, 140)
        glBegin(GL_QUADS)
        glVertex2f(-0.14 * self.escalaX, -0.50 * self.escalaY)
        glVertex2f(-0.02 * self.escalaX, -0.50 * self.escalaY)
        glVertex2f(-0.02 * self.escalaX, -0.78 * self.escalaY)
        glVertex2f(-0.14 * self.escalaX, -0.78 * self.escalaY)

        glVertex2f( 0.14 * self.escalaX, -0.50 * self.escalaY)
        glVertex2f( 0.02 * self.escalaX, -0.50 * self.escalaY)
        glVertex2f( 0.02 * self.escalaX, -0.78 * self.escalaY)
        glVertex2f( 0.14 * self.escalaX, -0.78 * self.escalaY)
        glEnd()
        #PUNTAS PIE
        glBegin(GL_TRIANGLES)
        glVertex2f( 0.00 * self.escalaX, -0.82 * self.escalaY)
        glVertex2f(-0.02 * self.escalaX, -0.78 * self.escalaY)
        glVertex2f(-0.14 * self.escalaX, -0.78 * self.escalaY)

        glVertex2f( 0.18 * self.escalaX, -0.82 * self.escalaY)
        glVertex2f( 0.02 * self.escalaX, -0.78 * self.escalaY)
        glVertex2f( 0.14 * self.escalaX, -0.78 * self.escalaY)
        glEnd()

        #CINTURON
        glColor3ub(255, 145, 34)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX, -0.02 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.03 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX, -0.12 * self.escalaY)
        glEnd()

        #CUELLO BLANCO
        glColor3ub(255, 255, 255)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.10 * self.escalaX,  0.38 * self.escalaY)
        glVertex2f( 0.00 * self.escalaX,  0.45 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.38 * self.escalaY)
        glEnd()

        #SACO INFERIOR
        glColor3ub( 0, 129, 169)
        glBegin(GL_QUADS)
        glVertex2f(-0.87 * self.escalaX, -0.87 * self.escalaY)
        glVertex2f(-0.03 * self.escalaX,  0.10 * self.escalaY)
        glVertex2f( 0.00 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f(-0.22 * self.escalaX, -0.50 * self.escalaY)

        glVertex2f( 0.82 * self.escalaX, -0.75 * self.escalaY)
        glVertex2f( 0.25 * self.escalaX, -0.40 * self.escalaY)
        glVertex2f( 0.097 * self.escalaX, -0.11 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.10 * self.escalaY)
        glEnd()

        #BRAZO IZQUIERDO
        glBegin(GL_POLYGON)
        glVertex2f(-0.03 * self.escalaX,  0.10 * self.escalaY)
        glVertex2f(-0.06 * self.escalaX,  0.05 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX,  0.12 * self.escalaY)
        glVertex2f(-0.22 * self.escalaX,  0.28 * self.escalaY)
        glVertex2f(-0.20 * self.escalaX,  0.30 * self.escalaY)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex2f(-0.23 * self.escalaX, -0.02 * self.escalaY)
        glVertex2f(-0.39 * self.escalaX,  0.12 * self.escalaY)
        glVertex2f(-0.22 * self.escalaX,  0.28 * self.escalaY)
        glVertex2f(-0.15 * self.escalaX,  0.20 * self.escalaY)
        glVertex2f(-0.19 * self.escalaX,  0.11 * self.escalaY)
        glVertex2f(-0.15 * self.escalaX,  0.05 * self.escalaY)
        glEnd()

        #BRAZO DERECHO
        glBegin(GL_QUAD_STRIP)
        glVertex2f( 0.28 * self.escalaX,  0.000 * self.escalaY)
        glVertex2f( 0.37 * self.escalaX,  0.070 * self.escalaY)
        glVertex2f( 0.22 * self.escalaX,  0.120 * self.escalaY)
        glVertex2f( 0.32 * self.escalaX,  0.200 * self.escalaY)
        glVertex2f( 0.18 * self.escalaX,  0.150 * self.escalaY)
        glVertex2f( 0.17 * self.escalaX,  0.321 * self.escalaY)
        glVertex2f( 0.09 * self.escalaX,  0.150 * self.escalaY)
        glVertex2f( 0.09 * self.escalaX,  0.300 * self.escalaY)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f( 0.09 * self.escalaX, 0.15 * self.escalaY)
        glVertex2f( 0.18 * self.escalaX, 0.15 * self.escalaY)
        glVertex2f( 0.16 * self.escalaX, 0.00 * self.escalaY)
        glVertex2f( 0.09 * self.escalaX, 0.00 * self.escalaY)
        glEnd()

        #MANO IZQUIERDA
        glColor3ub(255, 195, 155)
        glBegin(GL_POLYGON)
        glVertex2f(-0.10 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f(-0.19 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f(-0.19 * self.escalaX, -0.08 * self.escalaY)
        glVertex2f(-0.14 * self.escalaX, -0.02 * self.escalaY)
        glVertex2f(-0.12 * self.escalaX, -0.02 * self.escalaY)
        glEnd()

        #MANO DERECHA
        glBegin(GL_QUADS)
        glVertex2f( 0.334 * self.escalaX, -0.100 * self.escalaY)
        glVertex2f( 0.320 * self.escalaX, -0.010 * self.escalaY)
        glVertex2f( 0.419 * self.escalaX, -0.045 * self.escalaY)
        glVertex2f( 0.400 * self.escalaX, -0.120 * self.escalaY)
        glEnd()

        #CUELLO ROJO
        glColor3ub(181, 54, 65)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.20 * self.escalaX,  0.30 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX,  0.39 * self.escalaY)
        glVertex2f(-0.03 * self.escalaX,  0.08 * self.escalaY)

        glVertex2f( 0.09 * self.escalaX,  0.390 * self.escalaY)
        glVertex2f( 0.17 * self.escalaX,  0.323 * self.escalaY)
        glVertex2f( 0.09 * self.escalaX,  0.090 * self.escalaY)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(-0.025 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f(-0.022 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f(-0.030 * self.escalaX,  0.08 * self.escalaY)
        glVertex2f(-0.045 * self.escalaX,  0.10 * self.escalaY)

        glVertex2f( 0.09 * self.escalaX,  0.10 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.10 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f( 0.09 * self.escalaX,  0.00 * self.escalaY)
        glEnd()

        #Mangas
        glBegin(GL_QUADS)
        glVertex2f(-0.14 * self.escalaX,  0.05 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f(-0.21 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f(-0.28 * self.escalaX, -0.03 * self.escalaY)

        glVertex2f( 0.22 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f( 0.41 * self.escalaX,  0.11 * self.escalaY)
        glVertex2f( 0.45 * self.escalaX,  0.00 * self.escalaY)
        glVertex2f( 0.28 * self.escalaX, -0.09 * self.escalaY)
        glEnd()

        #ESPADA
        glColor3ub(130, 130, 130)
        glBegin(GL_QUADS)
        glVertex2f( 0.33 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f( 0.42 * self.escalaX, -0.05 * self.escalaY)
        glVertex2f( 0.44 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f( 0.35 * self.escalaX, -0.13 * self.escalaY)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f( 0.25 * self.escalaX, -0.78 * self.escalaY)
        glVertex2f( 0.35 * self.escalaX, -0.50 * self.escalaY)
        glVertex2f( 0.37 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f( 0.38 * self.escalaX, -0.10 * self.escalaY)
        glVertex2f( 0.42 * self.escalaX, -0.50 * self.escalaY)
        glEnd()



        ##CARA##
        glColor3ub(255, 195, 155)
        glBegin(GL_POLYGON)
        glVertex2f( 0.00 * self.escalaX, 0.70 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX, 0.60 * self.escalaY)
        glVertex2f( 0.10 * self.escalaX, 0.45 * self.escalaY)
        glVertex2f( 0.00 * self.escalaX, 0.38 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX, 0.45 * self.escalaY)
        glVertex2f(-0.10 * self.escalaX, 0.60 * self.escalaY)
        glEnd()
        ##CABELLO##
        glColor3ub(255, 165, 0)
        glBegin(GL_POLYGON)
        glVertex2f( 0.045 * self.escalaX, 0.700 * self.escalaY)
        glVertex2f( 0.120 * self.escalaX, 0.705 * self.escalaY)
        glVertex2f( 0.080 * self.escalaX, 0.680 * self.escalaY)
        glVertex2f( 0.116 * self.escalaX, 0.681 * self.escalaY)
        glVertex2f( 0.100 * self.escalaX, 0.650 * self.escalaY)
        glVertex2f( 0.118 * self.escalaX, 0.625 * self.escalaY)
        glVertex2f( 0.100 * self.escalaX, 0.627 * self.escalaY)
        glVertex2f( 0.106 * self.escalaX, 0.602 * self.escalaY)
        glVertex2f( 0.100 * self.escalaX, 0.600 * self.escalaY)
        glVertex2f( 0.110 * self.escalaX, 0.578 * self.escalaY)
        glVertex2f( 0.026 * self.escalaX, 0.625 * self.escalaY)
        glVertex2f( 0.075 * self.escalaX, 0.575 * self.escalaY)
        glVertex2f( 0.000 * self.escalaX, 0.600 * self.escalaY)
        glVertex2f( 0.025 * self.escalaX, 0.550 * self.escalaY)
        glVertex2f(-0.025 * self.escalaX, 0.600 * self.escalaY)
        glVertex2f(-0.050 * self.escalaX, 0.602 * self.escalaY)
        glVertex2f(-0.040 * self.escalaX, 0.550 * self.escalaY)
        glVertex2f(-0.080 * self.escalaX, 0.575 * self.escalaY)
        glVertex2f(-0.075 * self.escalaX, 0.545 * self.escalaY)
        glVertex2f(-0.105 * self.escalaX, 0.495 * self.escalaY)
        glVertex2f(-0.125 * self.escalaX, 0.525 * self.escalaY)
        glVertex2f(-0.120 * self.escalaX, 0.550 * self.escalaY)
        glVertex2f(-0.150 * self.escalaX, 0.545 * self.escalaY)
        glVertex2f(-0.130 * self.escalaX, 0.575 * self.escalaY)
        glVertex2f(-0.150 * self.escalaX, 0.574 * self.escalaY)
        glVertex2f(-0.125 * self.escalaX, 0.600 * self.escalaY)
        glVertex2f(-0.160 * self.escalaX, 0.625 * self.escalaY)
        glVertex2f(-0.124 * self.escalaX, 0.635 * self.escalaY)
        glVertex2f(-0.126 * self.escalaX, 0.675 * self.escalaY)
        glVertex2f(-0.080 * self.escalaX, 0.676 * self.escalaY)
        glVertex2f(-0.080 * self.escalaX, 0.700 * self.escalaY)
        glVertex2f(-0.100 * self.escalaX, 0.702 * self.escalaY)
        glVertex2f(-0.065 * self.escalaX, 0.700 * self.escalaY)
        glVertex2f(-0.050 * self.escalaX, 0.750 * self.escalaY)
        glVertex2f(-0.027 * self.escalaX, 0.699 * self.escalaY)
        glVertex2f( 0.050 * self.escalaX, 0.725 * self.escalaY)
        glEnd()

        #

        glFlush()

    def titulo(self):
        font = GLUT_BITMAP_TIMES_ROMAN_24
        glRasterPos2d(-0.1, 0.5) 
        glColor3ub(70, 70, 255)
        glutBitmapString (font, b"EL PRINCIPITO.")
        glFlush ()

    def portada(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3ub(158, 239, 250)
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(-1,  1)
        glColor3ub(77, 102, 255)
        glVertex2f( 1,  1)
        glVertex2f( 1, -1)
        glEnd()
        self.PrincipitoFront();
        self.titulo()

class Flor(object):
    def __init__(self,escalar):
        self.escalaX = 1 * escalar;
        self.escalaY = 16/9 * escalar
    def Flor3D(self):
        glColor3ub(181, 54, 65)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.85 * self.escalaX, -0.85 * self.escalaY)
        glVertex2f( 0.80 * self.escalaX, -0.73 * self.escalaY)
        glVertex2f( 0.00 * self.escalaX,  0.00 * self.escalaY)
        glEnd()