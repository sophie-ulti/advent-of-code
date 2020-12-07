import re


required_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyes_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_int(value, min, max):
    year = int(value)
    return min <= year <= max


def birth_year(value):
    return check_int(value, 1920, 2002)


def issue_year(value):
    return check_int(value, 2010, 2020)


def expiration_year(value):
    return check_int(value, 2020, 2030)


def height(value):
    if 'cm' in value:
        s = 'cm'
        min = 150
        max = 193
    elif 'in' in value:
        s = 'in'
        min = 59
        max = 76
    else:
        return False
    value = value.replace(s, '')
    return check_int(value, min, max)


def hair_color(value):
    match = re.search(r'^#(?:[0-9a-fA-F]{6})$', value)
    return True if match else False


def eye_color(value):
    return value in eyes_color


def pid(value):
    match = re.search(r'(?:[0-9]{9})$', value)
    return True if match and len(value) == 9 else False


required_field_with_rule = {
                               "byr": birth_year,
                               "iyr": issue_year,
                               "eyr": expiration_year,
                               "hgt": height,
                               "hcl": hair_color,
                               "ecl": eye_color,
                               "pid": pid
}


def read_input(filename):
    f = open(filename, "r")
    passports = []
    passport = ""

    for line in f:
        line = line.rstrip()
        if line == "":
            passports.append(passport)
            passport = ""
        else:
            passport += " "
            passport += line
    return passports


def has_all_field_passport(passport):
    nb_present = 0
    for field in required_field:
        if field in passport:
            nb_present += 1
    return 1 if nb_present == 7 else 0


def is_a_valid_passport(passport):
    nb_present = 0
    passport_values = passport.split(' ')
    passport_dict = {}
    for field in passport_values:
        if field != "":
            key, value = field.split(':')
            passport_dict[key] = value

    for field, validation in required_field_with_rule.items():
        if field in passport_dict:
            if validation(passport_dict[field]):
                nb_present += 1
            else:
                return False

    return 1 if nb_present == 7 else 0


passports = read_input("input_day4")
cpt = 0
for passport in passports:
    if is_a_valid_passport(passport) == 1:
        cpt += 1

print(cpt)
