def parse_string(line):
    numbers, letter, password = line.split(' ')
    letter = letter.replace(':', '')
    int1s, int2s = numbers.split('-')
    int1 = int(int1s)
    int2 = int(int2s)
    return int1, int2, letter, password


def is_valid_1(line):
    mini, maxi, letter, password = parse_string(line)

    count = password.count(letter)
    minb = count >= mini
    maxb = count <= maxi
    return minb and maxb


def is_valid_2(line):
    index1, index2, letter, password = parse_string(line)

    if len(password) < index2:
        return False
    first = password[index1-1] == letter
    second = password[index2-1] == letter
    return (first and not second) or (not first and second)

cpt = 0
f = open("input_day2_1", "r")
for line in f:
    if is_valid_2(line):
        cpt += 1

print(cpt)
