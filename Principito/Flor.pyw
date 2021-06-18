import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Capitulos
import time, sys

class Tridimensional:
    def __init__(self):
        self.G_capitulos = Capitulos.Capitulos(-0.90,-0.68, 0.0)
    #inicializa la ventana donde desplegaremos los graficos
    def InitGL(self,Width, Height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
    def keyPressed(self,*args):
        # Permite estar rotando el objeto
        if args[0] == '\x1b':
            sys.exit()   
        if args[0]  == b' ':
            glutLeaveMainLoop();
    def main(self):
        global window
        global RotarEnY
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(1280, 720)
        glutInitWindowPosition(0, 0)
        window = glutCreateWindow("3D")
        glutFullScreen()
        glutDisplayFunc(self.G_capitulos.Close_Up_Flor)
        glutIdleFunc(self.G_capitulos.Close_Up_Flor)
        glutKeyboardFunc(self.keyPressed)
        self.InitGL(1280, 720)
        RotarEnY = 0.0
        glutMainLoop()

main_process = Tridimensional();
main_process.main()

