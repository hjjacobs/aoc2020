def count_valid_passwords():
    number_of_valid_passwords = 0

    with open('day2/test.txt') as f:
        for line in f:
            items = line.split(' ')
            pos1 = int(items[0].split('-')[0])
            pos2 = int(items[0].split('-')[1])
            letter = items[1].split(':')[0]
            password = items[2].rstrip()

            letter_pos1 = password[pos1-1]
            letter_pos2 = password[pos2-1]

            # Alternative from reddit - addind boolens
            # bool(letter_pos1 == letter) + bool(letter_pos2 == letter) must be 1 for 1 occurence

            if (letter_pos1 != letter_pos2) and ((letter_pos1 == letter) or (letter_pos2 == letter)):
                print(f'Char "{letter}" on {pos1}:{letter_pos1} and {pos2}:{letter_pos2} in password {password}')
                number_of_valid_passwords += 1

    return number_of_valid_passwords


def main():
    print(f'Number of valid password: {count_valid_passwords()}')

if __name__ == '__main__':
    main()
