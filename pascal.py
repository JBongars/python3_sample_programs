from clear import clear  

def go():

    clear()
    levels = int(input('Enter the number of levels... '))
    prevLevel = [1]
    curLevel = []

    for i in range(levels):
        print(' '.join(str(x) for x in prevLevel))
        curLevel = []

        for j in range(len(prevLevel) + 1):
            if j == 0 or j == len(prevLevel):
                curLevel.append(1)
            else:
                curLevel.append(prevLevel[j] + prevLevel[j - 1])
        prevLevel = curLevel

    print('done!')
    input("Press any key to continue...")

def factorial(a):
    result = 1
    while a > 0:
        result *= a
        a -= 1
    return result

def combinations(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


print(combinations(7, 4)) # expected: 35
print(combinations(6, 5)) # expected: 6
print(combinations(12, 6)) # expected: 924
