# 4) Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный 
# взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см#
# ж). ниже 166 см.

# Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.),
# а затем проверить себя с помощью встроенных функций.

from scipy import stats

mu = 174
sigma = 8

# а). больше 182 см
print('б). больше 182 см')
x = 182
z = (x - mu) / sigma
print(f'z = {z}')   # 1
# далее воспользуемся таблицей z
pRight182 = 0.1587
print(f'Вероятность больше 182 см = {round(pRight182 * 100, 2)}%')
print(f'Вероятность больше 182 см = {round((1 - stats.norm.cdf(x, mu, sigma)) * 100, 2)}%')

# б). больше 190 см
print('б). больше 190 см')
x = 190
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pRight190 = 0.0228
print(f'Вероятность больше 190 см = {round(pRight190 * 100, 2)}%')
print(f'Вероятность больше 190 см = {round((1 - stats.norm.cdf(x, mu, sigma)) * 100, 2)}%')

# в). от 166 см до 190 см
print('в). от 166 см до 190 см')
x = 166
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pRight166 = 0.8413
print(f'Вероятность от 166 см до 190 см = {round((pRight166 - pRight190) * 100, 2)}%')
print(f'Вероятность от 166 см до 190 см = {round(((1 - stats.norm.cdf(x, mu, sigma)) - pRight190) * 100, 2)}%')

# г). от 166 см до 182 см
print('г). от 166 см до 182 см')
print(f'Вероятность от 166 см до 182 см = {round((pRight166 - pRight182) * 100, 2)}%')
print(f'Вероятность от 166 см до 182 см = {round(((1 - stats.norm.cdf(x, mu, sigma)) - pRight182) * 100, 2)}%')

# д). от 158 см до 190 см
print('д). от 158 см до 190 см')
x = 158
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pRight158 = 0.9772
print(f'Вероятность от 158 см до 190 см = {round((pRight158 - pRight190) * 100, 2)}%')
print(f'Вероятность от 158 см до 190 см = {round(((1 - stats.norm.cdf(x, mu, sigma)) - pRight190) * 100, 2)}%')

# е). не выше 150 см или не ниже 190 см
print('е). не выше 150 см или не ниже 190 см')
x = 150
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pLeft150 = 0.00135
print(pRight190)
print(f'Вероятность не выше 150 см или не ниже 190 см = {round((pLeft150 + pRight190) * 100, 2)}%')
print(f'Вероятность не выше 150 см или не ниже 190 см = {round(((stats.norm.cdf(x, mu, sigma)) + pRight190) * 100, 2)}%')

# ё). не выше 150 см или не ниже 198 см#
print('ё). не выше 150 см или не ниже 198 см')
x = 198
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pLeft198 = 0.00135
print(f'Вероятность не выше 150 см или не ниже 198 см = {round((pLeft150 + pLeft198) * 100, 2)}%')
print(f'Вероятность не выше 150 см или не ниже 198 см = {round(((1 - stats.norm.cdf(x, mu, sigma)) + pLeft150) * 100, 2)}%')

# ж). ниже 166 см.
print('ж). ниже 166 см')
x = 166
z = (x - mu) / sigma
print(f'z = {z}')    # 1
# далее воспользуемся таблицей z
pLeft160 = 0.1587
print(f'Вероятность ниже 166 см = {round(pLeft160 * 100, 2)}%')
print(f'Вероятность ниже 166 см = {round((stats.norm.cdf(x, mu, sigma)) * 100, 2)}%')
