for _ in range(int(input())):
    n = input()
    word = input()
    count_one = word.count("_")
    count__ = word.count("-")
    if count_one < 1 or count__ < 2:
        print(0)
    else:
        a = count__ // 2
        b = count__ - a
        print(a * b * count_one)