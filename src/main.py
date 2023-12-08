def fizzBuzz():
    list = []

    for x in range(1, 101, 1):
        list.append(x)

    new_list = []

    for number in list:
        if number % 3 == 0 and number % 5 == 0:
            new_list.append('FizzBuzz')
        elif number % 3 == 0:
            new_list.append('Fizz')
        elif number % 5 == 0:
            new_list.append('Buzz')
        else:
            new_list.append(number)

    return new_list


if __name__ == '__main__':
    print(fizzBuzz())