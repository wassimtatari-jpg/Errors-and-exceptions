def procces_input(input_string):
    try:
        if input_string=="":
            raise IndexError("Empety string")
        number=int(input_string)
        return number**2
    except ValueError:
        print("Error: The sting  enter is not number")
    except IndexError:
        print("Error: An empety string was entred")
print(procces_input("5"))
print(procces_input("abc"))
print(procces_input(""))