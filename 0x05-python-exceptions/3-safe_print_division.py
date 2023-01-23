#!/usr/bin/python3
def safe_print_division(a, b):
    """function that divides 2 integers and prints the result
    Args:
        a: first integer
        b: second integer
    Returns:
        value of the division,
        Otherwise - None
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
