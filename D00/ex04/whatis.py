import sys

#checks errors argv
if len(sys.argv) == 1: #sys.argv[0] est le nom du script donc toujours au moins 1 arg
    sys.exit()
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")

else:
    try:
        arg = int(sys.argv[1])  # Convertit l'argument en entier
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit()     
    if arg % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

sys.exit()
