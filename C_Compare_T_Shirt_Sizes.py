for _ in range(int(input())):
    a, b = input().split()
    if a[-1] == "L":
        if b[-1] == "L":
            if len(a) > len(b):
                print(">")
            elif len(a) < len(b):
                print("<")
            else:
                print("=")
        else:
            print(">")
    elif a[-1] == "S":
        if b[-1] == "S":
            if len(a) < len(b):
                print(">")
            elif len(a) > len(b):
                print("<")
            else:
                print("=")
        else:
            print("<")
    
    elif a[-1] == "M":
        if b[-1] == "M":
            print("=")
        elif b[-1] == "S":
            print(">")
        else:
            print("<")     