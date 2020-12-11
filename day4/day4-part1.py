#
# AoC 2020 ; Day 4 Part 1
# Count the number of valid passports - those that have all required fields. Treat cid as optional.
# 

def read_file():

    pasports = []
    pasport = []

    with open('day4/test.txt') as f:
        for line in f:
            items = line.rstrip().split(' ')

            if items[0] != '':   # Empty line
                pasport.extend(items)
            
            if line == '\n':     # Empty line
                pasports.append(pasport)
                pasport = []

    pasports.append(pasport)

    return pasports

def check_pasports(pasports):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    for pasport in pasports:
        print(pasport)
        for field in pasport:
            fieldid = field.split(':')[0]
            if fieldid in required_fields:
                print('ok')
            


def main():
    pasports = read_file()
    print(f"Pasport count {len(pasports)}")
    check_pasports(pasports)

if __name__ == '__main__':
    main()
