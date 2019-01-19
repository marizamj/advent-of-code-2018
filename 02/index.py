def parseInput(path):
    inputArr = []

    with open(path, 'r') as input:
        for line in input.readlines():
            inputArr.append(line.strip())

    return inputArr


def checksum(arr):
    pairs = 0
    triples = 0

    for string in arr:
        found = {}

        for char in string:
            if 'pair' not in found and string.count(char) == 2:
                pairs += 1
                found['pair'] = True

            if 'triple' not in found and string.count(char) == 3:
                triples += 1
                found['triple'] = True

    return pairs * triples


def correctIDs(arr):

    def match(str1, str2):
        isGood = True
        diffInd = None

        for n in range(len(str1)):
            if str1[n] != str2[n] and diffInd != None:
                isGood = False

            if str1[n] != str2[n] and diffInd == None:
                diffInd = n

        return str1[:diffInd] + str1[diffInd + 1:] if isGood and diffInd != None else None

    result = ''

    for string1 in arr:
        if not result:
            for string2 in arr:
                if string1 != string2 and match(string1, string2):
                    return match(string1, string2)

    return result


input = parseInput('./input.txt')

print('First part answer: %s' % checksum(input))
print('Second part answer: %s' % correctIDs(input))
