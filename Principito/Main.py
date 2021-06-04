from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from decimal import *
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
        self.G_capitulos = Capitulos.Capitulos(-0.90,-0.70,0.0)
        self.G_dialogos = Dialogos.Dialogos()
        self.nivel = 0
        self.cont_dialog = 0
        self.Thread_Music = threading.Thread();
        self.musica = pyglet.resource.media('00Menu.mp3', streaming=True)
        self.player=pyglet.media.Player()
        self.changed = False
        self.RotarEnY = 0.0
        self.RotarLuz = 0.0

    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if key == "n":
            self.nivel +=1;
        if key == chr(27):
            pyglet.app.exit()
            self.Thread_Music.join()
            os._exit(1) 
            sys.exit()
            
        #CAPITULO CINCO
        if key == chr(32) and self.nivel == 5:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.CuatroEspinas()      
            
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1
            
            glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
            glutIdleFunc(self.G_capitulos.Cap_Cuatro)
        if key == chr(32) and self.nivel == 6:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.SieteRey()
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont  + 1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
            self.G_capitulos.Scene_cont += 1
            glutDisplayFunc(self.G_capitulos.Rey)
            glutIdleFunc(self.G_capitulos.Rey)

        #CAPITULO CINCO
        if key == chr(32) and self.nivel == 5:
            
            glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
            
            glMatrixMode(GL_PROJECTION);
            #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
            glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
       
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.CuatroEspinas()      
            
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1
            
            glutDisplayFunc(self.G_capitulos.Cap_Cinco)
            glutIdleFunc(self.G_capitulos.Cap_Cinco)
        #CLOSE UP FLOR
        if key == chr(32) and self.nivel == 4:
            
            glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
            glClearColor(0.0, 0.0, 0.0, 0.0)
            glClearDepth(1.0)
            glShadeModel(GL_SMOOTH)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(45.0, float(1280)/float(720), 0.1, 100.0)
            if self.G_capitulos.RotarEnY  >= 1000:
                self.nivel +=1;
                self.G_capitulos = Capitulos.Capitulos(-0.90,-0.70,self.RotarEnY)
            glutDisplayFunc(self.G_capitulos.Close_Up_Flor)
            glutIdleFunc(self.G_capitulos.Close_Up_Flor)
            glMatrixMode(GL_MODELVIEW)
        #CAPITULO CUATRO
        if key == chr(32) and self.nivel == 3:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.CuatroEspinas()      
            
            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1
            
            glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
            glutIdleFunc(self.G_capitulos.Cap_Cuatro)

        #CAPITULO TRES
        if key == chr(32) and self.nivel == 2:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.TresPuesta()      

            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1

            glutDisplayFunc(self.G_capitulos.Cap_Tres)
            glutIdleFunc(self.G_capitulos.Cap_Tres)

        #CAPITULO DOS
        if key == chr(32) and self.nivel == 1:
            if self.changed == False:
                self.player.next_source()
                self.changed = True
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.DosAvion()           

            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1

            glutDisplayFunc(self.G_capitulos.Cap_Dos)
            glutIdleFunc(self.G_capitulos.Cap_Dos)

        #CAPITULO UNO
        if key == chr(32) and self.nivel == 0:
            if self.changed == False:
                self.player.next_source()
                self.changed = True
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.UnoPiloto()

            self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
            self.G_capitulos.Dialog_For = ""
            self.G_capitulos.Dialog_cont = 0
            self.G_capitulos.wrote = 0
            if self.G_capitulos.Scene_cont == len(self.G_dialogos.dialogos):
                self.nivel +=1
                self.G_capitulos.Scene_cont = 0
            self.G_capitulos.Scene_cont += 1

            glutDisplayFunc(self.G_capitulos.Cap_Uno)
            glutIdleFunc(self.G_capitulos.Cap_Uno)
            
    def keyOptions(self,key,x,y):
        if key == GLUT_KEY_UP:
            if self.player.volume < 1.00:
                self.player.volume += 0.1
        if key == GLUT_KEY_DOWN:
            if self.player.volume > 0.00:
                self.player.volume -= 0.1
        if key == GLUT_KEY_LEFT:
            if self.G_capitulos.time > 0.0:
                getcontext().prec = 2
                self.G_capitulos.time = float(Decimal(self.G_capitulos.time) - Decimal(0.01))
        if key == GLUT_KEY_RIGHT:
            if self.G_capitulos.time < 0.50:
                getcontext().prec = 2
                self.G_capitulos.time = float(Decimal(self.G_capitulos.time) + Decimal(0.01))
        glutPostRedisplay()
    def main(self):
        
        self.Thread_Music = threading.Thread(name="Music", target=self.Music)
        self.Thread_Music.start();
        glutInit(sys.argv)
        glutInitWindowSize(1280,720)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Ventana")
        glutFullScreen()
        glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
            
        glMatrixMode(GL_PROJECTION);
        glutDisplayFunc(self.G_capitulos.Portada)

        #glutDisplayFunc(self.G_capitulos.desierto)
        #glutIdleFunc(self.G_principito_front.principito)

        glClearColor(0.027, 0.823, 0.835, 0.0)
        #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
       
        glutKeyboardFunc(self.keyPress)
        glutSpecialFunc(self.keyOptions)
        glutMainLoop()
    def Music(self):
        self.player.queue(pyglet.media.load("00Menu.mp3"))
        self.player.queue(pyglet.media.load("01TemaDesierto.mp3"))
        self.player.play();
        self.player.volume = 0.1
        pyglet.app.run()

View = Main();
View.main();
# End of Program