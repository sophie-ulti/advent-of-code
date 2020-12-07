

def count_tree(t, rowchange, linechange):
    coords = (0, 0)
    cpt = 0
    has_next = True
    lines = len(t)

    while has_next:
        tree, coords = check_and_move(t, coords, rowchange, linechange)
        if tree:
            cpt += 1
        if coords[0] >= lines:
            has_next = False
    return cpt


def check_and_move(t, coords, rowchange, linechange):
    has_tree = False
    if t[coords[0]][coords[1]] == '#':
        has_tree = True
    line = coords[0] + linechange
    row = (coords[1] + rowchange) % 31
    return has_tree, (line, row)


f = open("input_day3", "r")
t = []
for line in f:
    t.append(line.rstrip())

cpt11 = count_tree(t, 1, 1)
cpt31 = count_tree(t, 3, 1)
cpt51 = count_tree(t, 5, 1)
cpt71 = count_tree(t, 7, 1)
cpt12 = count_tree(t, 1, 2)

product = cpt11 * cpt12 * cpt31 * cpt51 * cpt71
print(product)
