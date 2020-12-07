

def read_input(filename):
    tableau = []
    f = open(filename, "r")
    for line in f:
        tableau.append(int(line))
    return tableau


def find_addition(tableau):
    for first in tableau:
        for second in tableau:
            if first + second == 2020:
                return first * second
    return 0


def find_three_component(tableau):
    tableau.sort()
    for first in tableau:
        for second in tableau:
            for third in tableau:
                if first + second + third == 2020:
                    return first * second * third

tableau = read_input('input_day1')
print(tableau[0])
result = find_three_component(tableau)
print(result)
