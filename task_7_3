import random
import asyncio
import time


array_num : list[int] = []
sum_numbers = 0

async def count_sum_numbers(num_list : list[int]):
    global sum_numbers
    sum_in_list = 0
    for num in num_list:
        sum_in_list += num
    sum_numbers += sum_in_list

async def main():
    global array_num
    tasks: list[asyncio.Task] = []

    for _ in range(1000):
        new_list = [random.randint(1, 100) for _ in range(1000)]
        task = asyncio.create_task(count_sum_numbers(new_list))
        array_num.extend(new_list)
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    start_time = time.time()
    print(array_num)
    print(f'Сумма всех чисел в массиве: {sum_numbers}')
    print(f'Время выполнения программы: {time.time() - start_time}')