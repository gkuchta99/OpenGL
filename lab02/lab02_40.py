#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from random import randint

up_left_corner = list()
down_left_corner = list()
up_right_corner = list()
down_right_corner = list()


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def gen_deform(x, y, a, b, d):
    if randint(0, 100) % 2 == 0:
        up_left_corner.append(x - randint(0, b) * d / 100)
    else:
        up_left_corner.append(x + randint(0, b) * d / 100)
    if randint(0, 100) % 2 == 0:
        up_left_corner.append(y + a - randint(0, a) * d / 100)
    else:
        up_left_corner.append(y + a + randint(0, a) * d / 100)
    if randint(0, 100) % 2 == 0:
        down_left_corner.append(x - randint(0, b) * d / 100)
    else:
        down_left_corner.append(x + randint(0, b) * d / 100)
    if randint(0, 100) % 2 == 0:
        down_left_corner.append(y - randint(0, a) * d / 100)
    else:
        down_left_corner.append(y + randint(0, a) * d / 100)
    if randint(0, 100) % 2 == 0:
        up_right_corner.append(x + b - randint(0, b) * d / 100)
    else:
        up_right_corner.append(x + b + randint(0, b) * d / 100)
    if randint(0, 100) % 2 == 0:
        up_right_corner.append(y + a - randint(0, a) * d / 100)
    else:
        up_right_corner.append(y + a + randint(0, a) * d / 100)
    if randint(0, 100) % 2 == 0:
        down_right_corner.append(x + b - randint(0, b) * d / 100)
    else:
        down_right_corner.append(x + b + randint(0, b) * d / 100)
    if randint(0, 100) % 2 == 0:
        down_right_corner.append(y - randint(0, a) * d / 100)
    else:
        down_right_corner.append(y + randint(0, a) * d / 100)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(down_left_corner[0], down_left_corner[1])
    glVertex2f(up_left_corner[0], up_left_corner[1])
    glVertex2f(down_right_corner[0], down_right_corner[1])
    glEnd()

    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(up_left_corner[0], up_left_corner[1])
    glVertex2f(up_right_corner[0], up_right_corner[1])
    glVertex2f(down_right_corner[0], down_right_corner[1])
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, 'lab02-4.0', None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    gen_deform(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
