import sys


def main():
    '''
    This function counts the number of upper case, lower case,
    punctuation mark and digits for a given string.
    '''

    if len(sys.argv) > 2:
        print("AssertionError")
        sys.exit()
    if len(sys.argv) == 1:
        # sys.argv[0] est le nom du script donc toujours au moins 1 arg
        print("What is the text to count?")
        phrase = input()
    else:
        phrase = sys.argv[1]

    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    punctuation_count = 0
    ponctuation = '\'"!()-[]{;}:\\,<>./?@#$%^&*_~+/=|'

    for caractere in phrase:
        if caractere.isupper():
            upper_count += 1
        if caractere.islower():
            lower_count += 1
        if caractere in ponctuation:
            punctuation_count += 1
        if caractere == ' ':
            space_count += 1
        if caractere.isnumeric():
            digit_count += 1

    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

    sys.exit()


if __name__ == "__main__":
    # print(main.__doc__)
    main()
