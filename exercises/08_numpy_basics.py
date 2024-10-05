import numpy as np

# Създаване на NumPy масиви
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("1D масив:")
print(arr1)
print("\n2D масив:")
print(arr2)

# Основни операции
print("\nСума на елементите в arr1:", np.sum(arr1))
print("Средна стойност на arr1:", np.mean(arr1))
print("Максимална стойност в arr2:", np.max(arr2))

# Преоразмеряване на масив
reshaped = arr1.reshape(5, 1)
print("\nПреоразмерен масив:")
print(reshaped)

# Индексиране и срязване
print("\nВтори ред на arr2:")
print(arr2[1])
print("\nПърва колона на arr2:")
print(arr2[:, 0])

# Математически операции
print("\narr1 на квадрат:")
print(np.square(arr1))
print("\nКвадратен корен на arr1:")
print(np.sqrt(arr1))

# Генериране на случайни числа
random_arr = np.random.rand(3, 3)
print("\nМасив със случайни числа:")
print(random_arr)

# Логически операции
print("\nЕлементи на arr1, по-големи от 3:")
print(arr1 > 3)

# Линейна алгебра
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\nУмножение на матрици:")
print(np.dot(a, b))