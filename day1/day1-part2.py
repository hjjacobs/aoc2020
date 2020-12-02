path = '/Users/hjj/Projects/private/aoc2020/day1/input.txt'

with open(path) as f:
    amounts = f.read().splitlines()

total = 0

for amount1 in amounts:

    if total == 2020 :
        break

    for amount2 in amounts:

        if total == 2020 :
            break

        for amount3 in amounts:

            total = int(amount1) + int(amount2) + int(amount3)

            print(f"{amount1} + {amount2} + {amount3} = {total}")

            if (total == 2020) :
                answer = int(amount1) * int(amount2) * int(amount3)
                print(f"********************** found: {amount1} + {amount2} + {amount3} = 2020 ==> {answer}")
                break