
def input_float(msg: str, char: str):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(f'Wrong value {char}, Try again!')
            continue


# choose task
def task_choose():
    while True:
        match input(
            f'\tEnter the task number (1, 2):\n'
            f'<Enter>/quit/exit to exit the program!\n'
        ).lower().strip():
            case '1':
                task_1()
                return 1
            case '2':
                task_2()
                return 2

            case '' | 'quit' | 'exit':  # how to exit program option
                print('Closing the program.')
                break
            # default output, out of cases:
            case _:
                print(f'\tWrong task number of incorrect input. Try again!')
                continue


# choose option in task
def option_choose():
    while True:
        match input(
            f'\tEnter the option number (1, 4):\n'
            f'<Enter>/quit/exit to exit the program!\n'
        ).lower().strip():
            case '1':
                option_1()
                return 1
            case '4':
                option_4()
                return 4

            case '' | 'quit' | 'exit':  # how to exit program option
                print('Closing the program.')
                break
            # default output, out of cases:
            case _:
                print(f'\tWrong task number of incorrect input. Try again!')
                continue


def task_1():
    try:
        task = option_choose()
    finally:
        print('\tEnd of Task 1.')


def task_2():
    pass


def option_1():

    a = input_float('Enter a value of a:\n', 'a')
    b = input_float('Enter a value of b:\n', 'b')
    c = input_float('Enter a value of c:\n', 'c')
    k = input_float('Enter a value of k:\n', 'k')

    try:
        result = abs(
            (a**2/b**2 + c**2*a**2)
            / (a + b + c*(k - a/b**3))
            + c + (k/b - k/a)*c
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'Result = {result}')


def option_4():
    a = input_float('Enter a value of a:\n', 'a')
    b = input_float('Enter a value of b:\n', 'b')
    c = input_float('Enter a value of c:\n', 'c')
    d = input_float('Enter a value of d:\n', 'd')
    f = input_float('Enter a value of f:\n', 'f')

    try:
        result = abs(
            a - b*c*d**3 + (c**5 - a**2)/a + f**3 * (a-213)
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'Result = {result}')


task_choose()
