#!/usr/bin/env python3
import math
import random
import sys
from math import pow, sin, pi

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

N = 10
points = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
u_values_list = list()
v_values_list = list()
vertex_color_first = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
vertex_color_second = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]


def count_x(u, v):
    return (-90 * pow(u, 5)
            + 225 * pow(u, 4)
            - 270 * pow(u, 3)
            + 180 * pow(u, 2)
            - 45 * u) * math.cos(pi * v)


def count_y(u):
    return 160 * pow(u, 4) \
           - 320 * pow(u, 3) \
           + 160 * pow(u, 2)


def count_z(u, v):
    return (-90 * pow(u, 5)
            + 225 * pow(u, 4)
            - 270 * pow(u, 3)
            + 180 * pow(u, 2)
            - 45 * u) * sin(pi * v)


def init_u_v_lists(N):
    for i in range(N):
        v_values_list.append(i / (N - 1))
        u_values_list.append(i / (N - 1))


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def gen_points():
    for i in range(N):
        for j in range(N):
            u = u_values_list[i]
            v = v_values_list[j]
            points[i][j][0] = count_x(u, v)  # x
            points[i][j][1] = count_y(u)  # y
            points[i][j][2] = count_z(u, v)  # z
            vertex_color_first[i][j][0] = random.random()
            vertex_color_first[i][j][1] = random.random()
            vertex_color_first[i][j][2] = random.random()
            vertex_color_second[i][j][0] = random.random()
            vertex_color_second[i][j][1] = random.random()
            vertex_color_second[i][j][2] = random.random()


def draw_points():
    for x in range(N - 1):
        for y in range(N - 1):
            glBegin(GL_TRIANGLES)
            glColor3f(vertex_color_first[x][y][0], vertex_color_first[x][y][1], vertex_color_first[x][y][2])
            glVertex3f(points[x][y][0], points[x][y][1], points[x][y][2])
            glVertex3f(points[x + 1][y][0], points[x + 1][y][1], points[x + 1][y][2])
            glVertex3f(points[x][y + 1][0], points[x][y + 1][1], points[x][y + 1][2])
            glEnd()
            glBegin(GL_TRIANGLES)
            glColor3f(vertex_color_second[x][y][0], vertex_color_second[x][y][1], vertex_color_second[x][y][2])
            glVertex3f(points[x][y + 1][0], points[x][y + 1][1], points[x][y + 1][2])
            glVertex3f(points[x + 1][y][0], points[x + 1][y][1], points[x + 1][y][2])
            glVertex3f(points[x + 1][y + 1][0], points[x + 1][y + 1][1], points[x + 1][y + 1][2])
            glEnd()



    glFlush()


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / math.pi)

    axes()
    draw_points()
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    init_u_v_lists(N)
    gen_points()
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
