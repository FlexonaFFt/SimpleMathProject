# Импортирование библиотек и ресурсов
import matplotlib as mpl 
import matplotlib.pyplot as plt
import math

# Прописывание основных функций программы 
def find_cylinder_with_min_surface_area(num_cylinders):
    cylinders = []
    for i in range(num_cylinders):
        print(f"Введите данные для цилинда {i+1}:")
        radius = float(input("Радиус окружности: "))
        height = float(input("Высота окружности: "))
        expression = math.pi * (radius ** 2) * height
        # surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
        # cylinders.append((expression, surface_area))
        surface_area = 2 * math.pi * radius * (radius + height)
        cylinders.append((radius, height, surface_area))
    # min_surface_area_cylinder = min(cylinders, key=lambda x: x[1])
    min_surface_area_cylinder = min(cylinders, key=lambda x: x[2])
    print("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ")
    return min_surface_area_cylinder

def find_cylinder_with_min_surface_area_with_graph(num_cylinders):
    cylinders = []
    for i in range(num_cylinders):
        print(f"Введите данные для цилинда {i+1}:")
        radius = float(input("Радиус окружности: "))
        height = float(input("Высота окружности: "))
        expression = math.pi * (radius ** 2) * height
        surface_area = 2 * math.pi * radius * (radius + height)
        cylinders.append((radius, height, surface_area))

    # блок для создания графических массивов
    radii = [c[0] for c in cylinders]
    surface_areas = [c[2] for c in cylinders]
    # построение графика
    plt.figure(facecolor='#4d4847')
    plt.plot(radii, surface_areas, color='#fe5f00', label='График')
    plt.plot(radii[surface_areas.index(max(surface_areas))], max(surface_areas), 'o', color='#fe5f00')
    plt.xlabel("Радиус", color='white')
    plt.ylabel("Площадь поверхности", color='white')
    plt.title("Зависимость площади поверхности от радиуса", color='white')
    plt.tick_params(axis='both', colors='white')

    min_surface_area_cylinder = min(cylinders, key=lambda x: x[2])
    plt.show()
    print("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ")
    return min_surface_area_cylinder

def find_cylinder_with_min_surface_area_with_graph_solarized(num_cylinders):
    cylinders = []
    for i in range(num_cylinders):
        print(f"Введите данные для цилинда {i+1}:")
        radius = float(input("Радиус окружности: "))
        height = float(input("Высота окружности: "))
        expression = math.pi * (radius ** 2) * height
        surface_area = 2 * math.pi * radius * (radius + height)
        cylinders.append((radius, height, surface_area))

    # блок для создания графических массивов
    radii = [c[0] for c in cylinders]
    surface_areas = [c[2] for c in cylinders]
    # построение графика
    with plt.style.context('Solarize_Light2'):
        plt.plot(radii, surface_areas, label='График')
        plt.plot(radii[surface_areas.index(max(surface_areas))], max(surface_areas), 'o')
        plt.xlabel("Радиус")
        plt.ylabel("Площадь поверхности")
        plt.title("Зависимость площади поверхности от радиуса")
        plt.tick_params(axis='both')

        min_surface_area_cylinder = min(cylinders, key=lambda x: x[2])
        plt.show()
        print("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ")
        return min_surface_area_cylinder
    
def find_cylinder_with_min_surface_area_with_hizt_solarized(num_cylinders):
    cylinders = []
    for i in range(num_cylinders):
        print(f"Введите данные для цилинда {i+1}:")
        radius = float(input("Радиус окружности: "))
        height = float(input("Высота окружности: "))
        expression = math.pi * (radius ** 2) * height
        surface_area = 2 * math.pi * radius * (radius + height)
        cylinders.append((radius, height, surface_area))

    # блок для создания графических массивов
    radii = [c[0] for c in cylinders]
    surface_areas = [c[2] for c in cylinders]
    # построение графика
    with plt.style.context('Solarize_Light2'):

        plt.figure(facecolor='#5e503f')  # Цвет фона
        plt.hist(surface_areas, bins=10, density=True, alpha=0.75, color='#fe5f00')  # Создание гистограммы
        plt.xlabel("Площадь поверхности", color='white')  # Подпись оси X
        plt.ylabel("Частота", color='white')  # Подпись оси Y
        plt.title("Распределение площади поверхностей", color='white')  # Заголовок
        plt.tick_params(axis='both', colors='white')

        min_surface_area_cylinder = min(cylinders, key=lambda x: x[2])
        plt.axvline(x=min_surface_area_cylinder[2], color='r', linestyle='--', label='График')
        plt.legend()
        plt.show()
        print("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ")
        return min_surface_area_cylinder

# Прописываем вывод и ввод программы: 
print("╔══╗─╔═══╗╔═══╗╔══╗╔╗╔╗╔═══╗────╔╗──╔══╗ \n║╔╗║─║╔══╝║╔═╗║║╔═╝║║║║║╔═╗║───╔╝║──║╔╗║ \n║╚╝╚╗║╚══╗║╚═╝║║║──║║║║║╚═╝║───╚╗║──║║║║ \n║╔═╗║║╔══╝║╔══╝║║──║║╔║╚╗╔╗║────║║──║║║║ \n║╚═╝║║╚══╗║║───║╚═╗║╚╝║─║║║║────║║╔╗║╚╝║ \n╚═══╝╚═══╝╚╝───╚══╝╚══╝─╚╝╚╝────╚╝╚╝╚══╝" )
print("Решение без графика - 1")
print("Решение с графиком - 2")
print("Решение с графиком(solarized) - 3")
print("Решение с гистограммой(solarized) - 4")
function = int(input("Какой вариант решения задачи будем использовать? \n Введите: "))

if function == 1:
    res = int(input("Введите количество цилиндров: "))
    print(find_cylinder_with_min_surface_area(res))

if function == 2:
    res = int(input("Введите количество цилиндров: "))
    print(find_cylinder_with_min_surface_area_with_graph(res))

if function == 3:
    res = int(input("Введите количество цилиндров: "))
    print(find_cylinder_with_min_surface_area_with_graph_solarized(res))

if function == 4:
    res = int(input("Введите количество цилиндров: "))
    print(find_cylinder_with_min_surface_area_with_hizt_solarized(res))