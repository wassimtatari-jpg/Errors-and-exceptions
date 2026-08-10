def  safe_division(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
       return "Error : Invalid Type"
    return result
print(safe_division(10,"2"))
