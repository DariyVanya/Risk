# Матриця прибутків для різних варіантів рішень (x1, x2, x3) і станів попиту (θ1, θ2, θ3)
profits = [
    [6.0, 3.5, 5.0],  # Прибутки для x1
    [6.5, 7.0, 4.0],  # Прибутки для x2
    [3.5, 3.5, 8.5]   # Прибутки для x3
]

# Критерій Вальда: обчислюємо мінімальні значення для кожного варіанту рішення
min_profits = [min(row) for row in profits]
wald_solution_index = min_profits.index(max(min_profits))
wald_solution_value = max(min_profits)

print("Оптимальне рішення за критерієм Вальда: x" + str(wald_solution_index + 1))
print("Максимальний мінімальний прибуток:", wald_solution_value)

# Критерій Севіджа: обчислення матриці ризиків (втрат)
# Знаходимо максимальний прибуток для кожного стану попиту
max_profits_per_state = [max(column) for column in zip(*profits)]

# Обчислюємо матрицю ризиків (втрат) як різницю між максимальним прибутком у стані і реальним прибутком
risks = [[max_profits_per_state[j] - profits[i][j] for j in range(len(profits[0]))] for i in range(len(profits))]

# Для кожного варіанту рішення знаходимо максимальну втрату
max_risks = [max(row) for row in risks]
savage_solution_index = max_risks.index(min(max_risks))
savage_solution_value = min(max_risks)

print("Оптимальне рішення за критерієм Севіджа: x" + str(savage_solution_index + 1))
print("Мінімальна максимальна втрата:", savage_solution_value)
