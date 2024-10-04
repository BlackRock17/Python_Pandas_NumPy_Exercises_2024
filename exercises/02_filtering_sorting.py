import pandas as pd

# Четене на данни от CSV файл
df = pd.read_csv('../data/employees.csv')

# Филтриране на данни
print("Служители от София:")
sofia_employees = df[df['град'] == 'София']
print(sofia_employees)

# Сортиране на данни
print("\nСлужители сортирани по заплата (низходящ ред):")
sorted_by_salary = df.sort_values('заплата', ascending=False)
print(sorted_by_salary)

# Филтриране и сортиране
print("\nСлужители под 30 години, сортирани по заплата:")
young_sorted = df[df['възраст'] < 30].sort_values('заплата', ascending=False)
print(young_sorted)