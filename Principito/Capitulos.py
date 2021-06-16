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
    def __init__(self, w, h, RotarEnY):
        self.RotarEnY = 0.0 
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
        self.Colorizar = 0
        self.Blur = 0
        self.time = 0.03
        self.Color1 = [0.619, 0.937, 0.980]
        self.Color2 = [0.301, 0.4, 1]
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
        if self.Colorizar == 0:
            self.Color1 = [0.619, 0.937, 0.980]
            self.Color2 = [0.301, 0.4, 1]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
        Principito= [2,4,6,8,9,11,13,15,17,19,21]
        Aviador=[3,5,7,10,12,14,16,18,20]
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
                 if self.wrote == 0:
                     self.Color1[0] -= 0.0304
                     self.Color1[1] -= 0.0047
                     self.Color1[2] += 0.0004
                     self.Color2[0] += 0.0214
                     self.Color2[1] += 0.029
                     self.Color2[2] -= 0.01905
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
                 if self.wrote == 0:
                     self.Color1[0] -= 0.0304
                     self.Color1[1] -= 0.0047
                     self.Color1[2] += 0.0004
                     self.Color2[0] += 0.0214
                     self.Color2[1] += 0.029
                     self.Color2[2] -= 0.01905
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        glFlush()
        time.sleep(float(self.time)); 
    
    def Cap_Dos(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_personas = Personas.Personas(0.40, 0.40, -0.25)
        if self.Colorizar == 0:
            self.Color1 = [0.011, 0.843, 0.988]
            self.Color2 = [0.729, 0.980, 0.619]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
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
                 if self.wrote == 0:
                     self.Color1[0] += 0.0535
                     self.Color1[1] -=  0.0171
                     self.Color1[2] -= 0.0581
                     self.Color2[0] -= 0.0255
                     self.Color2[1] -= 0.0576
                     self.Color2[2] -= 0.00008
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
                 if self.wrote == 0:
                     self.Color1[0] += 0.0535
                     self.Color1[1] -=  0.0171
                     self.Color1[2] -= 0.0581
                     self.Color2[0] -= 0.0255
                     self.Color2[1] -= 0.0576
                     self.Color2[2] -= 0.00008
                 self.wrote  = 1
            texto = self.Dialog_For.encode('cp1252')
            glutBitmapString (font, texto)
        glFlush()
        time.sleep(float(self.time)); 
        
    def Cap_Tres(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_personas = Personas.Personas(0.40, 0.40, -0.25)
        self.Color1 = [0.921, 0.552, 0]
        self.Color2 = [0.294, 0, 0.611]
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
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
        self.G_personas = Personas.Personas(0.70, 0.00, -0.60)
        if self.Colorizar == 0:
            self.Color1 = [0.619, 0.937, 0.980]
            self.Color2 = [0.301, 0.4, 1]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
        Principito= [2,4,6,8,10,12,14,15,17,19,21,23,24,26]
        Aviador=[3,5,7,9,11,13,16,18,20,22,25]
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
    
    def Close_Up_Flor(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glClearColor(0.40, 0.58, 0.93, 0.0)
        
        #glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
        glLight(GL_LIGHT0, GL_POSITION,  (1, 15, 1, 1)) # point light from the left, top, front
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

        glEnable(GL_DEPTH_TEST) 
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        glTranslatef(0.0, -1.0, -3.0)
        glRotatef(self.RotarEnY,0.0,1.0,0.0)
        self.G_objetos.Flor()
        glScalef(-1,0,0)
        glutSwapBuffers()
        self.RotarEnY += 0.2 
        
    def Cap_Cinco(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_personas = Personas.Personas(0.40, -0.40, -0.25)
        self.G_fondos.PlanetaPrincipito()
        letras = list(self.Dialog)
        Principito = [3,5,7,9,11,13,14,16]
        Aviador = [15]
        Flor = [2,4,6,8,10,12]

        if self.Scene_cont == 1:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
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
        elif self.Scene_cont in Flor:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.17,0.75,-0.72)
            self.G_caras.Flor()
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
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
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

    def Cap_Seis(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_personas = Personas.Personas(0.40, -0.40, -0.25)
        self.G_fondos.PlanetaPrincipito()
        letras = list(self.Dialog)
        Principito= [2,4,6,8,10, 12]
        Flor=[1,3,5,7,9,11]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
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
        elif self.Scene_cont in Flor:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.17,0.75,-0.72)
            self.G_caras.Flor()
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

    def Cap_Siete(self):
        self.G_personas = Personas.Personas(0.40, 0.00, -0.25)
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.Cuarto()
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
        
    def Cap_Ocho(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.Stage()
        letras = list(self.Dialog)
        Principito = [3,5,7,8,9,11,13,15]
        Vanidoso = [2,4,6,10,12,14]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
        elif self.Scene_cont in Vanidoso:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.66,0.67,-1.20)
            self.G_caras.Vanidoso() 
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
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
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
        
    def Cap_Nueve(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.Stage()
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10]
        Bebedor = [3,5,7,9]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
        elif self.Scene_cont in Bebedor:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.66,0.67,-1.20)
            self.G_caras.Vanidoso() 
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
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
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

    def Cap_Once(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.Oficina()
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44]
        DonNegocios = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43]

        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.51, -0.10)
            self.G_personas.HombreDeNegocios()
            self.G_objetos.escritorio()
        elif self.Scene_cont in DonNegocios:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.51, -0.10)
            self.G_personas.HombreDeNegocios()
            self.G_objetos.escritorio()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.50,0.80,-1.16)
            self.G_caras.HombreDeNegocios() 
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
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.51, -0.10)
            self.G_personas.HombreDeNegocios()
            self.G_objetos.escritorio()
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

    def Cap_Doce(self):
        glClear(GL_COLOR_BUFFER_BIT)
        letras = list(self.Dialog)
        Principito = [2,3,5,7,9,11,13,15,17,19,21,23,25]
        Farolero = [4,6,8,10,12,14,16,18,20,22,24]
        if self.Scene_cont % 2 == 0:
            self.G_fondos.PlanetaVerde(True)
            self.G_objetos = Objetos.Objetos(0.60, 0.0,0.15)
            self.G_objetos.Faro2DApagado()
        else:
            self.G_fondos.PlanetaVerde(False)
            self.G_objetos = Objetos.Objetos(0.60, 0.0,0.15)
            self.G_objetos.Faro2DPrendido()
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Farolero()
        elif self.Scene_cont in Farolero:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Farolero()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.66,0.83,-1.15)
            self.G_caras.Farolero() 
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
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Farolero()
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

    def Cap_Trece(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.PlanetaPrincipito();
        letras = list(self.Dialog)
        Principito = [3,5,7,8,9,11,13,15]
        Geografo = [2,4,6,10,12,14]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Geografo()
        elif self.Scene_cont in Geografo:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Geografo()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.70,0.67,-1.20)
            self.G_caras.Geografo() 
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
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Geografo()
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