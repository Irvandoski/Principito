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
        self.G_capitulos = Capitulos.Capitulos(-0.90,-0.68, 0.0)
        self.G_dialogos = Dialogos.Dialogos()
        self.nivel = 1
        self.cont_dialog = 0
        self.Thread_Music = threading.Thread();
        self.musica = pyglet.resource.media('00Menu.mp3', streaming=True)
        self.player=pyglet.media.Player()
        self.reading = False
        self.nextlevel = ''
        self.indexsong = 0;
        self.songnumber = 0;
        #self.cls3D = Tridimensional.Tridimensional()
    def keyPress(self,bkey,x,y):
        key = bkey.decode("utf-8")
        #SALIR
        if key == "n":
            if self.reading:
                try:
                    self.nivel = int(self.nextlevel);
                    key =  chr(32) 
                    self.nextlevel += '';
                except :
                    pass
                self.reading = False;
            else:
                self.reading = True;
        else:
            if self.reading:
                try:
                    self.nextlevel += key;
                except :
                    pass
        if key == chr(27) or self.nivel == 22:
            pyglet.app.exit()
            self.Thread_Music.join()
            os._exit(1) 
            sys.exit()
        if key == chr(32):
            
            if self.nivel == 21:
                glClearColor(0, 0, 0, 0.0)
                self.G_dialogos.Veintiuno()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Veintiuno)
                    glutIdleFunc(self.G_capitulos.Cap_Veintiuno)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Veintiuno)
                    glutIdleFunc(self.G_capitulos.Cap_Veintiuno)
                self.G_capitulos.Scene_cont += 1
            #CAPITULO VEINTE
            if self.nivel == 20:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.Veinte()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Veintiuno)
                    glutIdleFunc(self.G_capitulos.Cap_Veintiuno)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Veinte)
                    glutIdleFunc(self.G_capitulos.Cap_Veinte)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Veinte)
                    glutIdleFunc(self.G_capitulos.Cap_Veinte)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DIECINUEVE
            if self.nivel == 19:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.TreceGeografo()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Veinte)
                    glutIdleFunc(self.G_capitulos.Cap_Veinte)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Diecinueve)
                    glutIdleFunc(self.G_capitulos.Cap_Diecinueve)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Diecinueve)
                    glutIdleFunc(self.G_capitulos.Cap_Diecinueve)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DIECIOCHO
            if self.nivel == 18:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.TreceGeografo()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Diecinueve)
                    glutIdleFunc(self.G_capitulos.Cap_Diecinueve)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciocho)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciocho)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciocho)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciocho)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DIECISIETE
            if self.nivel == 17:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.DiecisieteDespedidaZorro()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 8;
                    self.nivel +=1;
                    self.G_capitulos.Dialog = ""
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    os.startfile('Pozo.pyw')
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciocho)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciocho)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Diecisiete)
                    glutIdleFunc(self.G_capitulos.Cap_Diecisiete)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Diecisiete)
                    glutIdleFunc(self.G_capitulos.Cap_Diecisiete)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DIECISEIS
            if self.nivel == 16:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.DieciseisZorro()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Diecisiete)
                    glutIdleFunc(self.G_capitulos.Cap_Diecisiete)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciseis)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciseis)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciseis)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciseis)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO QUINCE 
            if self.nivel == 15:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.QuinceFlores()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 8;
                    self.nivel +=1;
                    self.G_capitulos.Dialog = ""
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    os.startfile('Zorro.pyw')
                    glutDisplayFunc(self.G_capitulos.Cap_Dieciseis)
                    glutIdleFunc(self.G_capitulos.Cap_Dieciseis)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Quince)
                    glutIdleFunc(self.G_capitulos.Cap_Quince)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Quince)
                    glutIdleFunc(self.G_capitulos.Cap_Quince)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO CATORCE
            if self.nivel == 14:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.CatorceSerpiente()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Quince)
                    glutIdleFunc(self.G_capitulos.Cap_Quince)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Catorce)
                    glutIdleFunc(self.G_capitulos.Cap_Catorce)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Catorce)
                    glutIdleFunc(self.G_capitulos.Cap_Catorce)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO TRECE
            if self.nivel == 13:
                self.songnumber = 8;
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.TreceGeografo()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Catorce)
                    glutIdleFunc(self.G_capitulos.Cap_Catorce)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Trece)
                    glutIdleFunc(self.G_capitulos.Cap_Trece)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Trece)
                    glutIdleFunc(self.G_capitulos.Cap_Trece)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DOCE
            if self.nivel == 12:
                self.songnumber = 7;
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.DoceFarolero()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 8;
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Trece)
                    glutIdleFunc(self.G_capitulos.Cap_Trece)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Doce)
                    glutIdleFunc(self.G_capitulos.Cap_Doce)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Doce)
                    glutIdleFunc(self.G_capitulos.Cap_Doce)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO ONCE
            if self.nivel == 11:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 6;
                self.G_dialogos.OnceNegocios()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 7;
                    self.nivel +=1;
                    self.G_capitulos.Dialog = ""
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    os.startfile('Faro.pyw')
                    glutDisplayFunc(self.G_capitulos.Cap_Doce)
                    glutIdleFunc(self.G_capitulos.Cap_Doce)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Once)
                    glutIdleFunc(self.G_capitulos.Cap_Once)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Once)
                    glutIdleFunc(self.G_capitulos.Cap_Once)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO NUEVE
            if self.nivel == 9:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 5;
                self.G_dialogos.NueveBebedor()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 6;
                    self.nivel +=2;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Once)
                    glutIdleFunc(self.G_capitulos.Cap_Once)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                    glutIdleFunc(self.G_capitulos.Cap_Nueve)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                    glutIdleFunc(self.G_capitulos.Cap_Nueve)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO OCHO
            if self.nivel == 8:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 4;
                self.G_dialogos.OchoVanidoso()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 5;
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Nueve)
                    glutIdleFunc(self.G_capitulos.Cap_Nueve)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                    glutIdleFunc(self.G_capitulos.Cap_Ocho)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                    glutIdleFunc(self.G_capitulos.Cap_Ocho)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO SIETE
            if self.nivel == 7:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 3;
                self.G_dialogos.SieteRey()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 4;
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Ocho)
                    glutIdleFunc(self.G_capitulos.Cap_Ocho)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Siete)
                    glutIdleFunc(self.G_capitulos.Cap_Siete)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Siete)
                    glutIdleFunc(self.G_capitulos.Cap_Siete)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO SEIS
            if self.nivel == 6:
                self.songnumber = 2;
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.SeisByeFlor()
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 3;
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Siete)
                    glutIdleFunc(self.G_capitulos.Cap_Siete)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Seis)
                    glutIdleFunc(self.G_capitulos.Cap_Seis)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Seis)
                    glutIdleFunc(self.G_capitulos.Cap_Seis)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO CINCO
            if self.nivel == 5:
                self.songnumber = 2;
                glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
            
                glMatrixMode(GL_PROJECTION);
                #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
                glOrtho(-1.0, 1.0, -1.0, 1.0, -1, 1);
       
                glClearColor(0.027, 0.823, 0.835, 0.0)

                self.G_dialogos.CincoFlor()
            
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Seis)
                    glutIdleFunc(self.G_capitulos.Cap_Seis)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                    glutIdleFunc(self.G_capitulos.Cap_Cinco)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                    glutIdleFunc(self.G_capitulos.Cap_Cinco)
                self.G_capitulos.Scene_cont += 1


            #CAPITULO CUATRO
            if self.nivel == 4:
                self.songnumber = 1;
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.G_dialogos.CuatroEspinas()      
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.songnumber = 2;
                    self.nivel +=1;
                    self.G_capitulos.Dialog = ""
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    os.startfile('Flor.pyw')
                    glutDisplayFunc(self.G_capitulos.Cap_Cinco)
                    glutIdleFunc(self.G_capitulos.Cap_Cinco)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                    glutIdleFunc(self.G_capitulos.Cap_Cuatro)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                    glutIdleFunc(self.G_capitulos.Cap_Cuatro)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO TRES
            if self.nivel == 3:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 1;
                self.G_dialogos.TresPuesta()      
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Cuatro)
                    glutIdleFunc(self.G_capitulos.Cap_Cuatro)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Tres)
                    glutIdleFunc(self.G_capitulos.Cap_Tres)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Tres)
                    glutIdleFunc(self.G_capitulos.Cap_Tres)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO DOS
            if self.nivel == 2:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 1;
                self.G_dialogos.DosAvion()           
                if self.G_capitulos.Scene_cont  -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1;
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Tres)
                    glutIdleFunc(self.G_capitulos.Cap_Tres)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1] 
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Dos)
                    glutIdleFunc(self.G_capitulos.Cap_Dos)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Dos)
                    glutIdleFunc(self.G_capitulos.Cap_Dos)
                self.G_capitulos.Scene_cont += 1

            #CAPITULO UNO
            if self.nivel == 1:
                glClearColor(0.027, 0.823, 0.835, 0.0)
                self.songnumber = 1;
                self.G_dialogos.UnoPiloto()
                if self.G_capitulos.Scene_cont -1 == len(self.G_dialogos.dialogos):
                    self.nivel +=1
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Scene_cont = 0
                    self.G_capitulos.Colorizar = 0                
                    glutDisplayFunc(self.G_capitulos.Cap_Dos)
                    glutIdleFunc(self.G_capitulos.Cap_Dos)
                elif self.G_capitulos.Scene_cont != 0:
                    self.G_capitulos.Dialog = self.G_dialogos.dialogos[self.G_capitulos.Scene_cont-1]
                    self.G_capitulos.Dialog_For_A = ""
                    self.G_capitulos.Dialog_For_B = ""
                    self.G_capitulos.Dialog_For_C = ""
                    self.G_capitulos.Dialog_cont = 0
                    self.G_capitulos.wrote = 0
                    glutDisplayFunc(self.G_capitulos.Cap_Uno)
                    glutIdleFunc(self.G_capitulos.Cap_Uno)
                else:
                    glutDisplayFunc(self.G_capitulos.Cap_Uno)
                    glutIdleFunc(self.G_capitulos.Cap_Uno)
                self.G_capitulos.Scene_cont += 1

            while (self.indexsong < self.songnumber):
                self.player.next_source()
                self.indexsong +=1
            
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
        self.player.queue(pyglet.media.load("05Ebrio.mp3"))
        self.player.queue(pyglet.media.load("06BuisnessMen.mp3"))
        self.player.queue(pyglet.media.load("07Farolero.mp3"))
        self.player.queue(pyglet.media.load("08Geologo.mp3"))
        self.player.queue(pyglet.media.load("10Muerte.mp3"))
        self.player.play();
        self.player.volume = 0.1
        pyglet.app.run()

View = Main();
View.main();
# End of Program