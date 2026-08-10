def convert_and_sum(a,b):
    try:
        num1=int(a)
        num2=int(b)
        return num1+num2
    except ValueError:
        return "Incorrect value"
print(convert_and_sum("a",10))
print(convert_and_sum(10,2))
print(convert_and_sum("10","15"))