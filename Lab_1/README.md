# Lab work № 1

### 1. Write a program to solve the example (by options). Consider checking for division by zero. All required variables the user enters through the console. Record |example| means "to take module”, i.e. if the value is negative, then change sign from minus to plus.
- ### Option 1. ![img.png](images/lab1_t1_op1.png)
- ### Option 4. ![img.png](images/lab1_t1_op2.png)
---
# Result 1:

- the choice of task and option is made through functions in the following sequence: _choose_ -> _task_num()_ -> _choose_ ->_option_num()_
- for the correct input of the value, the function  is implemented _input_float()_

### 2. Given an arbitrary list containing both strings and numbers.
- ### Option 1. Output all even elements line by line.
- ### Option 4. Print all odd elements on one line.
---
# Result 2:

- To solve the option 1 condition we can use _for_ cycle:

       for i, el in enumerate(str_list):
           if i % 2 == 0 and i > 0:
               print(i, el)
- To solve the option 2 condition we can use list comprehension and * operator before:

        print(*[str_list[i] for i in range(len(str_list)) if i % 2 == 0])

### 3. Given an arbitrary list containing only numbers.
- ### Option 1. Print the result of adding all numbers greater than 10.
- ### Option 2. Print the result of adding all numbers from 1 to 10.
- ### Option 4. Print the result of multiplying all numbers less than 10.
---
# Result 3:

- To solve option 1 and 2 conditions we can use _filter_ and _lambda_-function:

      print('Option 1: sum =', sum(list(filter(lambda x: x > 10, numbers))))
      print('Option 2: sum =', sum(list(filter(lambda x: 1 < x < 10, numbers))))
- To solve option 3 we need to create _**mul**_  to calculate the result using only built-in features:

      mul = 1
      for i in list(filter(lambda x: x < 10, numbers)):
          mul *= i
      print('Option 4: mul =', mul, 3)

### 4. Given an arbitrary list containing only numbers.
- ### Option 1. Print the maximum number.
- ### Option 2. Print the minimum number.
- ### Option 3. Print the arithmetic mean (sum of all numbers, divided by the number of elements).
- ### Option 4. Output the number in the middle of the array.
---
# Result 4:

- To find maximum number we can use _max_ function:

      print('Option 1: max =', max(numbers))
- To find minimum number we can use _min_ function:

      print('Option 2: min =', min(numbers))
- The solution of the task is contained in its description. The only thing I can highlight is the rounding _round_ function:

      print('Option 3: Avg =', round(sum(numbers) / len(numbers), 3))
- If there are 2 elements in the middle at once, then you need to return the value of the second one:

      print('Option 4: mid =', numbers[len(numbers)//2])
    *NOTE But if we need to get the value of the first one, then: (**_a_** is some iterable obj)

      print(a[len(a)//2-1 if len(a) % 2 == 0 else len(a)//2])