import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Създаване на DataFrame с данни за продажби (използваме данните от предишната задача)
np.random.seed(0)
data = {
    'продукт': ['A', 'B', 'C', 'D'] * 25,
    'цена': np.random.uniform(10, 100, 100).round(2),
    'количество': np.random.randint(1, 50, 100),
    'регион': np.random.choice(['Север', 'Юг', 'Изток', 'Запад'], 100)
}
df = pd.DataFrame(data)
df['приход'] = df['цена'] * df['количество']

# 1. Хистограма на цените
plt.figure(figsize=(10, 6))
plt.hist(df['цена'], bins=20, edgecolor='black')
plt.title('Разпределение на цените')
plt.xlabel('Цена')
plt.ylabel('Честота')
plt.savefig('price_distribution.png')
plt.close()

# 2. Scatter plot на цена спрямо количество
plt.figure(figsize=(10, 6))
plt.scatter(df['цена'], df['количество'], alpha=0.5)
plt.title('Цена спрямо Количество')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.savefig('price_vs_quantity.png')
plt.close()

# 3. Box plot на приходите по продукт
plt.figure(figsize=(10, 6))
sns.boxplot(x='продукт', y='приход', data=df)
plt.title('Разпределение на приходите по продукт')
plt.savefig('revenue_by_product.png')
plt.close()

# 4. Bar plot на средния приход по регион
avg_revenue_by_region = df.groupby('регион')['приход'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
avg_revenue_by_region.plot(kind='bar')
plt.title('Среден приход по регион')
plt.xlabel('Регион')
plt.ylabel('Среден приход')
plt.savefig('avg_revenue_by_region.png')
plt.close()

# 5. Heatmap на корелацията между числовите променливи
plt.figure(figsize=(8, 6))
sns.heatmap(df[['цена', 'количество', 'приход']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Корелация между променливите')
plt.savefig('correlation_heatmap.png')
plt.close()

print("Визуализациите са запазени като PNG файлове в текущата директория.")