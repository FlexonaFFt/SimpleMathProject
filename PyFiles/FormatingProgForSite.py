import math

# Основная функция для рассчёта условия задачи
def find_cylinder_with_min_surface_area_with_graph_solarized(num_cylinders):
    cylinders = []
    for i in range(num_cylinders):
        print(f"Введите данные для цилинда {i+1}:")
        radius = float(input("Радиус окружности: "))
        height = float(input("Высота окружности: "))
        expression = math.pi * (radius ** 2) * height
        surface_area = 2 * math.pi * radius * (radius + height)
        cylinders.append((radius, height, surface_area))
        min_surface_area_cylinder = min(cylinders, key=lambda x: x[2])
    print("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ")
    return min_surface_area_cylinder

# Обращение к этой функции
res = int(input("Введите количество цилиндров: "))
print(find_cylinder_with_min_surface_area_with_graph_solarized(res))