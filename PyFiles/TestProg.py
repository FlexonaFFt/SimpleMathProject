import math

def find_cylinder_params(volume):
    cylinders = []
    radius = (volume / 2 * math.pi) ** (1/3)
    height = (100 / (math.pi * (radius ** 2)))
    if math.isclose(math.pi * radius**2 * height, volume, rel_tol=1e-9):
        cylinders.append((radius, height))
    return cylinders

volume = int(input("Введите объем цилиндра: "))
cylinders = find_cylinder_params(volume)
print("Радиусы и высоты цилиндров с объемом", volume, ":", cylinders)
print("Количество цилиндров:", len(cylinders))