# coding: utf-8
# license: GPLv3
import math
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        r = max(r, body.R)
        force = gravitational_constant * obj.m * space_objects.m / r**2
        alpha = math.atan((body.x - space_objects.x) / (body.y - space_objects.y))
        body.Fx += force * math.sin(alpha)
        body.Fy += force * math.cos(alpha)
    return body.Fx, body.Fy
        # FIXME: обработка аномалий при прохождении одного тела сквозь другое
        #pass  # FIXME: Взаимодействие объектов

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    old = body.x  # FIXME: Вывести формулы для ускорения, скоростей и координат
    body.Vy += ay * dt
    body.Vx += ay * dt
    body.ax += body.Fx/body.m
    body.ay += body.Fy / body.m
    body.x += body.Vx * dt + ax * dt ** 2 / 2
    body.y += body.Vy * dt + ay * dt ** 2 / 2


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
