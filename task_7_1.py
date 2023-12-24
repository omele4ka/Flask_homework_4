# Задание №7
# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения
# вычислений.

import random 
import threading
import time


sum_numbers = 0
def count_sum(num_list: list[int]):
    global sum_numbers
    sum_in_list = 0
    for num in num_list:
        sum_in_list += num
    sum_numbers += sum_in_list

random_list = []
threads : list[threading.Thread] = []
start_time = time.time()

for _ in range(1000):
    new_list = [random.randint(1, 100) for _ in range(1000)]
    thread = threading.Thread(target=count_sum, args=[new_list])
    random_list.extend(new_list)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(random_list)
print(f'Сумма всех чисел в массиве: {sum_numbers}')
print(f'Время выполнения программы: {time.time() - start_time}')