
# PyPoints.py
# Setting a coordinate system with central origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
def principito():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)
    glVertex2f(-1, 0.0)
    glVertex2f(1,0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()


    #SOLAPA ROJA
    glColor3ub(181, 54, 65)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.85, -0.85)
    glVertex2f(0.8, -0.73)
    glVertex2f(0,0)
    glEnd()
    #TORSO
    glColor3ub(255, 255, 255)

    glBegin(GL_QUADS)
    glVertex2f(-0.1,0.38)
    glVertex2f(0.1,0.38)
    glVertex2f(0.1,-0.37)
    glVertex2f(-0.05,-0.37)
    glEnd()
    #PIERNA DERECHA
    glColor3ub(235,235,235)
    glBegin(GL_QUADS)
    glVertex2f(0.08, -0.06)
    glVertex2f(0.2, -0.37)
    glVertex2f(0.08,-0.62)
    glVertex2f(-0.06,-0.37)
    glEnd()
    #PIERNA IZQUIERDA
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(-0.08, -0.06)
    glVertex2f(-0.2, -0.37)
    glVertex2f(-0.08,-0.62)
    glVertex2f(0.06,-0.37)
    glEnd()
    #BOTITAS
    glColor3ub(38, 74, 140)
    glBegin(GL_QUADS)
    glVertex2f(-0.14, -0.5)
    glVertex2f(-0.02, -0.5)
    glVertex2f(-0.02,-0.78)
    glVertex2f(-0.14,-0.78)

    glVertex2f(0.14, -0.5)
    glVertex2f(0.02, -0.5)
    glVertex2f(0.02,-0.78)
    glVertex2f(0.14,-0.78)
    glEnd()
    #PUNTAS PIE
    glBegin(GL_TRIANGLES)
    glVertex2f(0, -0.82)
    glVertex2f(-0.02,-0.78)
    glVertex2f(-0.14, -0.78)

    glVertex2f(0.18, -0.82)
    glVertex2f(0.02, -0.78)
    glVertex2f(0.14,-0.78)
    glEnd()

    #CINTURON
    glColor3ub(255, 145, 34)
    glBegin(GL_QUADS)
    glVertex2f(-0.1, -0.02)
    glVertex2f(0.1, 0.03)
    glVertex2f(0.1,0)
    glVertex2f(-0.1,-0.12)
    glEnd()
    #CUELLO BLANCO
    glColor3ub(255, 255, 255)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, 0.38)
    glVertex2f(0,0.45)
    glVertex2f(0.1, 0.38)
    glEnd()

    #SACO INFERIOR
    glColor3ub(0, 129, 169)
    glBegin(GL_QUADS)
    glVertex2f(-0.87,-0.87)
    glVertex2f(-0.03, 0.1)
    glVertex2f(0,-0.1)
    glVertex2f(-0.22,-0.5)

    glVertex2f(0.82,-0.75)
    glVertex2f(0.25, -0.4)
    glVertex2f(0.097,-0.11)
    glVertex2f(0.1,0.1)
    glEnd()

    #BRAZO IZQUIERDO
    glBegin(GL_POLYGON)

    glVertex2f(-0.03,0.1)
    glVertex2f(-0.06, 0.05)
    glVertex2f(-0.1,0)
    glVertex2f(-0.1, 0.12)
    glVertex2f(-0.22,0.28)
    glVertex2f(-0.2,0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-0.23,-0.02)
    glVertex2f(-0.39,0.12)
    glVertex2f(-0.22,0.28)
    glVertex2f(-0.15, 0.2)
    glVertex2f(-0.19, 0.11)
    glVertex2f(-0.15, 0.05)
    glEnd()

    #BRAZO DERECHO
    glBegin(GL_QUAD_STRIP)
    glVertex2f(0.28,0)
    glVertex2f(0.37,0.07)
    glVertex2f(0.22,0.12)
    glVertex2f(0.32,0.2)
    glVertex2f(0.18,0.15)
    glVertex2f(0.17,0.321)
    glVertex2f(0.09,0.15)
    glVertex2f(0.09,0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(0.09,0.15)
    glVertex2f(0.18,0.15)
    glVertex2f(0.16,0)
    glVertex2f(0.09,0)
    glEnd()

    #MANO IZQUIERDA
    glColor3ub(255, 195, 155)
    glBegin(GL_POLYGON)
    glVertex2f(-0.1,-0.1)
    glVertex2f(-0.19,-0.1)
    glVertex2f(-0.19,-0.08)
    glVertex2f(-0.14,-0.02)
    glVertex2f(-0.12,-0.02)
    glEnd()

    #MANO DERECHA
    glBegin(GL_QUADS)
    glVertex2f(0.334,-0.1)
    glVertex2f(0.32,-0.01)
    glVertex2f(0.419,-0.045)
    glVertex2f(0.4,-0.12)
    glEnd()

    #CUELLO ROJO
    glColor3ub(181, 54, 65)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.2,0.3)
    glVertex2f(-0.1,0.39)
    glVertex2f(-0.03,0.08)

    glVertex2f(0.09,0.39)
    glVertex2f(0.17,0.323)
    glVertex2f(0.09,0.09)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-0.025,0)
    glVertex2f(-0.022,0)
    glVertex2f(-0.03,0.08)
    glVertex2f(-0.045,0.1)

    glVertex2f(0.09,0.1)
    glVertex2f(0.1,0.1)
    glVertex2f(0.1,0)
    glVertex2f(0.09,0)
    glEnd()

    #Mangas
    glBegin(GL_QUADS)
    glVertex2f(-0.14,0.05)
    glVertex2f(-0.10,0)
    glVertex2f(-0.21,-0.1)
    glVertex2f(-0.28,-0.03)

    glVertex2f(0.22,0)
    glVertex2f(0.41,0.11)
    glVertex2f(0.45,0)
    glVertex2f(0.28,-0.09)
    glEnd()

    #ESPADA
    glColor3ub(130, 130, 130)
    glBegin(GL_QUADS)
    glVertex2f(0.33,-0.1)
    glVertex2f(0.42,-0.05)
    glVertex2f(0.44,-0.1)
    glVertex2f(0.35,-0.13)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(0.25,-0.78)
    glVertex2f(0.35,-0.5)
    glVertex2f(0.37,-0.1)
    glVertex2f(0.38,-0.1)
    glVertex2f(0.42,-0.5)
    glEnd()



    ##CARA##
    glColor3ub(255, 195, 155)
    glBegin(GL_POLYGON)
    glVertex2f(0, 0.7)
    glVertex2f(0.1, 0.6)
    glVertex2f(0.1, 0.45)
    glVertex2f(0, 0.38)
    glVertex2f(-0.1, 0.45)
    glVertex2f(-0.1, 0.6)
    glEnd()
    ##CABELLO##
    glColor3ub(255, 165, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0.045, 0.7)
    glVertex2f(0.12, 0.705)
    glVertex2f(0.08, 0.68)
    glVertex2f(0.116, 0.681)
    glVertex2f(0.1, 0.65)
    glVertex2f(0.118, 0.625)
    glVertex2f(0.1, 0.627)
    glVertex2f(0.106, 0.602)
    glVertex2f(0.1, 0.6)
    glVertex2f(0.11, 0.578)
    glVertex2f(0.026,0.625)
    glVertex2f(0.075, 0.575)
    glVertex2f(0, 0.6)
    glVertex2f(0.025, 0.55)
    glVertex2f(-0.025, 0.6)
    glVertex2f(-0.05, 0.602)
    glVertex2f(-0.04, 0.55)
    glVertex2f(-0.08, 0.575)
    glVertex2f(-0.075, 0.545)
    glVertex2f(-0.105, 0.495)
    glVertex2f(-0.125, 0.525)
    glVertex2f(-0.120, 0.55)
    glVertex2f(-0.15, 0.545)
    glVertex2f(-0.13, 0.575)
    glVertex2f(-0.15, 0.574)
    glVertex2f(-0.125, 0.6)
    glVertex2f(-0.16, 0.625)
    glVertex2f(-0.124, 0.635)
    glVertex2f(-0.126, 0.675)
    glVertex2f(-0.08, 0.676)
    glVertex2f(-0.08, 0.7)
    glVertex2f(-0.1, 0.702)
    glVertex2f(-0.065, 0.7)
    glVertex2f(-0.05, 0.75)
    glVertex2f(-0.027, 0.699)
    glVertex2f(0.05, 0.725)
    glEnd()

    #

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Ventana")
    glutDisplayFunc(principito)
    init()
    glutMainLoop()
main()
# End of Program