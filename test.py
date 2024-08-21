from itertools import combinations
def starter(x) -> str:
    word = ''
    for i in range(x):
        word += 'a'
    return word


bucket = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i in range(1, 4):
    count = 1
    string = starter(i)
    while count < 10 ** len(string):
        print(count)
        count += 1

var = com