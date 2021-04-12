import random
from time import time


def StandardMultiplication(a, b):
    an = len(a)
    am = len(a[0])

    bn = len(b)
    bm = len(b[0])

    c = [[0 for i in range(bm)] for j in range(an)]

    for i in range(an):
        for j in range(bm):
            for k in range(am):
                c[i][j] += a[i][k] * b[k][j]
    return c


def MultiplicationVinograd(a, b):
    an = len(a)
    am = len(a[0])

    bn = len(b)
    bm = len(b[0])

    c = [[0 for i in range(bm)] for j in range(an)]
    mulH = [0 for j in range(an)]
    mulV = [0 for i in range(bm)]

    for i in range(an):
        for j in range(int(am / 2)):
            mulH[i] = mulH[i] + a[i][j * 2] * b[i][j * 2 + 1]

    for i in range(bm):
        for j in range(int(bn / 2)):
            mulV[i] = mulV[i] + b[j * 2][i] * b[j * 2 + 1][i]

    for i in range(an):
        for j in range(bm):
            c[i][j] = -mulH[i] - mulV[j]
            for k in range(int(am / 2)):
                c[i][j] = c[i][j] + (a[i][2 * k + 1] + b[2 * k][j]) * (a[i][2 * k] + b[2 * k + 1][j])

    if am % 2:
        for i in range(an):
            for j in range(bm):
                c[i][j] = c[i][j] + a[i][am - 1] * b[am - 1][j]

    return c


def MultiplicationVinogradOptimize(a, b):
    an = len(a)
    am = len(a[0])

    bn = len(b)
    bm = len(b[0])

    c = [[0 for i in range(bm)] for j in range(an)]
    mulH = [0 for j in range(an)]
    mulV = [0 for i in range(bm)]

    # 1
    modam = am % 2
    modbn = bn % 2

    for i in range(an):
        for j in range(0, am - modam, 2):  # 2
            mulH[i] = mulH[i] + a[i][j] * a[i][j + 1]

    for i in range(bm):
        for j in range(0, bn - modbn, 2):
            mulV[i] = mulV[i] + b[j][i] * b[j + 1][i]

    for i in range(an):
        for j in range(bm):
            buff = -mulH[i] - mulV[j]  # 3
            for k in range(0, am - modam, 2):
                buff = buff + (a[i][k+1] + b[k][j]) * (a[i][k] + b[k + 1][j])
            c[i][j] = buff
    if modam:
        minam = am - 1  # 4
        for i in range(an):
            for j in range(bm):
                c[i][j] = c[i][j] + a[i][minam] * b[minam][j]

    return c


def input_matrix():
    n = int(input("Введите длину матрицы: "))
    m = int(input("Введите высоту матрицы: "))

    a = [[(int(input("Введите " + str(i + 1) + " элемент " + str(j + 1) + " строки: "))) for i in range(n)] for j in
         range(m)]

    return a


def generate_matrix(n, m):
    a = [[random.randint(-10000, 10000) for i in range(n)] for j in range(m)]

    return a


def print_matrix(a):
    print("\nОтвет:\n")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print("\n")


def measure_time(n, m, f):
    overall_time = 0.0
    for i in range(n):
        a = generate_matrix(m, m)
        b = generate_matrix(m, m)
        start = time()
        f(a, b)
        end = time()
        overall_time = end - start

    return overall_time / n


def menu():
    flag = True
    while 1:
        do = int(input("\nВыберите один из пунктов меню:\n"
                       "1 - стандартный алгоритм умножения матриц\n"
                       "2 - алгоритм Виноградова\n"
                       "3 - модифицированный алгоритм Виноградова\n"
                       "4 - применение всех алгоритмов\n"
                       "5 - замеры времени\n"
                       "6 - завершение программы\n"
                       "выбор: "))
        if do == 1:
            a = input_matrix()
            b = input_matrix()
            print_matrix(StandardMultiplication(a, b))
        if do == 2:
            a = input_matrix()
            b = input_matrix()
            print_matrix(MultiplicationVinograd(a, b))
        if do == 3:
            a = input_matrix()
            b = input_matrix()
            print_matrix(MultiplicationVinogradOptimize(a, b))
        if do == 4:
            a = input_matrix()
            b = input_matrix()

            print_matrix(StandardMultiplication(a, b))
            print_matrix(MultiplicationVinograd(a, b))
            print_matrix(MultiplicationVinogradOptimize(a, b))
        if do == 5:
            n = 100
            len_matrix = 500
            for i in range(101, len_matrix + 4, 100):
                print("\nРазмер матрицы: " + str(i))

                time = measure_time(n, i, StandardMultiplication)
                print("стандартный алгоритм умножения матриц\nвремя = {:.10f}".format(time))

                time = measure_time(n, i, MultiplicationVinograd)
                print("алгоритм Виноградова\nвремя = {:.10f}".format(time))

                time = measure_time(n, i, MultiplicationVinogradOptimize)
                print("модифицированный алгоритм Виноградова\nвремя = {:.10f}".format(
                    time))
        else:
            flag = False


if __name__ == "__main__":
    menu()
