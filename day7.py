import re


class Bag:
    def __init__(self, color, to_parse):
        self.color = color
        self.to_parse = to_parse
        self.parent = {}
        self.child = {}

    def add_parent(self, name, c):
        self.parent[name] = c

    def add_child(self, name, c, number):
        self.child[name] = (number, c)

    def become_child_of_(self, name, c):
        self.add_parent(name, c)
        c.add_child(self.color, self)

    def become_parent_of_(self, name, c, number):
        c.add_parent(self.color, self)
        self.add_child(name, c, number)

    def compute_childs(self):
        childs = self.to_parse.split(', ')
        if childs[0] == "no other bags.":
            return

        for child in childs:
            r = re.match(r"(\d) (\w+) (\w+)", child)
            number = int(r.group(1))
            color_name = r.group(2) + " " + r.group(3)
            color_class = all_bag[color_name]
            self.become_parent_of_(color_name, color_class, number)

    def list_parents_recursivly(self):
        unique_parents = set(self.parent.keys())

        for parent in self.parent.values():
            grand_parent = parent.list_parents_recursivly()
            unique_parents.update(grand_parent)
        return unique_parents

    def count_parents(self):
        s = self.list_parents_recursivly()
        return len(s)

    def count_childs(self):
        nb_total = 0
        for nb, child in self.child.values():
            nb_total += nb
            if nb > 0:
                nb_total += nb * child.count_childs()
        return nb_total


def construct_bag(line):
    bag_color, to_parse = line.split(" bags contain ")
    return bag_color, Bag(bag_color, to_parse.rstrip())


f = open("input_day7", "r")
all_bag = {}
for line in f:
    bag_color, bag = construct_bag(line)
    all_bag[bag_color] = bag

for color, bag in all_bag.items():
    bag.compute_childs()


shiny = all_bag["shiny gold"]
print(shiny.count_parents())
print(shiny.count_childs())
