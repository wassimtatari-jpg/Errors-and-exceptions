def system_registration():
        
    try:
        user_name=input("Enter your user name: ")
        age=int(input("Enter your age:"))
        acount_number=int(input("Enter your acount number : "))
        
    except ValueError:
        return "Error: only number (inteiger) acept"

    else:
        return f"User Name: {user_name}\nAge:{age}\nAcount number:{acount_number}"
    finally:
        print("information check done")
result=system_registration()
print(result)
