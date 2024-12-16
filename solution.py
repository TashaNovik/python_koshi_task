def f(x, y):
    return 2 * x

x0 = 0
y0 = 1
xf = 1
h = 0.001  # Выбираем шаг h = 0.001 для большей точности. Можно уменьшить для еще большей точности
n = int((xf - x0) / h)

x = x0
y = y0

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h

print(f"y(1) ≈ {y}")




# Analytically:
# Интегрируя y' = 2x,
# получаем y = x² + C.
# Из начального условия y(0) = 1 следует, что C = 1.
# Таким образом, аналитическое решение: y = x² + 1.
# Тогда y(1) = 1² + 1 = 2, что совпадает с заданным значением.