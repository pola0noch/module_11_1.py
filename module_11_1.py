# Домашнее задание по теме "Обзор сторонних библиотек Python"

# requests
import requests

url = 'https://httpbin.org/post'
data = {'имя': 'Катя', 'возраст': 24}

r = requests.post(url, data=data)
print(r.status_code) # Печать кода статуса
print(r.headers) # Печать заголовков ответа
print(r.json()) # Печать тела ответа (в виде JSON)
print("-" * 20)


r = requests.put(url, data=data)
if r.status_code == 200:
    print("Пользователь успешно обновлен!")
else:
    print("Ошибка при обновлении пользователя:", r.status_code)
print("-" * 20)


r = requests.get('https://api.github.com/events')
print(r)
if r.status_code == 200:
    events = r.json()
    for event in events:
        print(f"Тип события: {event['type']}")
        print(f"Актер: {event['actor']['login']}")
        print("-" * 20)
else:
    print("Ошибка при получении данных:", r.status_code)


# pandas
import pandas as pd
import matplotlib.pyplot as plt

p = pd.DataFrame({'A': [1, 2, 3]})
print(p)
print("-" * 20)

data = pd.read_csv('example_1kb.csv') # Чтение данных из CSV-файла
print(data.head())
print("-" * 20)

filtered_data = data[data['name'] == "Alex Batz"] # Фильтрация данных по столбцу 'name'
print(filtered_data)
print("-" * 20)

data = pd.DataFrame({'год': [2020, 2021, 2022], 'продажи': [100, 120, 150]}) # Создание графика
data.plot(x="год", y="продажи")
print(data)
print("-" * 20)
plt.show() # Изображение графика

# numpy
import numpy as np

print("-" * 20)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr + 2) # Добавить 2 к каждому элементу
print(arr * 2)  # Умножить каждый элемент на 2
print(np.mean(arr))  # Рассчитать среднее значение
print(arr[1:3])  # Получить срез массива





