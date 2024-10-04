import pandas as pd
import numpy as np

# Създаване на прост DataFrame
data = {
    'име': ['Иван', 'Мария', 'Петър', 'Ана'],
    'възраст': [28, 34, 29, 31],
    'град': ['София', 'Пловдив', 'Варна', 'София']
}

df = pd.DataFrame(data)

print("Прост DataFrame:")
print(df)
print("\nИнформация за DataFrame:")
print(df.info())
print("\nПървите няколко реда:")
print(df.head())
print("\nОсновни статистики:")
print(df.describe())

# Четене на данни от CSV файл
df_from_csv = pd.read_csv('../data/employees.csv')

print("\nДанни от CSV файл:")
print(df_from_csv)
print("\nИнформация за DataFrame от CSV:")
print(df_from_csv.info())
print("\nОсновни статистики за DataFrame от CSV:")
print(df_from_csv.describe())