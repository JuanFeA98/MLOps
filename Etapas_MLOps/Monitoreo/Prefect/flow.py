from prefect import flow

from time import sleep

def add_numbers(a, b):
    # sleep(5)

    return (a + b)

def multiply_numbers(x, y):
    # sleep(5)
    try:
        return (x * y)
    except:
        return 10
@flow
def calculate(a, b):
    num_sum = add_numbers(a, b)
    num_product = multiply_numbers(num_sum, num_sum)

    return num_product

if __name__ == '__main__':
    print(calculate(10, 2))