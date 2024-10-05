import pandas as pd
import numpy as np
from scipy import stats

# Създаване на DataFrame с данни за продажби
np.random.seed(0)
data = {
    'продукт': ['A', 'B', 'C', 'D'] * 25,
    'цена': np.random.uniform(10, 100, 100).round(2),
    'количество': np.random.randint(1, 50, 100),
    'регион': np.random.choice(['Север', 'Юг', 'Изток', 'Запад'], 100)
}
df = pd.DataFrame(data)
df['приход'] = df['цена'] * df['количество']

print("Първите 5 реда от DataFrame:")
print(df.head())

# Описателни статистики
print("\nОписателни статистики:")
print(df.describe())

# Групиране по продукт
print("\nСредна цена и общ приход по продукт:")
print(df.groupby('продукт').agg({'цена': 'mean', 'приход': 'sum'}))

# Корелация между цена и количество
correlation = df['цена'].corr(df['количество'])
print(f"\nКорелация между цена и количество: {correlation:.2f}")

# Т-тест за сравняване на приходите между два региона
north_revenue = df[df['регион'] == 'Север']['приход']
south_revenue = df[df['регион'] == 'Юг']['приход']
t_stat, p_value = stats.ttest_ind(north_revenue, south_revenue)
print(f"\nТ-тест за приходите между Север и Юг:")
print(f"t-статистика: {t_stat:.2f}")
print(f"p-стойност: {p_value:.4f}")

# Честотно разпределение на продуктите
product_counts = df['продукт'].value_counts()
print("\nЧестотно разпределение на продуктите:")
print(product_counts)

# Процентно разпределение на продажбите по региони
region_sales_percent = df.groupby('регион')['приход'].sum() / df['приход'].sum() * 100
print("\nПроцентно разпределение на продажбите по региони:")
print(region_sales_percent)