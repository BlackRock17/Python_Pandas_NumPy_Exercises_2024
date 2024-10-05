import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Създаване на времеви ред за продажби
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales = np.random.randint(100, 1000, size=len(dates))
df = pd.DataFrame({'date': dates, 'sales': sales})
df.set_index('date', inplace=True)

print("Първите 5 реда от DataFrame:")
print(df.head())

# Ресемплиране на данните по месец
monthly_sales = df.resample('M').sum()
print("\nМесечни продажби:")
print(monthly_sales)

# Изчисляване на подвижна средна
df['moving_average'] = df['sales'].rolling(window=7).mean()
print("\nПърви 10 реда с подвижна средна:")
print(df.head(10))

# Намиране на най-добрия и най-лошия ден за продажби
best_day = df['sales'].idxmax()
worst_day = df['sales'].idxmin()
print(f"\nНай-добър ден за продажби: {best_day}, Продажби: {df['sales'][best_day]}")
print(f"Най-лош ден за продажби: {worst_day}, Продажби: {df['sales'][worst_day]}")

# Визуализация на данните
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['sales'], label='Дневни продажби')
plt.plot(df.index, df['moving_average'], label='7-дневна подвижна средна', color='red')
plt.title('Дневни продажби и подвижна средна')
plt.xlabel('Дата')
plt.ylabel('Продажби')
plt.legend()
plt.tight_layout()
plt.savefig('sales_plot.png')
plt.close()

print("\nГрафиката е запазена като 'sales_plot.png'")