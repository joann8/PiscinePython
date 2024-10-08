import sys

try:
    #checks errors argv
    if len(sys.argv) == 1: #sys.argv[0] est le nom du script donc toujours au moins 1 arg
        sys.exit()
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    else:
        try:
            arg = int(sys.argv[1])  # Convertit l'argument en entier
        except ValueError:
            raise AssertionError("argument is not an integer")
        if arg % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")

except AssertionError as e:
    print(f"AssertionError: {e}")