for _ in range(int(input())):
    word = input().strip().lower()
    if word.endswith("po"):
        print("FILIPINO")
    elif word.endswith("desu") or word.endswith("masu"):
        print("JAPANESE")
    else:
        print("KOREAN")