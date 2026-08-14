list_fruit=["apple","banana","stubery","cherry","lemmon"]
def find_index():
    try:
        user_index=int(input("Enter an Index to find it from list: "))
        fruit=list_fruit[user_index]
    except ValueError:
        return "Error: Value entred not integer"
    except IndexError:
        return "Error Index entred outside the range of list!!!"
    else:
        return fruit
    finally:
        print("Search operation end")
result=find_index()
print(f"Result {result}")
       
   