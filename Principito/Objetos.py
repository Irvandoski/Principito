from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

class Objetos():

     def __init__(self,escalar,w,h):
        self.escalaX = 1 * escalar;
        self.escalaY = 16/9 * escalar
        self.w = w
        self.h = h

     def cuadro_pequeño(self):
        #fondo cabello
        glColor3ub(240, 240, 240)
        glBegin(GL_QUADS)
        glVertex2f(-0.40 * self.escalaX,  0.25 * self.escalaY)
        glVertex2f( 0.40 * self.escalaX,  0.25 * self.escalaY)
        glVertex2f( 0.40 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f(-0.40 * self.escalaX, -0.25 * self.escalaY)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.07 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f( 0.16 * self.escalaX, -0.25 * self.escalaY)
        glVertex2f( 0.20 * self.escalaX, -0.43 * self.escalaY)
        glEnd()

     def cuadro_grande(self):
        #fondo cabello
        glColor3ub(119, 66, 3)
        glBegin(GL_POLYGON)
        glVertex2f(-0.99, -0.61)
        glVertex2f(-0.99, -0.85)
        glVertex2f(-0.90, -0.99)
        glVertex2f( 0.90, -0.99)
        glVertex2f( 0.99, -0.85)
        glVertex2f( 0.99, -0.61)
        glVertex2f( 0.90, -0.47)
        glVertex2f(-0.90, -0.47)
        glEnd()
        glColor3ub(240, 240, 240)
        glBegin(GL_POLYGON)
        glVertex2f(-0.96, -0.61)
        glVertex2f(-0.96, -0.85)
        glVertex2f(-0.88, -0.94)
        glVertex2f( 0.88, -0.94)
        glVertex2f( 0.96, -0.85)
        glVertex2f( 0.96, -0.61)
        glVertex2f( 0.88, -0.52)
        glVertex2f(-0.88, -0.52)
        glEnd()
        
     def escritorio(self):
        #fondo cabello
        glColor3ub(131, 82, 11)
        glBegin(GL_QUADS)
        glVertex2f( 0.40, -0.20)
        glVertex2f( 0.20, -0.20)
        glVertex2f( 0.20, -0.60)
        glVertex2f( 0.40, -0.60)
        glEnd()
        glColor3ub(116, 106, 20)
        glBegin(GL_QUADS)
        glVertex2f( 0.40, -0.40)
        glVertex2f( 0.60, -0.40)
        glVertex2f( 0.60, -0.80)
        glVertex2f( 0.40, -0.80)
        glEnd()
        glColor3ub(121, 111, 25)
        glBegin(GL_QUADS)
        glVertex2f( 0.40, -0.40)
        glVertex2f( 0.60, -0.40)
        glVertex2f( 0.40, -0.20)
        glVertex2f( 0.20, -0.20)
        glEnd()

     def Avioneta(self):
        #fondo cabello
        glColor3ub(255, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.30 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w, -0.07 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w, -0.13 * self.escalaY + self.h)
        glEnd()
        glColor3ub(200, 18, 18)
        glBegin(GL_POLYGON)
        glVertex2f( 0.28 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.23 * self.escalaX + self.w, -0.18 * self.escalaY + self.h)
        glVertex2f(-0.35 * self.escalaX + self.w, -0.08 * self.escalaY + self.h)
        glVertex2f(-0.27 * self.escalaX + self.w,  0.07 * self.escalaY + self.h)
        glVertex2f( 0.24 * self.escalaX + self.w,  0.23 * self.escalaY + self.h)
        glVertex2f( 0.30 * self.escalaX + self.w,  0.42 * self.escalaY + self.h)
        glVertex2f( 0.37 * self.escalaX + self.w,  0.27 * self.escalaY + self.h)
        glVertex2f( 0.33 * self.escalaX + self.w,  0.08 * self.escalaY + self.h)
        glEnd()
        glColor3ub(255, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.05 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w,  0.18 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.25 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w,  0.12 * self.escalaY + self.h)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.05 * self.escalaY + self.h)
        glVertex2f(-0.55 * self.escalaX + self.w,  0.18 * self.escalaY + self.h)
        glVertex2f(-0.45 * self.escalaX + self.w,  0.25 * self.escalaY + self.h)
        glVertex2f( 0.12 * self.escalaX + self.w,  0.12 * self.escalaY + self.h)
        glEnd()
        glColor3ub(120, 120, 120)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.15 * self.escalaX + self.w,  0.08 * self.escalaY + self.h)
        glVertex2f(-0.12 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)

        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.13 * self.escalaX + self.w, -0.23 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.30 * self.escalaY + self.h)
        
        glVertex2f(-0.30 * self.escalaX + self.w, -0.10 * self.escalaY + self.h)
        glVertex2f(-0.54 * self.escalaX + self.w, -0.12 * self.escalaY + self.h)
        glVertex2f(-0.52 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glEnd()

     def Faro2DPrendido(self):
        #fondo cabello
        glColor3ub(0, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f( 0.20 * self.escalaX + self.w, -0.80 * self.escalaY + self.h)
        glVertex2f( 0.20 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.80 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f( 0.025 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f( 0.025 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.025 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.025 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.00 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.00 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glColor3ub(255, 235, 0)
        glVertex2f( 0.07 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f( 0.07 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f(-0.07 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f(-0.07 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glColor3ub(0, 0, 0)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)

        glVertex2f( 0.06 * self.escalaX + self.w, 0.225 * self.escalaY + self.h)
        glVertex2f( 0.06 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f(-0.06 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f(-0.06 * self.escalaX + self.w, 0.225 * self.escalaY + self.h)
        glEnd()

     def Faro2DApagado(self):
        #fondo cabello
        glColor3ub(0, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f( 0.20 * self.escalaX + self.w, -0.80 * self.escalaY + self.h)
        glVertex2f( 0.20 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f(-0.20 * self.escalaX + self.w, -0.80 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, -0.775 * self.escalaY + self.h)
        glVertex2f( 0.025 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f( 0.025 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.025 * self.escalaX + self.w,  0.00 * self.escalaY + self.h)
        glVertex2f(-0.025 * self.escalaX + self.w, -0.75 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.00 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.00 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glColor3ub(85, 0, 186)
        glVertex2f( 0.07 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f( 0.07 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f(-0.07 * self.escalaX + self.w, 0.025 * self.escalaY + self.h)
        glVertex2f(-0.07 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glColor3ub(0, 0, 0)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f( 0.10 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.175 * self.escalaY + self.h)
        glVertex2f(-0.10 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)

        glVertex2f( 0.06 * self.escalaX + self.w, 0.225 * self.escalaY + self.h)
        glVertex2f( 0.06 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f(-0.06 * self.escalaX + self.w, 0.20 * self.escalaY + self.h)
        glVertex2f(-0.06 * self.escalaX + self.w, 0.225 * self.escalaY + self.h)
        glEnd()

     def Flor(self):
        glColor3ub(137, 255, 133)
        glBegin(GL_QUADS)
        vx = [ 0.050, -0.050 ];
        vy = [ 0.000, 0.800 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        glColor3ub(135, 245, 120)
        vx = [ 0.080, -0.020 ];
        vy = [ 0.100,  0.200 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        glColor3ub(140, 246, 130)
        vx = [ 0.050, -0.050 ];
        vy = [ 0.250,  0.350 ];
        vz = [ 0.080, -0.020 ];
        self.Box(vx,vy,vz);
        glColor3ub(135, 250, 140)
        vx = [ 0.020, -0.080 ];
        vy = [ 0.400,  0.500 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        glColor3ub(135, 245, 120)
        vx = [ 0.050, -0.050 ];
        vy = [ 0.600,  0.500 ];
        vz = [ 0.020, -0.080 ];
        self.Box(vx,vy,vz);
        #Capa 1 de petalos
        glColor3ub(255, 120, 120)
        vx = [ 0.110,  -0.110 ];
        vy = [ 0.800,   1.000 ];
        vz = [ 0.050,   0.085 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 100, 110)
        vx = [ 0.050,   0.085 ];
        vy = [ 0.800,   1.000 ];
        vz = [ 0.110,  -0.110 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 80, 100)
        vx = [-0.110,   0.110 ];
        vy = [ 0.800,   1.000 ];
        vz = [-0.050,  -0.085 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 60, 90)
        vx = [-0.050,  -0.085 ];
        vy = [ 0.800,   1.000 ];
        vz = [-0.110,   0.110 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 110, 110)
        #Capa 2 de petalos
        vx = [ 0.050,  -0.050 ];
        vy = [ 0.900,   1.020 ];
        vz = [ 0.085,   0.150 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 90, 103)
        vx = [ 0.085,   0.150 ];
        vy = [ 0.900,   1.020 ];
        vz = [ 0.050,  -0.050 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 70, 96)
        vx = [-0.050,   0.050 ];
        vy = [ 0.900,   1.020 ];
        vz = [-0.085,  -0.150 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 50, 89)
        vx = [-0.085,  -0.150 ];
        vy = [ 0.900,   1.020 ];
        vz = [-0.050,   0.050 ];
        self.Box(vx,vy,vz);
        
        glColor3ub(170, 170, 170)
        glVertex3f( 100.0 , -0.01,  100.0)
        glVertex3f(-100.0 , -0.01,  100.0)
        glVertex3f(-100.0 , -0.01, -100.0)
        glVertex3f( 100.0 , -0.01, -100.0)
        
        glColor3ub(130, 130, 130)
        sum = 9
        glVertex3f( 4.5 + sum,  0.00,  3.0)
        glVertex3f(-4.5 + sum,  0.00,  3.0)
        glVertex3f(-4.5 + sum,  0.00, -3.0)
        glVertex3f( 4.5 + sum,  0.00, -3.0)
        glVertex3f( 3.0 + sum,  0.00,  4.5)
        glVertex3f(-3.0 + sum,  0.00,  4.5)
        glVertex3f(-3.0 + sum,  0.00, -4.5)
        glVertex3f( 3.0 + sum,  0.00, -4.5)
        glColor3ub(140, 140, 140)
        sum = 17
        glVertex3f( 4.5 + sum,  0.00,  3.0 + sum)
        glVertex3f(-4.5 + sum,  0.00,  3.0 + sum)
        glVertex3f(-4.5 + sum,  0.00, -3.0 + sum)
        glVertex3f( 4.5 + sum,  0.00, -3.0 + sum)
        glVertex3f( 3.0 + sum,  0.00,  4.5 + sum)
        glVertex3f(-3.0 + sum,  0.00,  4.5 + sum)
        glVertex3f(-3.0 + sum,  0.00, -4.5 + sum)
        glVertex3f( 3.0 + sum,  0.00, -4.5 + sum)
        sum = -13
        glVertex3f( 4.5 + sum,  0.00,  3.0 + sum)
        glVertex3f(-4.5 + sum,  0.00,  3.0 + sum)
        glVertex3f(-4.5 + sum,  0.00, -3.0 + sum)
        glVertex3f( 4.5 + sum,  0.00, -3.0 + sum)
        glVertex3f( 3.0 + sum,  0.00,  4.5 + sum)
        glVertex3f(-3.0 + sum,  0.00,  4.5 + sum)
        glVertex3f(-3.0 + sum,  0.00, -4.5 + sum)
        glVertex3f( 3.0 + sum,  0.00, -4.5 + sum)
        sum = -10
        glVertex3f( 4.5,  0.00,  3.0 + sum)
        glVertex3f(-4.5,  0.00,  3.0 + sum)
        glVertex3f(-4.5,  0.00, -3.0 + sum)
        glVertex3f( 4.5,  0.00, -3.0 + sum)
        glVertex3f( 3.0,  0.00,  4.5 + sum)
        glVertex3f(-3.0,  0.00,  4.5 + sum)
        glVertex3f(-3.0,  0.00, -4.5 + sum)
        glVertex3f( 3.0,  0.00, -4.5 + sum)
        sum = 14
        glVertex3f( 4.5 - 9,  0.00,  3.0 + sum)
        glVertex3f(-4.5 - 9,  0.00,  3.0 + sum)
        glVertex3f(-4.5 - 9,  0.00, -3.0 + sum)
        glVertex3f( 4.5 - 9,  0.00, -3.0 + sum)
        glVertex3f( 3.0 - 9,  0.00,  4.5 + sum)
        glVertex3f(-3.0 - 9,  0.00,  4.5 + sum)
        glVertex3f(-3.0 - 9,  0.00, -4.5 + sum)
        glVertex3f( 3.0 - 9,  0.00, -4.5 + sum)
        glEnd()

     def Faro(self):
        glColor3ub(35, 35, 35)
        glBegin(GL_QUADS)
        vx=[0.2,-0.2];
        vy=[0,0.1];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        vx=[0.05,-0.05];
        vy=[0,1.3];
        vz=[0.05,-0.05];
        self.Box(vx,vy,vz);
        vx=[0.15,-0.15];
        vy=[1.3,1.4];
        vz=[0.15,-0.15];
        self.Box(vx,vy,vz);
        vx=[0.15,-0.15];
        vy=[1.7,1.8];
        vz=[0.15,-0.15];
        self.Box(vx,vy,vz);
        vx=[0.1,-0.1];
        vy=[1.8,1.85];
        vz=[0.1,-0.1];
        self.Box(vx,vy,vz);
        glColor3ub(217, 205, 95)
        vx=[0.1,-0.1];
        vy=[1.4,1.7];
        vz=[0.1,-0.1];
        self.Box(vx,vy,vz);
        glColor3ub(150, 41, 119)
        glVertex3f( 100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00, -100.0)
        glVertex3f( 100.0 ,  0.00, -100.0)
        glEnd()

     def Pozo(self):
        glColor3ub(60, 60, 60)
        glBegin(GL_QUADS)
        #Pared 1
        vx=[0.2,-0.2];
        vy=[0,0.3];
        vz=[0.2,0.3];
        self.Box(vx,vy,vz);
        #Pared 2
        vx=[0.2,0.3];
        vy=[0,0.3];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        #Pared 3
        vx=[0.2,-0.2];
        vy=[0,0.3];
        vz=[-0.2,-0.3];
        self.Box(vx,vy,vz);
        #Pared 4
        vx=[-0.2,-0.3];
        vy=[0,0.3];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        #Borde 1
        vx=[0.2,-0.2];
        vy=[0.3,0.4];  
        vz=[0.3,0.4];
        self.Box(vx,vy,vz);
        #Esquina 1
        vx=[0.2,0.3];
        vy=[0.3,0.4];  
        vz=[0.2,0.3];
        self.Box(vx,vy,vz);
        #Esquina 2
        vx=[-0.2,-0.3];
        vy=[0.3,0.4];  
        vz=[-0.2,-0.3];
        self.Box(vx,vy,vz);
        #Esquina 3
        vx=[0.2, 0.3];
        vy=[0.3,0.4];  
        vz=[-0.2,-0.3];
        self.Box(vx,vy,vz);
        #Esquina 4
        vx=[-0.2,-0.3];
        vy=[0.3,0.4];  
        vz=[0.2,0.3];
        self.Box(vx,vy,vz);
        #Borde 2
        vx=[0.3,0.4];
        vy=[0.3,0.4];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        #Borde 3
        vx=[0.2,-0.2];
        vy=[0.3,0.4];
        vz=[-0.3,-0.4];
        self.Box(vx,vy,vz);
        #Borde 4
        vx=[-0.3,-0.4];
        vy=[0.3,0.4];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        glColor3ub(175, 140, 90)
        #Poste 1
        vx=[-0.3,-0.4];
        vy=[0.4,0.9];
        vz=[0.05,-0.05];
        self.Box(vx,vy,vz);
        #Poste 2
        vx=[0.3,0.4];
        vy=[0.4,0.9];
        vz=[0.05,-0.05];
        self.Box(vx,vy,vz);
        
        glVertex3f(-0.40 ,  1.00,  0.00)
        glVertex3f(-0.40 ,  0.90, -0.05)
        glVertex3f(-0.40 ,  0.60,  0.45)
        glVertex3f(-0.40 ,  0.70,  0.50)

        glVertex3f(-0.40 ,  1.00, -0.00)
        glVertex3f(-0.40 ,  0.90,  0.05)
        glVertex3f(-0.40 ,  0.60, -0.45)
        glVertex3f(-0.40 ,  0.70, -0.50)


        glVertex3f( 0.40 ,  1.00,  0.00)
        glVertex3f( 0.40 ,  0.90, -0.05)
        glVertex3f( 0.40 ,  0.60,  0.45)
        glVertex3f( 0.40 ,  0.70,  0.50)

        glVertex3f( 0.40 ,  1.00, -0.00)
        glVertex3f( 0.40 ,  0.90,  0.05)
        glVertex3f( 0.40 ,  0.60, -0.45)
        glVertex3f( 0.40 ,  0.70, -0.50)


        glVertex3f( 0.40 ,  0.70, -0.50)
        glVertex3f( 0.40 ,  0.60, -0.45)
        glVertex3f(-0.40 ,  0.60, -0.45)
        glVertex3f(-0.40 ,  0.70, -0.50)
        
        glVertex3f( 0.40 ,  0.70,  0.50)
        glVertex3f( 0.40 ,  0.60,  0.45)
        glVertex3f(-0.40 ,  0.60,  0.45)
        glVertex3f(-0.40 ,  0.70,  0.50)


        glVertex3f( 0.40 ,  0.70,  0.50)
        glVertex3f(-0.40 ,  0.70,  0.50)
        glVertex3f(-0.40 ,  1.00,  0.00)
        glVertex3f( 0.40 ,  1.00,  0.00)
        
        glVertex3f( 0.40 ,  0.70, -0.50)
        glVertex3f(-0.40 ,  0.70, -0.50)
        glVertex3f(-0.40 ,  1.00,  0.00)
        glVertex3f( 0.40 ,  1.00,  0.00)

        glColor3ub(135, 165, 205)
        #Agua
        vx=[0.2,-0.2];
        vy=[0,0.1];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        
        glColor3ub(207, 192, 112)
        glVertex3f( 100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00, -100.0)
        glVertex3f( 100.0 ,  0.00, -100.0)
        glEnd()

     def Zorro(self):
        glBegin(GL_QUADS)
        #Cuerpo
        glColor3ub(239, 135, 0)
        glVertex3f(-0.18 ,  0.00,  0.20)
        glVertex3f(-0.18 ,  0.00, -0.20)
        glVertex3f( 0.18 ,  0.60, -0.20)
        glVertex3f( 0.18 ,  0.60,  0.20)

        glVertex3f( 0.18 ,  0.60,  0.20)
        glVertex3f( 0.18 ,  0.60, -0.20)
        glVertex3f(-0.18 ,  0.00, -0.20)
        glVertex3f(-0.18 ,  0.00,  0.20)

        glVertex3f(-0.18 ,  0.00, -0.20)
        glVertex3f( 0.18 ,  0.60, -0.20)
        glVertex3f(-0.09 ,  0.75, -0.20)
        glVertex3f(-0.42 ,  0.15, -0.20)
        
        glVertex3f(-0.42 ,  0.15, -0.20)
        glVertex3f(-0.09 ,  0.75, -0.20)
        glVertex3f( 0.18 ,  0.60, -0.20)
        glVertex3f(-0.18 ,  0.00, -0.20)

        glVertex3f(-0.18 ,  0.00,  0.20)
        glVertex3f( 0.18 ,  0.60,  0.20)
        glVertex3f(-0.09 ,  0.75,  0.20)
        glVertex3f(-0.42 ,  0.15,  0.20)
        
        glVertex3f(-0.42 ,  0.15,  0.20)
        glVertex3f(-0.09 ,  0.75,  0.20)
        glVertex3f( 0.18 ,  0.60,  0.20)
        glVertex3f(-0.18 ,  0.00,  0.20)

        glVertex3f(-0.09 ,  0.75,  0.20)
        glVertex3f(-0.09 ,  0.75, -0.20)
        glVertex3f(-0.42 ,  0.15, -0.20)
        glVertex3f(-0.42 ,  0.15,  0.20)
        
        glVertex3f(-0.42 ,  0.15,  0.20)
        glVertex3f(-0.42 ,  0.15, -0.20)
        glVertex3f(-0.09 ,  0.75, -0.20)
        glVertex3f(-0.09 ,  0.75,  0.20)
        #Cola1
        vx=[0.3,-0.5];
        vy=[0,0.3];
        vz=[0.4,0.7];
        self.Box(vx,vy,vz);
        #Cola2
        vx=[-0.3,-0.6];
        vy=[0,0.3];
        vz=[0,0.6];
        self.Box(vx,vy,vz);
        #PataAtIzq
        vx=[0,-0.2];
        vy=[0,0.1];
        vz=[0.1,0.2];
        self.Box(vx,vy,vz);
        #PataAtDer
        vx=[0,-0.2];
        vy=[0,0.1];
        vz=[-0.1,-0.2];
        self.Box(vx,vy,vz);
        #PataFrontIzq
        vx=[0.1,0.2];
        vy=[0,0.6];
        vz=[0.1,0.2];
        self.Box(vx,vy,vz);
        #PataFrontDer
        vx=[0.1,0.2];
        vy=[0,0.6];
        vz=[-0.1,-0.2];
        self.Box(vx,vy,vz);
        #Cabeza
        vx=[-0.1,0.3];
        vy=[0.6,1];
        vz=[0.2,-0.2];
        self.Box(vx,vy,vz);
        #OrejitaDer
        vx=[0.05,0.15];
        vy=[0.85,1.05];
        vz=[-0.15,-0.35];
        self.Box(vx,vy,vz);
        
        #Oreja chueca
        glVertex3f( 0.05 ,  0.80,  0.20)
        glVertex3f( 0.05 ,  0.95,  0.05)
        glVertex3f( 0.05 ,  1.10,  0.23)
        glVertex3f( 0.05 ,  0.95,  0.38)
        
        glVertex3f( 0.05 ,  0.95,  0.38)
        glVertex3f( 0.05 ,  1.10,  0.23)
        glVertex3f( 0.05 ,  0.95,  0.05)
        glVertex3f( 0.05 ,  0.80,  0.20)
        
        glVertex3f( 0.15 ,  0.80,  0.20)
        glVertex3f( 0.15 ,  0.95,  0.05)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  0.95,  0.38)
        
        glVertex3f( 0.15 ,  0.95,  0.38)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  0.95,  0.05)
        glVertex3f( 0.15 ,  0.80,  0.20)

        glVertex3f( 0.05 ,  0.80,  0.20)
        glVertex3f( 0.15 ,  0.80,  0.20)
        glVertex3f( 0.15 ,  0.95,  0.38)
        glVertex3f( 0.05 ,  0.95,  0.38)
        
        glVertex3f( 0.05 ,  0.95,  0.38)
        glVertex3f( 0.15 ,  0.95,  0.38)
        glVertex3f( 0.15 ,  0.80,  0.20)
        glVertex3f( 0.05 ,  0.80,  0.20)

        glVertex3f( 0.05 ,  0.95,  0.05)
        glVertex3f( 0.15 ,  0.95,  0.05)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.05 ,  1.10,  0.23)
        
        glVertex3f( 0.05 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  0.95,  0.05)
        glVertex3f( 0.05 ,  0.95,  0.05)
        
        glVertex3f( 0.05 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.15 ,  0.95,  0.38)
        glVertex3f( 0.05 ,  0.95,  0.38)
        
        glVertex3f( 0.05 ,  0.95,  0.38)
        glVertex3f( 0.15 ,  0.95,  0.38)
        glVertex3f( 0.15 ,  1.10,  0.23)
        glVertex3f( 0.05 ,  1.10,  0.23)

        #ColaPunta
        glColor3ub(255, 255, 255)
        vx=[0.3,0.35];
        vy=[0.05,0.25];
        vz=[0.45,0.65];
        self.Box(vx,vy,vz);
        #Cachetes
        vx=[0.2,0.35];
        vy=[0.6,0.8];
        vz=[0.25,-0.25];
        self.Box(vx,vy,vz);
        #Trompita
        vx=[0.3,0.5];
        vy=[0.6,0.8];
        vz=[0.1,-0.1];
        self.Box(vx,vy,vz);
        #Nariz
        glColor3ub(0, 0, 0)
        vx=[0.45,0.55];
        vy=[0.75,0.85];
        vz=[0.05,-0.05];
        self.Box(vx,vy,vz);
        #OjoIzq
        vx=[0.3,0.35];
        vy=[0.85,0.95];
        vz=[0.05,0.15];
        self.Box(vx,vy,vz);
        #OjoDer
        vx=[0.3,0.35];
        vy=[0.85,0.95];
        vz=[-0.05,-0.15];
        self.Box(vx,vy,vz);
        
        glColor3ub(76, 128, 50)
        glVertex3f( 100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00,  100.0)
        glVertex3f(-100.0 ,  0.00, -100.0)
        glVertex3f( 100.0 ,  0.00, -100.0)
        glEnd()
        #glBegin(GL_TRIANGLES)
        #glColor3ub(76, 128, 50)
        #glVertex3f( 30,  0.00,  30)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 60,  0.00,  30)
        
        #glVertex3f( 60,  0.00,  30)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 30,  0.00,  30)

        #glVertex3f( 30,  0.00,  30)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 30,  0.00,  60)
        
        #glVertex3f( 30,  0.00,  60)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 30,  0.00,  30)
        
        #glVertex3f( 60,  0.00,  60)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 60,  0.00,  30)
        
        #glVertex3f( 60,  0.00,  30)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 60,  0.00,  60)
        
        #glVertex3f( 60,  0.00,  60)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 30,  0.00,  60)
        
        #glVertex3f( 30,  0.00,  60)
        #glVertex3f( 45,  2.00,  45)
        #glVertex3f( 60,  0.00,  60)
        #glEnd()

     def Box(self,vx,vy,vz):
        i = 0;
        sumando = 1;
        for y in vy:
            for x in vx:
                glVertex3f( x ,  y,  vz[i])
                i = i + sumando
                glVertex3f( x ,  y,  vz[i])
                sumando = sumando * -1
        for z in vz:
            for x in vx:
                glVertex3f( x ,  vy[i],  z)
                i = i + sumando
                glVertex3f( x ,  vy[i],  z)
                sumando = sumando * -1
        for x in vx:
            for z in vz:
                glVertex3f( x ,  vy[i],  z)
                i = i + sumando
                glVertex3f( x ,  vy[i],  z)
                sumando = sumando * -1

        i = 1;
        sumando = -1;

        for y in vy:
            for x in vx:
                glVertex3f( x ,  y,  vz[i])
                i = i + sumando
                glVertex3f( x ,  y,  vz[i])
                sumando = sumando * -1
        for z in vz:
            for x in vx:
                glVertex3f( x ,  vy[i],  z)
                i = i + sumando
                glVertex3f( x ,  vy[i],  z)
                sumando = sumando * -1
        for x in vx:
            for z in vz:
                glVertex3f( x ,  vy[i],  z)
                i = i + sumando
                glVertex3f( x ,  vy[i],  z)
                sumando = sumando * -1  