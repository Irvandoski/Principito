from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes
import Fondos
import Objetos
import Personas
import threading
import time


class Capitulos(object):
    def __init__(self, w, h):
        self.escalaX = 1 
        self.escalaY = 16/9 
        self.G_personas = Personas.Personas(0.0, 0.0, 0.0)
        self.G_caras = Personas.Caras(0.0,0.0,-0.0)
        self.G_objetos = Objetos.Objetos(0.60,-0.6,0.0)
        self.G_fondos = Fondos.Fondos()
        self.Scene_cont = 0
        self.Dialog_cont = 0
        self.Dialog = " "
        self.Dialog_For = " "
        self.w = w
        self.h = h
        self.wrote = 0
        self.time = 0.03
    def Portada(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor3ub(158, 239, 250)
        
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(-1,  1)
        glColor3ub(77, 102, 255)
        glVertex2f( 1,  1)
        glVertex2f( 1, -1)
        glEnd()
        
        self.G_personas = Personas.Personas(0.40, 0.00, -0.25)
        self.G_personas.Principito()

        font = GLUT_BITMAP_TIMES_ROMAN_24
        glRasterPos2d(-0.1, 0.5) 
        glColor3ub(70, 70, 255)
        glutBitmapString (font, b"EL PRINCIPITO.")
        glFlush ()

    def Cap_Uno(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.G_personas = Personas.Personas(0.40, 0.00, -0.25)
        self.G_fondos.Desierto()

        letras = list(self.Dialog)
        self.G_personas.Principito();
        Principito= [2,4,6,8,9,11,13,15,17,19,21]
        Aviador=[3,5,7,10,1,14,19,18,20]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
            self.G_caras =Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
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
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
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
        time.sleep(float(self.time)); 
    
    def Cap_Dos(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.G_personas = Personas.Personas(0.40, 0.40, -0.25)
        self.G_fondos.Desierto()

        letras = list(self.Dialog)
        self.G_personas.Principito();
        Principito= [2,4,6,7,9,11,13,15,17]
        Aviador=[3,5,8,10,12,14,16,18]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
            self.G_caras =Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
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
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
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
        time.sleep(float(self.time)); 
        
    def Cap_Tres(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.G_personas = Personas.Personas(0.40, 0.40, -0.25)
        self.G_fondos.DesiertoNoche()
        letras = list(self.Dialog)
        self.G_personas.Principito();
        Principito= [2,4,6,8,10,12,14,16,18]
        Aviador=[3,5,7,9,11,13,15,17]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
            self.G_caras =Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
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
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
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
        time.sleep(float(self.time)); 

    def Cap_Cuatro(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.G_personas = Personas.Personas(0.40, 0.40, -0.25)
        self.G_fondos.Desierto()

        letras = list(self.Dialog)
        self.G_personas.Principito();
        Principito= [2,4,6,8,10,12,14,15,17,19,21,23,24,26]
        Aviador=[3,5,7,9,11,13,16,18,20,22,25]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
            self.G_caras =Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
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
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
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
        time.sleep(float(self.time)); 
    def Rey(self):
        self.G_personas = Personas.Personas(0.40, 0.00, -0.25)
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
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.80,-0.99)
            self.G_caras.Rey() 
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
        elif self.Scene_cont in Principito:
            self.G_personas.Rey()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
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
        time.sleep(float(self.time)); 