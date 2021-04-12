def Damerau_Levenshtein(f_str, s_str):(0)
    len_f_str = len(f_str)(1)
    len_s_str = len(s_str)(2)

    F = [[(i + j) if i * j == 0 else 0 for j in range(len_s_str + 1)](3)
         for i in range(len_f_str + 1)](4)

    for i in range(1, len_f_str + 1):(5)
        for j in range(1, len_s_str + 1):(6)
            cost = 0(7)

            if f_str[i - 1] != s_str[j - 1]:(8)
                cost = 1(9)

            F[i][j] = min(F[i - 1][j] + 1, F[i][j - 1] + 1, F[i - 1][j - 1] + cost)(10)

            if i > 1 and j > 1 and f_str[i - 1] == s_str[j - 2] and f_str[i - 2] == s_str[j - 1]:(11)
                F[i][j] = min(F[i][j], F[i - 2][j - 2] + 1)(12)

    result = F[len_f_str][len_s_str](13)
    return result