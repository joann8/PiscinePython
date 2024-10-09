
def NULL_not_found(object: any) -> int:
    if isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    elif object is None:
        print(f"Nothing: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
