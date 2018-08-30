
from time import sleep

def go():
    try:
        count = int(input("Please enter the number of digits you would like to display..."))
        result = thue(count)
        input("Press any key to continue...")
        return result
    except (NameError, ValueError):
        print("Invalid response, exiting...")
        sleep(1)
        return 0

def thue(count):
    sequence = [1]

    while len(sequence) < count:
        invertedSequence = invertArray(sequence)
        print(''.join([str(a) for a in invertedSequence]), end='')
        sequence += invertedSequence
    print("")
    return sequence

def invertArray(myArray):
    result = [0] * len(myArray)
    for i in range(len(myArray) - 1, 0, -1):
        result[i] = int(not(myArray[i]))
    
    return result
