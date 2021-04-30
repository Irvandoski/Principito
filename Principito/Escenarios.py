from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Objetos
import sys
import time
class Escenas(object):
    def __init__(self, w, h):
        self.escalaX = 1 
        self.escalaY = 16/9 
        self.G_personas = Objetos.Personas(0.0, 0.0, 0.0)
        self.G_dialogos = Objetos.CuadrosDeDialogo(0.40)
        self.G_caras = Objetos.Caras(0.65,0.80,-0.99)
        self.Scene_cont = 0
        self.Dialog_cont = 0
        self.Dialog = " "
        self.Dialog_For = " "
        self.w = w
        self.h = h
        self.wrote = 0
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

    def desierto(self):
        self.G_personas = Objetos.Personas(0.40, 0.00, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3ub(158, 239, 250)
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(-1,  1)
        glColor3ub(77, 102, 255)
        glVertex2f( 1,  1)
        glVertex2f( 1, -1)
        glEnd()

        glColor3ub(226, 203, 186)
        glBegin(GL_QUADS)
        glVertex2f(-1.2,0.1)
        glVertex2f(-0.65,0.42)
        glVertex2f(0,0.12)
        glVertex2f(-0.655,-0.12)
        glEnd()

        glColor3ub(233,211,193)
        glBegin(GL_POLYGON)
        glVertex2f(-0.83,-0.25)
        glVertex2f(0.22,0.55)
        glVertex2f(1.1,0.27)
        glVertex2f(1.1,-0.55)
        glVertex2f(0.3,-0.9)
        glEnd()

        glColor3ub(194,171,153)
        glBegin(GL_TRIANGLES)
        glVertex2f(-1.1,0.4)
        glVertex2f(0.7,-0.63)
        glVertex2f(-1.1,-0.7)
        glEnd()

        glColor3ub(226,203,186)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.05,-0.85)
        glVertex2f(0.68,-0.14)
        glVertex2f(1.4,-0.85)
        glEnd()

        glColor3ub(209,178,149)
        glBegin(GL_TRIANGLES)
        glVertex2f(-1,0)
        glVertex2f(1,-0.95)
        glVertex2f(-1,-0.95)
        glEnd()

        glColor3ub(233,211,193)
        glBegin(GL_QUADS)
        glVertex2f(-1,-0.7)
        glVertex2f(1,-0.7)
        glVertex2f(1,-1)
        glVertex2f(-1,-1)
        glEnd()

        letras = list(self.Dialog)
        self.G_personas.PrincipitoFront();
        Principito= [2,4,6,8,9,11,13,15,17,19,21]
        Aviador=[3,5,7,10,1,14,19,18,20]

        if self.Scene_cont == 1:
            self.G_personas.PrincipitoFront()
        elif self.Scene_cont in Principito:
            self.G_personas.PrincipitoFront()
            self.G_dialogos.cuadro_grande()
            self.G_caras =Objetos.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
            font = GLUT_BITMAP_TIMES_ROMAN_24
            glColor3ub(0,0,0) 
            glRasterPos2d(self.w, self.h) 
            #glColor3ub(0,0,0) 
            if self.Dialog_cont < len(letras) and self.wrote == 0:
                self.Dialog_For += letras[self.Dialog_cont]
                self.Dialog_cont += 1
            else:
                 self.Dialog_cont = 0
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        elif self.Scene_cont in Aviador:
            self.G_personas.PrincipitoFront()
            self.G_dialogos.cuadro_grande()
            font = GLUT_BITMAP_TIMES_ROMAN_24
            glColor3ub(0,0,0) 
            glRasterPos2d(self.w, self.h) 
            
            if self.Dialog_cont < len(letras) and self.wrote == 0:
                self.Dialog_For += letras[self.Dialog_cont]
                self.Dialog_cont += 1
            else:
                 self.Dialog_cont = 0
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        glFlush()
        time.sleep(0.03); 
         
    def Rey(self):
        self.G_personas = Objetos.Personas(0.40, 0.00, -0.25)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3ub(55, 55, 55)
        glBegin(GL_QUADS)
        glVertex3f(-0.80, -0.80, -0.80)
        glVertex3f(-0.80,  0.80, -0.80)
        glVertex3f( 0.80,  0.80, -0.80)
        glVertex3f( 0.80, -0.80, -0.80)
        glEnd()
         
        glColor3ub(55, 55, 255)
        glBegin(GL_POLYGON)
        glVertex3f(-0.60,  0.20,  0.60)
        glVertex3f(-0.60,  0.20,  0.60)
        glVertex3f(-0.40,  0.60,  0.60)
        glVertex3f(-0.40,  0.60,  0.60)
        glEnd()

        glColor3ub(95, 95, 95)
        glBegin(GL_QUADS) 
        glVertex3f(-0.80, -0.80, -0.80)
        glVertex3f(-1.00, -1.00,  0.80)
        glVertex3f(-1.00,  1.00,  0.80)
        glVertex3f(-0.80,  0.80, -0.80)
        glEnd()
        
        glColor3ub(95, 95, 95)
        glBegin(GL_QUADS) 
        glVertex3f( 0.80, -0.80, -0.80)
        glVertex3f( 1.00, -1.00,  0.80)
        glVertex3f( 1.00,  1.00,  0.80)
        glVertex3f( 0.80,  0.80, -0.80)
        glEnd()
        
        glColor3ub(80, 80, 80)
        glBegin(GL_QUADS) 
        glVertex3f(-0.80,  0.80, -0.80)
        glVertex3f(-1.00,  1.00,  0.80)
        glVertex3f( 1.00,  1.00,  0.80)
        glVertex3f( 0.80,  0.80, -0.80)
        glEnd()

        glColor3ub(80, 80, 80)
        glBegin(GL_QUADS) 
        glVertex3f(-0.80, -0.80, -0.80)
        glVertex3f(-1.00, -1.00,  0.80)
        glVertex3f( 1.00, -1.00,  0.80)
        glVertex3f( 0.80, -0.80, -0.80)
        glEnd()

        letras = list(self.Dialog)
        self.G_personas.Rey()
        Rey = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]
        Principito = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
        if self.Scene_cont == 1:
            self.G_personas.Rey()
        elif self.Scene_cont in Rey:
            self.G_personas.Rey()
            self.G_dialogos.cuadro_grande()
            self.G_caras = Objetos.Caras(0.65,0.80,-0.99)
            self.G_caras.Rey() 
            font = GLUT_BITMAP_TIMES_ROMAN_24
            glRasterPos2d(self.w, self.h) 
            glColor3ub(70, 70, 255) 
            if self.Dialog_cont < len(letras) and self.wrote == 0:
                self.Dialog_For += letras[self.Dialog_cont]
                self.Dialog_cont += 1
            else:
                 self.Dialog_cont = 0
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        elif self.Scene_cont in Principito:
            self.G_personas.Rey()
            self.G_dialogos.cuadro_grande()
            self.G_caras = Objetos.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
            font = GLUT_BITMAP_TIMES_ROMAN_24
            glRasterPos2d(self.w, self.h) 
            glColor3ub(70, 70, 255) 
            if self.Dialog_cont < len(letras) and self.wrote == 0:
                self.Dialog_For += letras[self.Dialog_cont]
                self.Dialog_cont += 1
            else:
                 self.Dialog_cont = 0
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        glFlush()
        time.sleep(0.03);