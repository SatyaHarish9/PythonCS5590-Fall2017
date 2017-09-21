str = input("Enter the sentence")
words = str.split()
empty = ""
for w in words:
    if w not in empty:
        empty = " ".join((empty,w))

empty1 = empty.split()
empty1.sort()
for e in empty1:
    print(e)