#
# AoC 2020 ; Day 4 Part 2
# Count the number of valid passports - those that have all required fields. Treat cid as optional.
# 

import re

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

def check_pasport_data(pasport):
    valid = True

    for field in pasport:
        fld_id, data = field.split(':')

        valid = check_byr(valid, fld_id, data)

        valid = check_iyr(valid, fld_id, data)

        valid = check_eyr(valid, fld_id, data)

        valid = check_hgt(valid, fld_id, data)
        
        valid = check_hcl(valid, fld_id, data) 

        valid = check_ecl(valid, fld_id, data)

        valid = check_pid(valid, fld_id, data)

    return valid

def check_pid(valid, fld_id, data):
    if (valid and fld_id == 'pid'):
        valid = (len(data) == 9) and data.isdigit()
    return valid

def check_ecl(valid, fld_id, data):
    if (valid and fld_id == 'ecl'):
        valid = (data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    return valid

def check_hcl(valid, fld_id, data):
    if (valid and fld_id == 'hcl'):
        valid = (re.match("\#[0-9, a-f]{6}", data) != None) 
    return valid

def check_hgt(valid, fld_id, data):
    if (valid and fld_id == 'hgt'):        
        if (data[-2:] == 'in'):
            valid = (59 <= int(data[:-2]) <= 76)
        elif (data[-2:] == 'cm'):
            valid = (150 <= int(data[:-2]) <= 193)
        else:
            valid = False
    return valid

def check_eyr(valid, fld_id, data):
    if (valid and fld_id == 'eyr'):
        valid = ( 2020 <= int(data) <= 2030 )
    return valid

def check_iyr(valid, fld_id, data):
    if (valid and fld_id == 'iyr'):
        valid = ( 2010 <= int(data) <= 2020 )
    return valid

def check_byr(valid, fld_id, data):
    if (valid and fld_id == 'byr'):
        valid = ( 1920 <= int(data) <= 2002 )
    return valid


def check_pasports(pasports):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # fixed for cid
    number_of_valid_pasports = 0

    for pasport in pasports:

        pasport_check_ok = True

        fields = extract_pasport_fields(pasport)

        for rf in required_fields:
            pasport_check_ok = pasport_check_ok & (rf in fields)   

        if pasport_check_ok and check_pasport_data(pasport):
            number_of_valid_pasports+=1
        
    return number_of_valid_pasports


def main():
    pasports = read_file()
    print(f"Pasport count {len(pasports)}")
    print(f"Number of valid pasports: {check_pasports(pasports)}")

if __name__ == '__main__':
    main()
