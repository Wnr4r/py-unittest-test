# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sum(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sum(6,6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
