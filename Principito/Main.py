from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes
import Capitulos
import Dialogos
import threading
import time
import pyglet

class Main(object):
    def __init__(self):
        self.screen= ctypes.windll.user32
        self.width = self.screen.GetSystemMetrics(0)
        self.height = self.screen.GetSystemMetrics(1)
        self.G_capitulos = Capitulos.Capitulos(-0.90,-0.70)
        self.G_dialogos = Dialogos.Dialogos()
        self.nivel = 0
        self.cont_dialog = 0
        self.Thread_Music = threading.Thread();
        self.musica = pyglet.resource.media('Menu.mp3', streaming=True)
        self.player=pyglet.media.Player()
        self.changed = False
    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if key == chr(27):
            pyglet.app.exit()
            self.Thread_Music.join()
            os._exit(1) 
            sys.exit()
        if key == chr(32) and self.nivel == 1:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.SieteRey()
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont  + 1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
            self.G_capitulos.Scene_cont += 1
            #glutDisplayFunc(self.G_capitulos.Rey)
            glutIdleFunc(self.G_capitulos.Rey)
        if key == chr(32) and self.nivel == 0:
            if self.changed == False:
                self.player.next_source()
                self.changed = True
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.UnoPiloto()
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont  + 1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
            self.G_capitulos.Scene_cont += 1
            glutDisplayFunc(self.G_capitulos.Cap_Dos)
            glutIdleFunc(self.G_capitulos.Cap_Dos)
            

    def main(self):
        
        self.Thread_Music = threading.Thread(name="Music", target=self.Music)
        self.Thread_Music.start();
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
        glutInitWindowSize(160,90)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Ventana")

        glutFullScreen()
        glMatrixMode(GL_PROJECTION);
        glutDisplayFunc(self.G_capitulos.Portada)

        #glutDisplayFunc(self.G_capitulos.desierto)
        #glutIdleFunc(self.G_principito_front.principito)
        glutKeyboardFunc(self.keyPress)
        glClearColor(0.027, 0.823, 0.835, 0.0)
        #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
        glutMainLoop()
    def Music(self):
        self.player.queue(pyglet.media.load("Menu.mp3"))
        self.player.queue(pyglet.media.load("01TemaDesierto.mp3"))
        self.player.play();
        self.player.volume = 0.1
        pyglet.app.run()

View = Main();
View.main();
# End of Program