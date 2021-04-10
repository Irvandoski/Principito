from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes
import Objetos
import Escenarios
import threading
import time
glutInit(sys.argv);

glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(640, 480)
glutInitWindowPosition(0, 0)


glMatrixMode(GL_PROJECTION);
glLoadIdentity();
glOrtho(0.0,512.0,384.0,0.0,0.0,10.0);
glEnable(GL_TEXTURE_2D);
glutSetCursor(GLUT_CURSOR_NONE);

glutDisplayFunc(drawscreen);
glutKeyboardFunc(inputevent);
glutSpecialFunc(sinputevent);
glClearColor(0.027, 0.823, 0.835, 0.0)
FocusCamera(0);
load_gl_textures();
glutMainLoop()
