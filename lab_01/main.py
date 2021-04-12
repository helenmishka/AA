import random
import string
from time import time
import tracemalloc

def Levenstein(f_str, s_str):
    len_f_str = len(f_str)
    len_s_str = len(s_str)
    F = [[(i + j) if i * j == 0 else 0 for j in range(len_s_str + 1)]
         for i in range(len_f_str + 1)]

    for i in range(1, len_f_str + 1):
        for j in range(1, len_s_str + 1):
            cost = 0

            if f_str[i - 1] != s_str[j - 1]:
                cost = 1

            F[i][j] = min(F[i - 1][j] + 1, F[i][j - 1] + 1, F[i - 1][j - 1] + cost)

    print_matrix(F, f_str, s_str)

    result = F[len_f_str][len_s_str]

    return result


def Levenstein_recursion(f_str, s_str):
    if f_str == '' or s_str == '':
        result = len(f_str) + len(s_str)
        return result

    substitution_cost = 0

    if f_str[-1] != s_str[-1]:
        substitution_cost = 1

    deletion = Levenstein_recursion(f_str[:-1], s_str) + 1
    insertion = Levenstein_recursion(f_str, s_str[:-1]) + 1
    substitution = Levenstein_recursion(f_str[:-1], s_str[:-1]) + substitution_cost

    result = min(deletion, insertion, substitution)
    return result


def Damerau_Levenshtein(f_str, s_str):
    F = [[0] * 100] * 100
    len_f_str = len(f_str)
    len_s_str = len(s_str)

    for i in range(len_f_str + 1):
         for j in range(len_s_str + 1):
              if i * j == 0:
                    F[i][j] = i+j
              else:
                    F[i][j] = 0

    for i in range(1, len_f_str + 1):
        for j in range(1, len_s_str + 1):
            cost = 0
            print(i,j)

            if f_str[i - 1] != s_str[j - 1]:
                print("+")
                cost = 1

            F[i][j] = min(F[i - 1][j] + 1, F[i][j - 1] + 1, F[i - 1][j - 1] + cost)

            if i > 1 and j > 1 and f_str[i - 1] == s_str[j - 2] and f_str[i - 2] == s_str[j - 1]:
                F[i][j] = min(F[i][j], F[i - 2][j - 2] + 1)
                print("-")
   

    #print_matrix(F, f_str, s_str)
    result = F[len_f_str][len_s_str]
    return result


def Damerau_Levenshtein_recursion(f_str, s_str):
    if f_str == '' or s_str == '':
        result = len(f_str) + len(s_str)
        return result

    substitution_cost = 0

    if f_str[-1] != s_str[-1]:
        substitution_cost = 1

    deletion = Damerau_Levenshtein_recursion(f_str[:-1], s_str) + 1
    insertion = Damerau_Levenshtein_recursion(f_str, s_str[:-1]) + 1
    substitution = Damerau_Levenshtein_recursion(f_str[:-1], s_str[:-1]) + substitution_cost

    result = min(deletion, insertion, substitution)

    if len(f_str) > 1 and len(s_str) > 1 and f_str[-1] == s_str[-2] and f_str[-2] == s_str[-1]:
        result = min(result, Damerau_Levenshtein_recursion(f_str[:-2], s_str[:-2]) + 1)

    return result


def input_strings_start(F):
    f_str = input("Введите первую строку: ")
    s_str = input("Введите вторую строку: ")
    return F(f_str, s_str)

def print_matrix(matr, f_str, s_str):
    print("\n   ", end=" ")
    for i in s_str:
        print(i, end=' ')
    for i in range(len(matr)):
        if i != 0:
            print("\n" + f_str[i - 1], end=" ")
        else:
            print("\n ", end=" ")
        for j in range(len(matr[i])):
            print(matr[i][j], end=' ')
    print("\n")

def output(result, i):
    if i == 1:
        print("\nалгоритм поиска расстояния Левенштейна с заполнением матрицы, ответ - ", result)
    if i == 2:
        print("рекурсивный алгоритм поиска расстояния Левенштейна, ответ - ", result)
    if i == 3:
        print("алгоритм поиска расстояния Дамерау-Левенштейна с заполнением матрицы, ответ - ", result)
    if i == 4:
        print("рекурсивный алгоритм поиска расстояния Дамерау-Левенштейна, ответ - ", result)

def build_string(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def measure_time(n, len_word, F):
    start = time()
    for i in range(n):
        str1 = build_string(len_word)
        str2 = build_string(len_word)
        tracemalloc.start(25)
        tracemalloc.clear_traces()
        F(str1, str2)
        print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    end = time()
    return (end - start) / n


def menu():
    flag = True
    while(flag):
        do = int(input("\nВыберите один из пунктов меню:\n"
                   "1 - алгоритм поиска расстояния Левенштейна с заполнением матрицы\n"
                   "2 - рекурсивный алгоритм поиска расстояния Левенштейна\n"
                   "3 - алгоритм поиска расстояния Дамерау-Левенштейна с заполнением матрицы\n"
                   "4 - рекурсивный алгоритм поиска расстояния Дамерау-Левенштейна\n"
                   "5 - применение всех алгоритмов\n"
                   "6 - замеры времени\n"
                   "7 - завершение программы\n"
                   "выбор: "))
        if do == 1:
            output(input_strings_start(Levenstein), 1)
        if do == 2:
            output(input_strings_start(Levenstein_recursion), 2)
        if do == 3:
            output(input_strings_start(Damerau_Levenshtein), 3)
        if do == 4:
            output(input_strings_start(Damerau_Levenshtein_recursion), 4)
        if do == 5:
            f_str = input("Введите первую строку: ")
            s_str = input("Введите вторую строку: ")
            output(Levenstein_recursion(f_str, s_str), 1)
            output(Levenstein(f_str, s_str), 2)
            output(Damerau_Levenshtein(f_str, s_str), 3)
            output(Damerau_Levenshtein_recursion(f_str, s_str), 4)
        if do == 6:
            n = 1
            len_word = 7
            for i in range(1, len_word + 1):
                print("\nдлина слова: " + str(i) + "\n")
                time = measure_time(n, i, Levenstein)
                print("алгоритм поиска расстояния Левенштейна с заполнением матрицы\n время = {:.7f}".format(time))

                time = measure_time(n, i, Levenstein_recursion)
                print("рекурсивный алгоритм поиска расстояния Левенштейна\n время = {:.7f}".format(time))

                time = measure_time(n, i, Damerau_Levenshtein)
                print("алгоритм поиска расстояния Дамерау-Левенштейна с заполнением матрицы\n время = {:.7f}".format(time))

                time = measure_time(n, i, Damerau_Levenshtein_recursion)
                print("рекурсивный алгоритм поиска расстояния Дамерау-Левенштейна\n время = {:.7f}".format(time))

        else:
            flag = False


if __name__ == "__main__":
    menu()

