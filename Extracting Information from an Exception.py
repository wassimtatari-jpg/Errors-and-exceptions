def read_sting(input_string):
    excpetion_instance=None
    try:
        number=int(input_string)
        return number
    except ValueError as e:
        excpetion_instance=e
        print(f"Error agruments {e.args}")
        print(f"Error type {type(e)}")
    print(f"excpetion error : {excpetion_instance}")
read_sting("abc")