import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# print("\n1. Чтение CSV-файла и печать первых 5 строк.")
df = pd.read_csv('diamonds.csv')
# print(df.head())

print("\n2. Выбор столбцов и печать первых 6 строк.")
columns = ['carat', 'cut', 'x', 'y', 'z']
print(df[columns].head(6))

print("\n3. Выбрать Series и вывести.")
print(df['cut'])

# print("\n4. Создание новой серии «Качество - Цвет»")
# df['Quality-Color'] = df.cut + ', ' + df.color
# print(df.head())
#
# print("\n5. Найти количество строк, столбцов и тип данных для каждого столбца алмазов.")
# print(f"Строк = {df.shape[0]}\nСтолбцов = {df.shape[1]}")
# print(f"Тип данных:\n{df.dtypes}")
#
# print("\n6. Суммированиe только столбцов типа данных «объект».")
# print(df.describe(include=object))
#
# print("\n7. Переименование двух столбцов.")
# df.rename(columns={'price': 'usd', 'cut':'quality'}, inplace=True)
# print(df.head())
#
# print("\n8. Переименовать все столбцы.")
# new_columns_name = ['CARAT', 'CUT', 'COLOR', 'CLARITY', 'DEPTH', 'TABLE', 'USD', 'X', 'Y', 'Z']
# df.columns = new_columns_name
# print(df.head())
#
# print("\n9. Удаления второго столбца.")
# df.pop('carat')
# print(df.head())
#
# print("\n10. Одновременное удаление нескольких столбцов из блока данных.")
# df.drop(['carat', 'cut'], axis=1, inplace=True)
# print(df.head())
#
# print("\n11. Одновременное удаление нескольких строк.")
# df.drop([0, 1, 2, 3, 4, 5], axis=0, inplace=True)
# print(df.head())
#
# # # # # СОРТИРОВКА
#
# print("\n12. Сортировка столбца по возрастанию.")
# print(df.cut.sort_values(ascending=True))
#
print("\n13. Сортировка столбца по убыванию.")
print(df.price.sort_values(ascending=False))

print("\n14. Сортировка столбца 'Карат' по возрастанию и убыванию.")
print(df.sort_values('carat'))
print(df.sort_values('carat', ascending=False))
#
# print("\n15. Фильтрация (True/False) строк, вес в каратах не менее 0,3.")
# print(df['carat'] >= 0.3)
#
# print("\n16. Преобразование списка list() у Pandas Series.")
# lst = [1, 2, 3, 4, 5]
# result = pd.Series(lst)
#
# # # # # ПОИСК
#
print("\n17. Найти бриллианты, где длина > 5, ширина > 5 и глубина > 5.")
res = df[(df['x'] > 5) & (df['y'] > 5) & (df['z'] > 5)]
print(res)
#
# print("\n18. Найти бриллианты премиум-класса или идеальные.")
# res = df[(df['cut'] == "Premium") | (df['cut'] == "Ideal")]
# print(res)
#
# print("\n19. Найти бриллианты c оценкой Fair, Good или Premium.")
# res = df[(df['cut'] == "Premium") | (df['cut'] == "Good") | (df['cut'] == "Fair")]
# print(res)
#
# 20.
# print(df.columns)
#
# 21.
# res = pd.read_csv('diamonds.csv', nrows=3)
# print(res)
#
# 22.
# for index, row in df.iterrows():
#     print(index, row.carat, row.cut, row.color, row.price)
#
# 23.
# print(df.select_dtypes(exclude=object))
#
# 24.
# print(df.select_dtypes(include=[np.number]).dtypes)
# print(df.select_dtypes(include=[np.number]))
#
# 25.
# print(df.describe(include=['object', 'float64']))
#
# 26. 27. 28. 29.
# print(df.mean(numeric_only=True))  # Среднее столбцов
# print(df.mean(axis=1, numeric_only=True))  # Среднее каждой строки
# print(df.groupby('cut').price.mean())  # Средняя цена для каждого вида огранки
# print(df.groupby('cut').price.agg(['count', 'min', 'max']))
#
# 30.
# df.drop(['carat'], axis=1, inplace=True)
# df.groupby('cut').mean(numeric_only=True).plot(kind='bar')
# plt.show()
#
# 31. 32. 33. 34.
# print(df.cut.value_counts())
# print(df['cut'].value_counts())
# print(df['cut'].value_counts(normalize=True))
# print(df['cut'].unique())
# print(df['cut'].nunique())
#
# 35.
print(pd.crosstab(df['cut'], df['price']))
#
# 36. 37. 38. 39.
# print(df['carat'].describe())
# df['carat'].plot(kind='hist')
# plt.show()
# df['cut'].value_counts().plot(kind='bar')
# plt.show()
# print(df.isnull().head(30))
#
# 40.
# print(df.isnull().sum())
#
# 41.
# print(df.shape)
# print(df.dropna(how='any').shape)  # Удаление строк с отсутствующими значениями
#
# 42.
# print(df.dropna(subset=['carat', 'cut'], how='any').shape)
# print(df.dropna(subset=['carat', 'cut'], how='all').shape)
#
# 43. 44.
# df.set_index('color', inplace=True)
# print(df.head(20))
# df.index.name = 'color'
# df.reset_index(inplace=True)
# print(df.head(20))
#
# 45.
# print(df['carat'].value_counts().index)
# print(df['carat'].value_counts().values)
#
# 46. Сортировка
# print(df['cut'].value_counts().sort_values())
# print(df['cut'].value_counts().sort_index())
# 47.
# print((df.x * df.y * df.z).head(20))
# 48.
# print(pd.concat([df, df['color']], axis=1).head(20))
# 49. 50. 51. 52. 53. 54.
# print(df.loc[0, :])
# print(df.loc[[0, 1, 2], :])
# print(df.loc[2:5, :])
# print(df.loc[0:2, ['color', 'price']])
# print(df.loc[0:2, 'color':'price'])
# print(df.loc[df['cut'] == 'Premium', 'color'])
# 55. 56. 57. 58.
# print(df.iloc[[0, 2], [1, 4]])
# print(df.iloc[0:4, 1:4])
# print(df.iloc[0:4, :])
# print(df.iloc[2:5, 1:3])
# 59.
# print(df.info())
# 60. 61.
# print(df.info(memory_usage='deep'))
# print(df.memory_usage(deep=True))  # bits
# 62.
# print(df.sample(n=3))
# 63.
# res = df.sample(frac=0.75, random_state=99)
# print(res)
# print(df.loc[~df.index.isin(res.index), :])
# 64.
# print(df.clarity.duplicated().sum())
# 65.
# print(df.duplicated().sum())
