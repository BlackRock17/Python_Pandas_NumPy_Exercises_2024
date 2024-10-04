import pandas as pd
import numpy as np

# Създаване на DataFrame с липсващи стойности
data = {
    'име': ['Иван', 'Мария', 'Петър', 'Ана', 'Георги'],
    'възраст': [28, 34, np.nan, 31, 27],
    'град': ['София', 'Пловдив', 'Варна', np.nan, 'Бургас'],
    'заплата': [3500, 4200, 3800, 4000, np.nan]
}

df = pd.DataFrame(data)

print("Оригинален DataFrame:")
print(df)

# Проверка за липсващи стойности
print("\nЛипсващи стойности:")
print(df.isnull().sum())

# Премахване на редове с липсващи стойности
df_dropped = df.dropna()
print("\nDataFrame след премахване на редове с липсващи стойности:")
print(df_dropped)

# Попълване на липсващи стойности
df_filled = df.fillna({
    'възраст': df['възраст'].mean(),
    'град': 'Неизвестен',
    'заплата': df['заплата'].median()
})

print("\nDataFrame след попълване на липсващи стойности:")
print(df_filled)

# Интерполация на числови стойности
df['заплата'] = df['заплата'].interpolate()
print("\nDataFrame след интерполация на заплатите:")
print(df)