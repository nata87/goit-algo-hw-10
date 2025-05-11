
import numpy as np
import scipy.integrate as spi

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2

# Monte Carlo метод
N = 100000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

# Точне значення через quad
quad_result, error = spi.quad(f, a, b)

print("Monte Carlo:", monte_carlo_result)
print("quad:", quad_result)
print("Абсолютна похибка:", abs(monte_carlo_result - quad_result))
