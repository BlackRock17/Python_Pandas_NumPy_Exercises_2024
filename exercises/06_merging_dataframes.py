import pandas as pd

# Създаване на първия DataFrame
df1 = pd.DataFrame({
    'служител_id': [1, 2, 3, 4, 5],
    'име': ['Иван', 'Мария', 'Петър', 'Ана', 'Георги'],
    'отдел': ['IT', 'HR', 'Финанси', 'Маркетинг', 'IT']
})

# Създаване на втория DataFrame
df2 = pd.DataFrame({
    'служител_id': [1, 2, 3, 4, 6],
    'заплата': [3500, 4200, 3800, 4000, 3900],
    'бонус': [500, 1000, 800, 900, 700]
})

print("DataFrame 1 (Информация за служители):")
print(df1)
print("\nDataFrame 2 (Заплати и бонуси):")
print(df2)

# Сливане на двата DataFrame-а
merged_df = pd.merge(df1, df2, on='служител_id', how='inner')
print("\nСлети данни (inner join):")
print(merged_df)

# Сливане с включване на всички служители от df1
left_merged_df = pd.merge(df1, df2, on='служител_id', how='left')
print("\nСлети данни (left join):")
print(left_merged_df)

# Сливане с включване на всички редове от двата DataFrame-а
outer_merged_df = pd.merge(df1, df2, on='служител_id', how='outer')
print("\nСлети данни (outer join):")
print(outer_merged_df)

# Добавяне на нов DataFrame с информация за отделите
df3 = pd.DataFrame({
    'отдел': ['IT', 'HR', 'Финанси', 'Маркетинг'],
    'ръководител': ['Петър', 'Мария', 'Стоян', 'Ана']
})

# Сливане на три DataFrame-а
final_df = pd.merge(merged_df, df3, on='отдел', how='left')
print("\nКраен резултат след сливане на три DataFrame-а:")
print(final_df)