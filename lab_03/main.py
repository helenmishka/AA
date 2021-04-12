import random
import string
from time import time
import tracemalloc


def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def SelectionSort(a):
    for i in range(len(a) - 1):
        m = i
        j = i + 1
        while j < len(a):
            if a[j] < a[m]:
                m = j
            j = j + 1
        a[i], a[m] = a[m], a[i]
    return a


def input_array():
    n = int(input("Введите длину массива: "))
    a = []
    for i in range(n):
        a.append(int(input("Введите " + str(i + 1) + " элемент: ")))
    return a


def print_array(a):
    print("Отсортированный массив:", end=' ')
    for i in range(len(a)):
        print(a[i], end=' ')


def build_array_random(n):
    a = []
    for i in range(n):
        a.append(random.randint(-10000, 10000))
    return a


def build_array_sort(n):
    a = []
    for i in range(n):
        a.append(i)
    return a


def build_array_full_unsort(n):
    a = []
    for i in range(n):
        a.append(i)
    a.reverse()
    return a


def measure_time(n, len_array, f):
    # overall_first_size = 0
    overall_first_peak = 0
    for i in range(n):
        a = build_array_sort(len_array)
        tracemalloc.start(25)
        tracemalloc.clear_traces()
        f(a)
        overall_first_size_i, overall_first_peak_i = tracemalloc.get_traced_memory()
        # overall_first_size += overall_first_size_i
        overall_first_peak += overall_first_peak_i

    print("\nPeak: " + str(round(overall_first_peak / n)))

    overall_time = 0.0
    for i in range(n):
        a = build_array_sort(len_array)
        start = time()
        f(a)
        end = time()
        overall_time = end - start

    return overall_time / n


def menu():
    flag = True
    while flag:
        do = int(input("\nВыберите один из пунктов меню:\n"
                       "1 - сортировка выбором\n"
                       "2 - сортировка вставками\n"
                       "3 - сортировка пузырьком\n"
                       "4 - применение всех алгоритмов\n"
                       "5 - замеры времени\n"
                       "6 - завершение программы\n"
                       "выбор: "))
        if do == 1:
            a = input_array()
            print_array(SelectionSort(a))
        if do == 2:
            a = input_array()
            print_array(insertSort(a))
        if do == 3:
            a = input_array()
            print_array(bubbleSort(a))
        if do == 4:
            n = int(input("Введите длину массива: "))
            a = []
            for i in range(n):
                a.append(int(input("Введите" + str(i + 1) + "элемент: ")))
            b = a
            c = a
            SelectionSort(a)
            insertSort(b)
            bubbleSort(c)
        if do == 5:
            n = 100
            len_array = 500
            for i in range(100, len_array + 1, 100):
                print("\nдлина массива: " + str(i))

                time = measure_time(n, i, SelectionSort)
                print("сортировка выбором\nвремя = {:.10f}".format(time))

                time = measure_time(n, i, insertSort)
                print("сортировка вставками\nвремя = {:.10f}".format(time))

                time = measure_time(n, i, bubbleSort)
                print("сортировка пузырьком\nвремя = {:.10f}".format(
                    time))
        else:
            flag = False


if __name__ == "__main__":
    menu()
