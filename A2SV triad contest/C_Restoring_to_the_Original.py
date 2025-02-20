input()
word = input()
 
ones = word.count("n")
zeros = word.count("z")

for _ in range(ones):
    print("1", end=" ") 
for _ in range(zeros):
    print("0", end=" ")