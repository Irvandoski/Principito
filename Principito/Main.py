from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes
import Objetos
import Escenarios
import Dialogos
import threading
import time

class Main(object):
    def __init__(self):
        self.screen= ctypes.windll.user32
        self.width = self.screen.GetSystemMetrics(0)
        self.height = self.screen.GetSystemMetrics(1)
        self.G_principito_front = Objetos.Principito(0.30)
        self.G_escenas = Escenarios.Escenas(-0.90,-0.70)
        self.G_dialogos = Dialogos.Dialogos()
        self.G_personas = Objetos.Personas(0.40, 0.00, 0.00)
        self.nivel = 0
        self.cont_dialog = 0
    #CAMBIOS
    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if key == chr(27):
            os._exit(1) 
            sys.exit()
        if key == chr(32) and self.nivel == 5:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(self.G_personas.Farolero)
            glutIdleFunc(self.G_personas.Farolero)
            glFlush()
            self.nivel +=1;
        if key == chr(32) and self.nivel == 4:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.SieteRey()
            self.G_escenas.Dialog = self.G_dialogos.dialogos[self.G_escenas.Scene_cont-1]
            self.G_escenas.Dialog_For = ""
            self.G_escenas.wrote = 0
            if self.G_escenas.Scene_cont  + 1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
            self.G_escenas.Scene_cont += 1
            glutDisplayFunc(self.G_escenas.Rey)
            glutIdleFunc(self.G_escenas.Rey)
            glFlush()
        if key == chr(32) and self.nivel == 3:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(Objetos.CuadrosDeDialogo(0.40).cuadro_pequeño)
            glutIdleFunc(Objetos.CuadrosDeDialogo(0.40).cuadro_pequeño)
            glFlush()
            self.nivel +=1;
        if key == chr(32) and self.nivel == 2:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(self.G_personas.Silueta_2)
            glutIdleFunc(self.G_personas.Silueta_2)
            glFlush()
            self.nivel +=1;
        if key == chr(32) and self.nivel == 1:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(self.G_personas.Silueta_1)
            glutIdleFunc(self.G_personas.Silueta_1)
            glFlush()
            self.nivel +=1;
        if key == chr(32) and self.nivel == 0:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(self.G_escenas.desierto)
            glutIdleFunc(self.G_escenas.desierto)
            glFlush()
            self.nivel +=1;
    def main(self):
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(160,90)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Ventana")

        glutFullScreen()
        glMatrixMode(GL_PROJECTION);
        glutDisplayFunc(self.G_principito_front.portada)

        #glutDisplayFunc(self.G_escenas.desierto)
        #glutIdleFunc(self.G_principito_front.principito)
        glutKeyboardFunc(self.keyPress)
        glClearColor(0.027, 0.823, 0.835, 0.0)
        #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
        glFlush()
        glutMainLoop()
        
View = Main();
View.main();
# End of Program