# coding: utf-8
# license: GPLv3

from source_code.solar_objects import Star, Planet
from source_code.solar_vis import DrawableObject
import numpy as np

def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселаx> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R = float(line[1])
    star.color = line[2]
    star.m = float(line[3])
    star.x = float(line[4])
    star.y = float(line[5])
    star.vx = float(line[6])
    star.vy = float(line[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = float(line[1])
    planet.color = line[2]
    planet.m = float(line[3])
    planet.x = float(line[4])
    planet.y = float(line[5])
    planet.vx = float(line[6])
    planet.vy = float(line[7])

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            line = line.split()
            object_type = line[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")
    return [DrawableObject(obj) for obj in objects]


def write_space_objects_vx_to_file(output_filename, space_objects):
    """Сохраняет Скорость x о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        s = ''
        for obj in space_objects:
            s += str(obj.vx)
            s += ' '
        out_file.write(s)
        if len(s.strip()) != 0:
            out_file.write('\n')
        out_file.close()

def write_space_objects_vy_to_file(output_filename, space_objects):
    """Сохраняет Скорость y о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        s = ''
        for obj in space_objects:
            s += str(obj.vy)
            s += ' '
        out_file.write(s)
        if len(s.strip()) != 0:
            out_file.write('\n')
        out_file.close()

def write_space_objects_x_to_file(output_filename, space_objects):
    """Сохраняет x о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        s = ''
        for obj in space_objects:
            s += str(obj.x)
            s += ' '
        out_file.write(s)
        if len(s.strip()) != 0:
            out_file.write('\n')
        out_file.close()

def write_space_objects_y_to_file(output_filename, space_objects):
    """Сохраняет y о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        s = ''
        for obj in space_objects:
            s += str(obj.y)
            s += ' '
        out_file.write(s)
        if len(s.strip()) != 0:
            out_file.write('\n')
        out_file.close()


def all_writer(space_objects):
    write_space_objects_vx_to_file('Data/vx.txt', space_objects)
    write_space_objects_vy_to_file('Data/vy.txt', space_objects)
    write_space_objects_x_to_file('Data/x.txt', space_objects)
    write_space_objects_y_to_file('Data/y.txt', space_objects)


def clear_a_file():
    '''

    :return: cleares all files in directory named Data
    '''
    with open('Data/vx.txt', 'w') as file:
        file.close()
    with open('Data/vy.txt', 'w') as file:
        file.close()
    with open('Data/x.txt', 'w') as file:
        file.close()
    with open('Data/y.txt', 'w') as file:
        file.close()






if __name__ == "__main__":
    print("This module is not for direct call!")
