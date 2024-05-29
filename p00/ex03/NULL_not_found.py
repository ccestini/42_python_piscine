def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and object != object:  # Check for NaN (Not a Number), condition to check is not equal to itself
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == "":
        print(f"Empty: {type(object)}")
    else:
        print("Type not Found")
        return 1  # Return 1 in case of error, not found
    return 0  # Return 0 if it goes well and there is a type of NULL
