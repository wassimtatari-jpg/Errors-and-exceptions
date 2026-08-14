import traceback

def divide_numbers(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError as e:
        traceback.print_exc()
divide_numbers(10,0)