def count_valid_passwords():
    valid_passwords = 0

    with open('day2/input.txt') as f:
        for line in f:
            items = line.split(' ')
            min = int(items[0].split('-')[0])
            max = int(items[0].split('-')[1])
            letter = items[1].split(':')[0]
            password = items[2].rstrip()
            count = password.count(letter)

            if (count >= min and count <= max):
                print(f'Char "{letter}" minimum {min} and maximum {max} in password {password} occurs {count} times')
                valid_passwords += 1

    return valid_passwords


def main():
    print(f'Number of valid password: {count_valid_passwords()}')

if __name__ == '__main__':
    main()
