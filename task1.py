from pulp import LpMaximize, LpProblem, LpVariable
import matplotlib.pyplot as plt

model = LpProblem(name="drink-production", sense=LpMaximize)

# Змінні: кількість лимонаду (x) та фруктового соку (y)
x = LpVariable(name="lemonade", lowBound=0, cat='Integer')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Обмеження
model += (2 * x + 1 * y <= 100, "Water")
model += (1 * x <= 50, "Sugar")
model += (1 * x <= 30, "Lemon_Juice")
model += (2 * y <= 40, "Fruit_Puree")

# Цільова функція: максимізувати загальну кількість продуктів
model += x + y


model.solve()

print(f"Лимонад: {x.value()}")
print(f"Фруктовий сік: {y.value()}")
print(f"Загальна кількість продуктів: {model.objective.value()}")


# Дані для графіка
labels = ['Лимонад', 'Фруктовий сік']
values = [x.value(), y.value()]

# Побудова графіка
plt.bar(labels, values)
plt.title('Виробництво напоїв')
plt.ylabel('Кількість одиниць')
plt.grid(axis='y')
plt.show()
