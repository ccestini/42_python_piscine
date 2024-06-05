def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        if object == "Brian":
            print(f"Brian is in the kitchen : {type(object)}")
        elif object == "Toto":
            print(f"Toto is in the kitchen : {type(object)}")
        else:
            print(f"Unknown string : {type(object)}")
    else:
        print(f"Type not found")
    return 42
