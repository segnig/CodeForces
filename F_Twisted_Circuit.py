a = input() == "1"
b = input() == "1"
c = input() == "1"
d = input() == "1"

result = (
    (
       ( a and b) or (c == d)
    ) and (
        (b or c) == (a and d)
    )
)

print(0)