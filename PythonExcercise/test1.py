def loop_over_list():
    numbers = [1, 2, 3, 4, 5, 6]
    result = []

    # Write your code here
    for number in numbers:
        result.append(number)
        number = range(number)
        print(number)
    return result
