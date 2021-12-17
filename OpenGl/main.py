import pygame
from OpenGL.raw.GLUT import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Вершины
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

# Ребра
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

# Цвета
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

# Поверхности
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

# Создание куба
def Cube():
    glBegin(GL_QUADS) # Четырехугольник
    for surface in surfaces:
        x = 0 # Счетчик
        for vertex in surface:
            x += 1
            glColor3fv(colors[x]) # Установка цвета
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES) # Отрисовка линий
    for edge in edges: # Идем по ребрам
        for vertex in edge:
            glVertex3fv(verticies[vertex]) # Отрисовка каждой линии
    glEnd()

def Sphere():


    sphere = gluNewQuadric()
    glColor3f(0.26, 0.05, 0)
    glPushMatrix()
    glTranslatef(0, 0, 0)
    gluSphere(sphere,1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 1, 0)
    gluSphere(sphere, 0.8, 50, 50)
    glPopMatrix()

    glColor3f(0.026, 0.011, 0)
    glPushMatrix()
    glTranslatef(-0.8, -0.8, 0)
    gluSphere(sphere, 0.3, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.8, -0.8, 0)
    gluSphere(sphere, 0.3, 50, 50)
    glPopMatrix()


    glPushMatrix()
    glTranslatef(-0.8, 0, 0)
    gluSphere(sphere, 0.3, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.8, 0, 0)
    gluSphere(sphere, 0.3, 50, 50)
    glPopMatrix()




def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # Говорим, что работаем с OpenGl
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) # Угол,соотношение сторон, ближняя, дальнюю плоскости отсече
    glTranslatef(0.0,0.0, -10) # Сдвигаемся на 5 единиц назад
    #glRotatef(90, 5, 0, 0)
    glMatrixMode(GL_PROJECTION)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    sphere = gluNewQuadric()  # Create new sphere

    # glMatrixMode(GL_PROJECTION)

    while True:
        # определяет возможность выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Делаем перемещения с помощью клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(-10, 0, 3, 0)

                if event.key == pygame.K_RIGHT:
                    glRotatef(10, 0, 3, 0)

                if event.key == pygame.K_UP:
                    glRotatef(-10, 3, 0, 0)

                if event.key == pygame.K_DOWN:
                    glRotatef(10, 3, 0, 0)


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.5)
                if event.button == 5:
                    glTranslatef(0, 0, -0.5)

        # init model view matrix
        glLoadIdentity()

        # init the view matrix
        glLoadIdentity()

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glMultMatrixf(viewMatrix)


        #glRotatef(1, 3, 1, 1) # угол вращения и координаты x, y, и z.


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # функция очистки
        # Cube()  # Отрисовка куба
        Sphere()


        # glColor4f(0.5, 0.2, 0.2, 1)
        # gluSphere(sphere, 1, 50, 50)


        pygame.display.flip() # обновляет наш экран
        pygame.time.wait(20) # Задержка


main()