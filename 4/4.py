import numpy as np
from scipy.optimize import minimize

# Дані
m = np.array([0.60, 0.50, 0.40, 0.70])  # Сподівані норми прибутку
sigma = np.array([0.40, 0.30, 0.25, 0.50])  # Ризики (середньоквадратичні відхилення)
rho = np.array([[1, 0.2, -0.3, 0.9],   # Кореляційна матриця
                [0.2, 1, 0.5, 0.7],
                [-0.3, 0.5, 1, -0.3],
                [0.9, 0.7, -0.3, 1]])

# Коваріаційна матриця
cov_matrix = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        cov_matrix[i, j] = sigma[i] * sigma[j] * rho[i, j]

# Функція для обчислення ризику портфеля
def portfolio_risk(x, cov_matrix):
    return np.sqrt(np.dot(x.T, np.dot(cov_matrix, x)))

# Умова рівності суми ваг до 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Обмеження для ваг (ваги повинні бути в межах від 0 до 1)
bounds = tuple((0, 1) for _ in range(4))

# Початкові припущення для ваг
x0 = np.array([0.25, 0.25, 0.25, 0.25])

# Мінімізація ризику
result = minimize(portfolio_risk, x0, args=(cov_matrix,), method='SLSQP', bounds=bounds, constraints=constraints)

# Оптимальні ваги
optimal_weights = result.x

# Обчислення сподіваної норми прибутку для мінімального ризику
m_p_min_risk = np.dot(optimal_weights, m)

# Обчислення мінімального ризику
sigma_p_min_risk = portfolio_risk(optimal_weights, cov_matrix)

print(optimal_weights, m_p_min_risk, sigma_p_min_risk)
