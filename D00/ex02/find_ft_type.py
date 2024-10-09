def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list) or isinstance(object, tuple) or isinstance(object, dict) or isinstance(object, set):
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen: {type(object)}")
    else:
        print("Type not found")
    return 42
