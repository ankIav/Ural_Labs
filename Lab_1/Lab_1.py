
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
        match choose('Enter the option:\n'):
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


# in this func complete the option choice
def task_2():
    pass


def task_1_option_1():

    # enter the variables
    a = input_float('Enter a value of a:\n', 'a')
    b = input_float('Enter a value of b:\n', 'b')
    c = input_float('Enter a value of c:\n', 'c')
    k = input_float('Enter a value of k:\n', 'k')

    # example with checking for division by zero
    try:
        result = abs(
            (a**2/b**2 + c**2*a**2)
            / (a + b + c*(k - a/b**3))
            + c + (k/b - k/a)*c
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'\tResult = {result}')


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
            a - b*c*d**3 + (c**5 - a**2)/a + f**3 * (a-213)
        )
    except ZeroDivisionError as err:
        print(f'Division by Zero: {err}')
    else:
        print(f'\tResult = {result}')


while True:
    match choose('Enter a task Number:\n'):
        case '1':
            task_1()
            break
        # case '2': task_2()
        case '' | 'quit' | 'exit':
            print('\tSTOP PROGRAM')
            break
        case _:
            print(f'\tIncorrect Task choice. Try again!')
            continue
