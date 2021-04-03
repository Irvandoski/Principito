from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes
import Objetos
import Escenarios
import threading
class Main(object):
    def __init__(self):
        self.screen= ctypes.windll.user32
        self.width = self.screen.GetSystemMetrics(0)
        self.height = self.screen.GetSystemMetrics(1)
        self.G_principito_front = Objetos.Principito(0.30)
        self.G_escenas = Escenarios.Escenas(); 

    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if key == chr(27):
            os._exit(1) 
            sys.exit()
        if key == 'q':
            glClearColor(0.027, 0.823, 0.835, 0.0)
            glutDisplayFunc(self.G_escenas.desierto)
            glFlush()
    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(160,90)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Ventana")
        glutFullScreen()
        glutDisplayFunc(self.G_principito_front.portada)
        #glutDisplayFunc(self.G_escenas.desierto)
        #glutIdleFunc(self.G_principito_front.principito)
        glutKeyboardFunc(self.keyPress)
        glClearColor(0.027, 0.823, 0.835, 0.0)
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glFlush()
        glutMainLoop()
View = Main();
View.main();
# End of Program