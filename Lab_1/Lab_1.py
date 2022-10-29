# float value input
def input_float(msg='Enter the float value of', char='variable') -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(f'Wrong value {char}, Try again!')
            continue


# choose func with exit option
def choose(msg='Choose\n'): return input(msg).strip().lower()


# in this func complete the option choice
def task_1():
    while True:
        match choose('Enter the option (1, 4):\n'):
            case '1':
                task_1_option_1()
                break
            case '4':
                task_1_option_4()
                break
            case '' | 'quit' | 'exit':
                print('\tSTOP PROGRAM')
                break
            case _:
                print(f'\tIncorrect Option choice. Try again!')
                continue


# task 1 option 1 solution
def task_1_option_1():
    # enter the variables
    a = input_float('Enter a value of a:\n', 'a')
    b = input_float('Enter a value of b:\n', 'b')
    c = input_float('Enter a value of c:\n', 'c')
    k = input_float('Enter a value of k:\n', 'k')

    # example with checking for division by zero
    try:
        result = abs(
            (a ** 2 / b ** 2 + c ** 2 * a ** 2)
            / (a + b + c * (k - a / b ** 3))
            + c + (k / b - k / a) * c
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'\tResult = {round(result, 3)}')


# task 1 option 2 solution
def task_1_option_4():
    # enter the variables
    a = input_float('Enter a value of a:\n', 'a')
    b = input_float('Enter a value of b:\n', 'b')
    c = input_float('Enter a value of c:\n', 'c')
    d = input_float('Enter a value of d:\n', 'd')
    f = input_float('Enter a value of f:\n', 'f')

    # example with checking for division by zero
    try:
        result = abs(
            a - b * c * d ** 3 + (c ** 5 - a ** 2) / a + f ** 3 * (a - 213)
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'\tResult = {round(result, 3)}')


# task 2 solution options 1, 4
def task_2():
    str_list = input('Enter some list through the whitespace:\n').split()

    # option 1 solution
    print('\tOption 1:\n')
    for i, el in enumerate(str_list):
        if i % 2 == 0 and i > 0:
            print(i, el)

    # option 4 solution
    print('\tOption 4:\n')
    print(*[str_list[i] for i in range(len(str_list)) if i % 2 == 0])


# task 3 solution options 1, 2, 4
def task_3():
    while True:
        try:
            numbers = list(map(float, input('Enter number thru WS\n').split()))
        except ValueError:
            continue
        else:
            # option 1 solution
            print('Option 1: sum =', sum(
                list(filter(lambda x: x > 10, numbers))))

            # option 2 solution
            print('Option 2: sum =', sum(
                list(filter(lambda x: 1 < x < 10, numbers))))

            # option 4 solution
            mul = 1
            for i in list(filter(lambda x: x < 10, numbers)):
                mul *= i

            print('Option 4: mul =', mul, 3)

            break


# task 4 solution options 1-4
def task_4():
    while True:
        try:
            numbers = list(map(float, input('Enter number thru WS\n').split()))
        except ValueError:
            continue
        else:
            # option 1 solution
            print('Option 1: max =', max(numbers))
            # option 2 solution
            print('Option 2: min =', min(numbers))
            # option 3 solution
            print('Option 3: Avg =', round(sum(numbers) / len(numbers), 3))
            # option 4 solution
            print('Option 4: mid =', numbers[len(numbers)//2])

            break


# main program
while True:
    match choose('Enter a task Number (1 - 4):\n'):
        case '1':
            task_1()
            break
        case '2':
            task_2()
            break
        case '3':
            task_3()
            break
        case '4':
            task_4()
            break
        case '' | 'quit' | 'exit':
            print('\tSTOP PROGRAM')
            break
        case _:
            print(f'\tIncorrect Task choice. Try again!')
            continue
