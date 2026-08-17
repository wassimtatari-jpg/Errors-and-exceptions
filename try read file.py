try:
    my_file=open("data.txt","r")
    content=my_file.read()
except FileNotFoundError:
    print("Error: This file not exist")
else:
    print(content)
finally:
   
    print("The operation is done")