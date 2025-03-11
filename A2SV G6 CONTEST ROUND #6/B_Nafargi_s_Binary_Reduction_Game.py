input()
word = input()

ones = word.count("1")

zeros = word.count("0")

print(abs(zeros - ones))