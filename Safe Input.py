def get_number():
    try:
        user_number=int(input("Enter a number : "))
    except (ValueError,TypeError) as e:
        return f"You should enter number!!!! {e}"
    else:
        return user_number
    finally:
        print("program finished")
result=get_number()
print(result)