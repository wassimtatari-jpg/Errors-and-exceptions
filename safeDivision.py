def safe_division():
    try:
        num1=int(input("Enter first number : "))
        num2=int(input("Enter second number : "))
        result= num1/num2
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError:
        return "Incorrect value"
    else:
       return result
    finally:
        print("Operation end")


result=safe_division()
print(f"Result {result}")
