# python3
def max_pairwise_product(numbers):
    n = len(numbers)
    a, b = 0, 0
    for i in numbers:
        if i > a:
            if a >= b:
                b = a
            a = i
        elif i <= a:
            if i > b:
                b = i

    return a*b


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
