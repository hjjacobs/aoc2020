#
# AoC 2020 ; Day 4 Part 1
# Count the number of valid passports - those that have all required fields. Treat cid as optional.
# 

def read_file():

    pasports = []
    pasport = []

    with open('day4/input.txt') as f:
        for line in f:
            items = line.rstrip().split(' ')

            if items[0] != '':   # Empty line
                pasport.extend(items)
            
            if line == '\n':     # Empty line
                pasports.append(pasport)
                pasport = []

    pasports.append(pasport)

    return pasports

def extract_pasport_fields(pasport):
    fields = []

    for field in pasport:
        fields.append(field.split(':')[0])

    return fields

def check_pasports(pasports):
#    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # fixed for cid
    number_of_valid_pasports = 0

    for pasport in pasports:

        pasport_check_ok = True

        fields = extract_pasport_fields(pasport)

        for rf in required_fields:
            pasport_check_ok = pasport_check_ok & (rf in fields)   

        if pasport_check_ok:
            number_of_valid_pasports+=1
        
    return number_of_valid_pasports


def main():
    pasports = read_file()
    print(f"Pasport count {len(pasports)}")
    print(f"Number of valid pasports: {check_pasports(pasports)}")

if __name__ == '__main__':
    main()
