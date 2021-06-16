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
        self.RotarEnY = 0
        self.screen= ctypes.windll.user32
        self.width = self.screen.GetSystemMetrics(0)
        self.height = self.screen.GetSystemMetrics(1)
        self.G_capitulos = Capitulos.Capitulos(-0.90,-0.70, 0.0)
        self.G_dialogos = Dialogos.Dialogos()
        self.nivel = 0
        self.cont_dialog = 0
        self.Thread_Music = threading.Thread();
        self.musica = pyglet.resource.media('00Menu.mp3', streaming=True)
        self.player=pyglet.media.Player()
        self.changed = False
        self.reading = False
    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if self.reading:
            try:
                self.nivel = 12;
                #self.nivel = int(key);
            except :
                pass
            key =  chr(32) 
            self.reading = False;
        if key == "n":
            self.reading = True;
        if key == chr(27):
            pyglet.app.exit()
            self.Thread_Music.join()
            os._exit(1) 
            sys.exit()
            
        #CAPITULO TRECE (PENDIENTE)
        if key == chr(32) and self.nivel == 13:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.TreceGeografo()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Trece)
                glutIdleFunc(self.G_capitulos.Cap_Trece)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Trece)
                glutIdleFunc(self.G_capitulos.Cap_Trece)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Trece)
                glutIdleFunc(self.G_capitulos.Cap_Trece)
            self.G_capitulos.Scene_cont += 1
        #CAPITULO DOCE (PENDIENTE)
        if key == chr(32) and self.nivel == 12:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.DoceFarolero()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Trece)
                glutIdleFunc(self.G_capitulos.Cap_Trece)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Doce)
                glutIdleFunc(self.G_capitulos.Cap_Doce)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Doce)
                glutIdleFunc(self.G_capitulos.Cap_Doce)
            self.G_capitulos.Scene_cont += 1
        #CAPITULO ONCE (PENDIENTE)
        if key == chr(32) and self.nivel == 11:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.OnceNegocios()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Doce)
                glutIdleFunc(self.G_capitulos.Cap_Doce)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Once)
                glutIdleFunc(self.G_capitulos.Cap_Once)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Once)
                glutIdleFunc(self.G_capitulos.Cap_Once)
            self.G_capitulos.Scene_cont += 1
        #CAPITULO NUEVE (PENDIENTE)
        if key == chr(32) and self.nivel == 9:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.NueveBebedor()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=2;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Once)
                glutIdleFunc(self.G_capitulos.Cap_Once)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                glutIdleFunc(self.G_capitulos.Cap_Nueve)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                glutIdleFunc(self.G_capitulos.Cap_Nueve)
            self.G_capitulos.Scene_cont += 1
        #CAPITULO OCHO
        if key == chr(32) and self.nivel == 8:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.OchoVanidoso()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                glutIdleFunc(self.G_capitulos.Cap_Nueve)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                glutIdleFunc(self.G_capitulos.Cap_Ocho)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                glutIdleFunc(self.G_capitulos.Cap_Ocho)
            self.G_capitulos.Scene_cont += 1
        #CAPITULO SIETE
        if key == chr(32) and self.nivel == 7:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.SieteRey()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.changed = False;
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                glutIdleFunc(self.G_capitulos.Cap_Ocho)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Siete)
                glutIdleFunc(self.G_capitulos.Cap_Siete)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Siete)
                glutIdleFunc(self.G_capitulos.Cap_Siete)
            self.G_capitulos.Scene_cont += 1

        #CAPITULO SEIS
        if key == chr(32) and self.nivel == 6:
            glClearColor(0.027, 0.823, 0.835, 0.0)
            self.G_dialogos.SeisByeFlor()
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.changed = False;
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Siete)
                glutIdleFunc(self.G_capitulos.Cap_Siete)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Seis)
                glutIdleFunc(self.G_capitulos.Cap_Seis)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Seis)
                glutIdleFunc(self.G_capitulos.Cap_Seis)
            self.G_capitulos.Scene_cont += 1

        #CAPITULO CINCO
        if key == chr(32) and self.nivel == 5:
            
            glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
            
            glMatrixMode(GL_PROJECTION);
            #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
            glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
       
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.CincoFlor()
            
            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Seis)
                glutIdleFunc(self.G_capitulos.Cap_Seis)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                glutIdleFunc(self.G_capitulos.Cap_Cinco)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                glutIdleFunc(self.G_capitulos.Cap_Cinco)
            self.G_capitulos.Scene_cont += 1

        #CLOSE UP FLOR
        if key == chr(32) and self.nivel == 4:
            gluPerspective(45.0, float(1280)/float(720), 0.1, 100.0)
            if self.G_capitulos.RotarEnY  >= 500:
                self.nivel +=1;
                self.G_capitulos = Capitulos.Capitulos(-0.90,-0.70, 0.0)
                glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
                glClear(GL_DEPTH_BUFFER_BIT);
                glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
                glMatrixMode(GL_PROJECTION);
                glClearColor(0.027, 0.823, 0.835, 0.0)
                glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                glutIdleFunc(self.G_capitulos.Cap_Cinco)
            else:            
                glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
                glClearColor(0.0, 0.0, 0.0, 0.0)
                glClearDepth(1.0)
                glShadeModel(GL_SMOOTH)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(45.0, float(1280)/float(720), 0.1, 100.0)
                glutDisplayFunc(self.G_capitulos.Close_Up_Flor)
                glutIdleFunc(self.G_capitulos.Close_Up_Flor)
                glMatrixMode(GL_MODELVIEW)

        #CAPITULO CUATRO
        if key == chr(32) and self.nivel == 3:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.CuatroEspinas()      

            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.changed = False;
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
                glClearColor(0.0, 0.0, 0.0, 0.0)
                glClearDepth(1.0)
                glShadeModel(GL_SMOOTH)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(45.0, float(1280)/float(720), 0.1, 100.0)
                glutDisplayFunc(self.G_capitulos.Close_Up_Flor)
                glutIdleFunc(self.G_capitulos.Close_Up_Flor)
                glMatrixMode(GL_MODELVIEW)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                glutIdleFunc(self.G_capitulos.Cap_Cuatro)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                glutIdleFunc(self.G_capitulos.Cap_Cuatro)
            self.G_capitulos.Scene_cont += 1

        #CAPITULO TRES
        if key == chr(32) and self.nivel == 2:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.TresPuesta()      

            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                glutIdleFunc(self.G_capitulos.Cap_Cuatro)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Tres)
                glutIdleFunc(self.G_capitulos.Cap_Tres)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Tres)
                glutIdleFunc(self.G_capitulos.Cap_Tres)
            self.G_capitulos.Scene_cont += 1

        #CAPITULO DOS
        if key == chr(32) and self.nivel == 1:
            if self.changed == False:
                self.player.next_source()
                self.changed = True
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.DosAvion()           

            if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1;
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0
                glutDisplayFunc(self.G_capitulos.Cap_Tres)
                glutIdleFunc(self.G_capitulos.Cap_Tres)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Dos)
                glutIdleFunc(self.G_capitulos.Cap_Dos)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Dos)
                glutIdleFunc(self.G_capitulos.Cap_Dos)
            self.G_capitulos.Scene_cont += 1

        #CAPITULO UNO
        if key == chr(32) and self.nivel == 0:
            glClearColor(0.027, 0.823, 0.835, 0.0)

            self.G_dialogos.UnoPiloto()
            if self.G_capitulos.Scene_cont -1 == len(self.G_dialogos.dialogos):
                self.nivel +=1
                self.G_capitulos.Scene_cont = 0
                self.G_capitulos.Colorizar = 0                
                glutDisplayFunc(self.G_capitulos.Cap_Dos)
                glutIdleFunc(self.G_capitulos.Cap_Dos)
            elif self.G_capitulos.Scene_cont != 0:
                self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
                self.G_capitulos.Dialog_For = ""
                self.G_capitulos.Dialog_cont = 0
                self.G_capitulos.wrote = 0
                glutDisplayFunc(self.G_capitulos.Cap_Uno)
                glutIdleFunc(self.G_capitulos.Cap_Uno)
            else:
                glutDisplayFunc(self.G_capitulos.Cap_Uno)
                glutIdleFunc(self.G_capitulos.Cap_Uno)
            self.G_capitulos.Scene_cont += 1
        if self.changed == False:
            self.player.next_source()
            self.changed = True
            
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
        glutSpecialFunc(self.keyOptions)
        glClearColor(0.027, 0.823, 0.835, 0.0)
        #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
        
        glutMainLoop()
    def Music(self):
        self.player.queue(pyglet.media.load("00Menu.mp3"))
        self.player.queue(pyglet.media.load("01TemaDesierto.mp3"))
        self.player.queue(pyglet.media.load("02Flor.mp3"))
        self.player.queue(pyglet.media.load("03Rey.mp3"))
        self.player.queue(pyglet.media.load("04Banidoso.mp3"))
        self.player.play();
        self.player.volume = 0.1
        pyglet.app.run()

View = Main();
View.main();
# End of Program