import random
import multiprocessing
import time


def count_sum(num_list: list[int], sum_numbers: multiprocessing.Value):
    sum_in_list = 0
    
    for num in num_list:
        sum_in_list += num

    with sum_numbers.get_lock():
        sum_numbers.value += sum_in_list

def main():
    result_sum = multiprocessing.Value("i", 0)
    random_list = []
    processes: list[multiprocessing.Process] = []

    for _ in range(1000):
        new_list = [random.randint(1, 100) for _ in range(1000)]
        process  = multiprocessing.Process(target=count_sum, args=(new_list, result_sum))
        random_list.extend(new_list)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(random_list)

    return result_sum

if __name__ == "__main__":
    start_time = time.time()
    result_sum_numbers = main()
    with result_sum_numbers.get_lock():
        result_sum = result_sum_numbers.value

    print(f'Сумма всех чисел в массиве: {result_sum}')
    print(f'Время выполнения программы: {time.time() - start_time}')
