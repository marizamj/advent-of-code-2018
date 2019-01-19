def parseInput(path):
    inputArr = []

    with open(path, 'r') as input:
        for line in input.readlines():
            inputArr.append(int(line.strip()))

    return inputArr


def countFrequency(arr):
    frequency = 0

    for number in arr:
        frequency = frequency + number

    return frequency


def firstDuplicate(arr):
    currentFrequency = 0
    seenFrequencies = {0: True}
    found = False

    while found == False:
        for number in arr:
            currentFrequency = currentFrequency + number

            if currentFrequency in seenFrequencies:
                found = True
                break

            seenFrequencies[currentFrequency] = True

    return currentFrequency


input = parseInput('./input.txt')

print('First part answer: %s' % countFrequency(input))
print('Second part answer: %s' % firstDuplicate(input))
