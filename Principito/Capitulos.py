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
        self.Dialog_For_A = " "
        self.Dialog_For_B = " "
        self.Dialog_For_C = " "
        self.w = w
        self.h = h
        self.wrote = 0
        self.Colorizar = 0
        self.Blur = 0
        self.time = 0.03
        self.Color1 = [0.619, 0.937, 0.980]
        self.Color2 = [0.301, 0.4, 1]
        self.sumatoria1 = [0, 0, 0]
        self.sumatoria2 = [0, 0, 0]

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
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
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
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
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
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.Avioneta()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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
        elif self.Scene_cont in Flor:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.17,0.75,-0.72)
            self.G_caras.Flor()
        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Flor:
            self.G_personas.Principito()
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.17,0.75,-0.72)
            self.G_caras.Flor()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Principito:
            self.G_personas.Rey()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
            
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Vanidoso()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 
        
    def Cap_Nueve(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.PlanetaCafé()
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10]
        Bebedor = [3,5,7,9]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.52, 0.47, -0.20)
            self.G_personas.Ebrio()
        elif self.Scene_cont in Bebedor:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.52, 0.47, -0.20)
            self.G_personas.Ebrio()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.66,0.80,-1.08)
            self.G_caras.Ebrio() 

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.52, 0.47, -0.20)
            self.G_personas.Ebrio()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
            
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
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

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.51, -0.10)
            self.G_personas.HombreDeNegocios()
            self.G_objetos.escritorio()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Close_Up_Faro(self):
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
        self.G_objetos.Faro()
        glScalef(-1,0,0)
        glutSwapBuffers()
        self.RotarEnY += 0.2 

    def Cap_Doce(self):
        glClear(GL_COLOR_BUFFER_BIT)
        letras = list(self.Dialog)
        Principito = [2,3,5,7,9,11,13,15,17,19,21,23,25]
        Farolero = [4,6,8,10,12,14,16,18,20,22,24]
        try:
            self.sumatoria1 = [(0.921 - 0.619) /  len(letras), (0.552 - 0.937) /  len(letras), (0 - 0.980) /  len(letras)]
            self.sumatoria2 = [(0.294 - 0.301) /  len(letras), (0 - 0.4) /  len(letras), (0.611 - 1) /  len(letras)]
        except :
            self.sumatoria1 = [0,0,0]
            self.sumatoria2 = [0,0,0]
        if self.Scene_cont % 2 == 0:
            if self.wrote == 0 and self.Scene_cont != 1:
                self.Color1 = [self.Color1[0]-self.sumatoria1[0], self.Color1[1]-self.sumatoria1[1], self.Color1[2]-self.sumatoria1[2]]
                self.Color2 = [self.Color2[0]-self.sumatoria2[0], self.Color2[1]-self.sumatoria2[1], self.Color2[2]-self.sumatoria2[2]]
            self.G_fondos.PlanetaVerde(self.Color1, self.Color2)
            self.G_objetos = Objetos.Objetos(0.60, 0.0,0.15)
            self.G_objetos.Faro2DApagado()

        else:
            if self.wrote == 0 and self.Scene_cont != 1:
                self.Color1 = [self.Color1[0]+self.sumatoria1[0], self.Color1[1]+self.sumatoria1[1], self.Color1[2]+self.sumatoria1[2]]
                self.Color2 = [self.Color2[0]+self.sumatoria2[0], self.Color2[1]+self.sumatoria2[1], self.Color2[2]+self.sumatoria2[2]]
            self.G_fondos.PlanetaVerde(self.Color1, self.Color2)
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

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.05)
            self.G_personas.Farolero()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Trece(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.PlanetaCafé();
        letras = list(self.Dialog)
        Principito = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
        Geografo = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]

        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.31, -0.15)
            self.G_personas.Geografo()
        elif self.Scene_cont in Geografo:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.31, -0.15)
            self.G_personas.Geografo()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.60,0.80,-1.18)
            self.G_caras.Geografo() 

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.31, -0.15)
            self.G_personas.Geografo()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Catorce(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.Desierto([0.619, 0.937, 0.980],[0.301, 0.4, 1])
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10,12,14,15,17,19,21]
        Serpiente = [3,5,7,9,11,13,16,18,20]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
        elif self.Scene_cont in Serpiente:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.25,0.83,-0.80)
            self.G_caras.Serpiente()

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Quince(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.G_fondos.PlanetaPrincipito();
        letras = list(self.Dialog)
        Principito = [2,4,6]
        Flor = [3,5]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.32,-0.55)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.36,-0.52)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.41,-0.60)
            self.G_caras.Flor()
        elif self.Scene_cont in Flor:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.32,-0.55)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.36,-0.52)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.41,-0.60)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.17,0.75,-0.72)
            self.G_caras.Flor()

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.17,0.30,-0.54)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.32,-0.55)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.36,-0.52)
            self.G_caras.Flor()
            self.G_caras = Personas.Caras(0.17,0.41,-0.60)
            self.G_caras.Flor()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Close_Up_Zorro(self):
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
        self.G_objetos.Zorro()
        glScalef(-1,0,0)
        glutSwapBuffers()
        self.RotarEnY += 0.2 

    def Cap_Dieciseis(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.Color1 = [0.619, 0.937, 0.980]
        self.Color2 = [0.301, 0.4, 1]
        self.G_fondos.PlanetaVerde(self.Color1, self.Color2);
        letras = list(self.Dialog)
        Principito = [3,5,7,9,11,12,14,16,18,20,22,24,26,29,31,33,36]
        Zorro = [2,4,6,8,10,13,15,17,19,21,23,25,27,28,30,32,34,35]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()

        elif self.Scene_cont in Zorro:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.45,0.87,-0.88)
            self.G_caras.Zorro() 

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Diecisiete(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.Color1 = [0.619, 0.937, 0.980]
        self.Color2 = [0.301, 0.4, 1]
        self.G_fondos.PlanetaVerde(self.Color1, self.Color2);
        letras = list(self.Dialog)
        Principito = [3,5,7,9,11,12,14,16,18]
        Zorro = [2,4,6,8,13,15,17]
        Flores = [10]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()
        elif self.Scene_cont in Zorro:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.45,0.87,-0.88)
            self.G_caras.Zorro() 

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_personas = Personas.Personas(0.40, 0.47, -0.35)
            self.G_personas.Zorro()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Close_Up_Pozo(self):
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
        self.G_objetos.Pozo()
        glScalef(-1,0,0)
        glutSwapBuffers()
        self.RotarEnY += 0.2 

    def Cap_Dieciocho(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.Colorizar == 0:
            self.Color1 = [0.619, 0.937, 0.980]
            self.Color2 = [0.301, 0.4, 1]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
        Principito = [3,5,7,9,11,13,15,16,18,20,21,23,25,27,29,31,33,35,37,39,41,43]
        Aviador = [2,4,6,8,10,12,14,17,19,22,24,26,28,30,32,34,36,38,40,42]
        if self.Scene_cont == 1:
            self.G_personas.Principito()
        elif self.Scene_cont in Principito:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
            self.G_caras =Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        elif self.Scene_cont in Aviador:
            self.G_personas.Principito()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Diecinueve(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.Colorizar == 0:
            self.Color1 = [0, 0.133, 0.439]
            self.Color2 = [0.921, 0.352, 0.2]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,31,33,35,37,39,41]
        Aviador = [9,11,13,15,17,19,21,23,25,27,29,32,34,36,38,40]
        Serpiente = [3,5,7]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
        elif self.Scene_cont in Serpiente:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.25,0.83,-0.80)
            self.G_caras.Serpiente()

        elif self.Scene_cont in Principito:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()
            
        elif self.Scene_cont in Aviador:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
            self.G_caras = Personas.Caras(0.45,0.30,-0.54)
            self.G_caras.Serpiente()
            self.G_objetos.cuadro_grande()
        glColor3ub(0,0,0) 
        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time)); 

    def Cap_Veinte(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.Colorizar == 0:
            self.Color1 = [0, 0.133, 0.439]
            self.Color2 = [0.921, 0.352, 0.2]
            self.Colorizar = 1
        self.G_fondos.Desierto(self.Color1, self.Color2)
        letras = list(self.Dialog)
        Principito = [2,4,6,8,10,12,14]
        Aviador = [3,5,7,9,11,13]
        if self.Scene_cont == 1:
            self.G_personas = Personas.Personas(0.37, -0.44, -0.20)
            self.G_personas.Principito();
        elif self.Scene_cont in Aviador:
            self.G_objetos.cuadro_grande()

        elif self.Scene_cont in Principito:
            self.G_objetos.cuadro_grande()
            self.G_caras = Personas.Caras(0.65,0.81,-1.35)
            self.G_caras.Principito()

        glColor3ub(0,0,0) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h-0.08) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.16) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time));
    
    def Cap_Veintiuno(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor3f(0, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(-1,  1)
        glVertex2f( 1,  1)
        glVertex2f( 1, -1)
        glEnd()
        letras = list(self.Dialog)
        glColor3ub(255,255,255) 
        font = GLUT_BITMAP_TIMES_ROMAN_24
        if self.Dialog_cont < len(letras) and self.wrote == 0:
            if self.Dialog_cont >280:
                self.Dialog_For_C += letras[self.Dialog_cont]
            elif self.Dialog_cont >140:
                self.Dialog_For_B += letras[self.Dialog_cont]
            else:
                self.Dialog_For_A += letras[self.Dialog_cont]
            self.Dialog_cont += 1
        else:
                self.Dialog_cont = 0
                self.wrote  = 1
        glRasterPos2d(self.w, self.h+0.8) 
        texto1 = self.Dialog_For_A.encode('cp1252')
        glutBitmapString (font, texto1)
        glRasterPos2d(self.w, self.h) 
        texto2 = self.Dialog_For_B.encode('cp1252')
        glutBitmapString (font, texto2)
        glRasterPos2d(self.w, self.h-0.8) 
        texto3 = self.Dialog_For_C.encode('cp1252')
        glutBitmapString (font, texto3)
        glFlush()
        time.sleep(float(self.time));