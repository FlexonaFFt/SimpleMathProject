import math

n = int(input("Введите число цилиндров: "))
V = 0
m = []
for V1 in range(1, n+1):
    V = float(input(f"Введите объем цилиндра {V1}: "))
    m.append(V)
for i in range(1, n+1):
    r = pow(m[i-1], 1/3)/pow(2*(math.pi), 1/3)
    h = m[i-1]/((math.pi)*r**2)
    s = 2*(math.pi)*r**2 + 2*(math.pi)*r*h
    print(f"Площадь поверхности цилиндра {i}: ", s)