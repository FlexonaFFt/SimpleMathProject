import math

V1 = float(input("Введите объем цилиндра: "))
r = pow(V1, 1/3)/pow(2*(math.pi), 1/3)
h = V1/((math.pi)*r**2)
s = 2*(math.pi)*r**2 + 2*(math.pi)*r*h
print(f"Площадь поверхности цилиндра: {s}")