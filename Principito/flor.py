import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import time, sys

class Objetos:

    global RotarEnY

    def __init__(self):
        self.main()

    #inicializa la ventana donde desplegaremos los graficos
    def InitGL(self,Width, Height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    # Funcion que dibuja los objetos.
    def DibujarObjetos(self):
        global RotarEnY
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glClearColor(0.40, 0.58, 0.93, 0.0)

        # Habilita las sombras en el color
        glShadeModel(GL_SMOOTH)
        # Habilita la limpieza del buffer de profundidad
        glClearDepth(1.0)

        #Habilita el manejo del culling
        glEnable(GL_CULL_FACE)
        # Habilita la prueba de profundidad
        glEnable(GL_DEPTH_TEST)
        #Parametros para establecer las luces
        #Por default la luz es blanca y viene desde la direccion de Z
        #glEnable(GL_LIGHTING)
        #Variable utilizada para posicionar la luz 0
        # x, y, z, w
        lightZeroPosition = [10.,4.,10.,1.0]
        #Variable para establecer los colores de la luz 0
        lightZeroColor = [0.8,1.0,0.8,1.0]

        #Varible para establecer la luz de ambiente de la luz 0
        lightZeroAmbient = [0.6,1.0,0.6,1.0]
        #lightZeroAmbient = [1.6,1.1,5.6,1.1]

        #Crea la luz 0 con los parametros establecidos
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)

        # Establede el color la luz ambiente
        glLightfv(GL_LIGHT0, GL_AMBIENT, lightZeroAmbient)

        # Establede el color de la luz difusa
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)


        #glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        #glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)

        #Variable utilizada para posicionar la luz 1
        #lightUnoPosition = [20.5, 1.5, 10.0, 1.0]
        lightUnoPosition = [0.0, 0.0, 1.0, 0.0] # luz directional de frente
        #lightUnoPosition = [0.0, 0.0, 1.0, 1.0] # Luz point de left, top, front


        #Variable para establecer los colores de la luz 1
        lightUnoColor = [8.8,1.8,8.8,1.0]

        #Varible para establecer la luz de ambiente de la luz 1
        lightUnoAmbient = [8.6,1.8,8.6,1.0]

        #Crea la luz 1 con los parametros establecidos
        glLightfv(GL_LIGHT1, GL_POSITION, lightUnoPosition)

        # Establede el color la luz ambiente
        glLightfv(GL_LIGHT1, GL_AMBIENT, lightUnoAmbient)

        # Establede el color de la luz difusa
        glLightfv(GL_LIGHT1, GL_DIFFUSE, lightUnoColor)
        #glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
        #glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)

        #glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT0)

        #Color del objeto
        #color = [3.5,0.5,1.5,1.]
        #color = [3.5,2.5,1.5,3.5]

        #Luz difusa del objeto
        #glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
        glTranslatef(0.0, -1.0, -3.0)
        glRotatef(RotarEnY,0.0,1.0,0.0)

        #Esferas:
        #glutWireSphere(radius, slices, stacks),
        #glutSolidSphere(radius, slices, stacks)
        #glutSolidSphere(2,50,5)
        #glutWireSphere(2,20,20)

        #Cubos:
        #glutWireCube(size),
        #glutSolidCube(size)
        #glutWireCube(3),
        #glutSolidCube(3)

        # Conos:
        #glutWireCone(base, height, slices, stacks),
        #glutSolidCone(base, height, slices, stacks)
        #glutSolidCone(1, 3, 30, 50)
        #glutSolidCone(base, height, slices, stacks)

        # Octaedros:
        #glutWireOctahedron(),
        #glutSolidOctahedron()
        #glutWireOctahedron()

        # Tetraedros:
        #glutWireTetrahedron()
        #glutSolidTetrahedron()

        #Icosaedros:
        #glutWireIcosahedron()
        #glutSolidIcosahedron()
        #glutWireIcosahedron()

        # Teteras:
        #glutWireTeapot(parametro)
        #glutWireTeapot(1.0)
        #glutSolidTeapot(1.0)

        # Toroides:
        #glutSolidTorus (GLdouble innerRadius, GLdouble outerRadius, GLint nsides, GLint rings)
        #glutSolidCube(1)
        glColor3ub(137, 255, 133)
        glBegin(GL_QUADS)
        vx = [ 0.050, -0.050 ];
        vy = [ 0.000, 0.800 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        vx = [ 0.080, -0.020 ];
        vy = [ 0.100,  0.200 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        vx = [ 0.050, -0.050 ];
        vy = [ 0.250,  0.350 ];
        vz = [ 0.080, -0.020 ];
        self.Box(vx,vy,vz);
        vx = [ 0.020, -0.080 ];
        vy = [ 0.400,  0.500 ];
        vz = [ 0.050, -0.050 ];
        self.Box(vx,vy,vz);
        vx = [ 0.050, -0.050 ];
        vy = [ 0.600,  0.500 ];
        vz = [ 0.020, -0.080 ];
        self.Box(vx,vy,vz);
        glColor3ub(255, 120, 120)
        vx = [ 0.110,  -0.110 ];
        vy = [ 0.800,   1.000 ];
        vz = [ 0.050,   0.085 ];
        self.Box(vx,vy,vz);
        glEnd()
        glScalef(0,0,0)
        glutSwapBuffers()
        RotarEnY += 0.2 #Esta variable se usa para la rotacion

    def keyPressed(self,*args):
        # Permite estar rotando el objeto
        if args[0] == '\x1b':
            sys.exit()
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
                
    def main(self):
        global window
        global RotarEnY
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(0, 0)

        window = glutCreateWindow("Programa para crear varios objetos 3D")
        glutDisplayFunc(self.DibujarObjetos)
        glutIdleFunc(self.DibujarObjetos)
        glutKeyboardFunc(self.keyPressed)
        self.InitGL(800, 600)
        RotarEnY = 0.0
        glutMainLoop()

if __name__ == "__main__":
    x = Objetos()
