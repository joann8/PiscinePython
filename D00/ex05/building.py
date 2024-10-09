import sys


def ft_check_char(phrase: str) -> None:
    '''
    This function counts and print the number of upper case char, lower
    case char, spaces, punctuation mark and digits for a given string as
    argument.

    Args: phrase (str): the string to analyse.
    Returns: None
    '''

    upp_count = 0
    low_count = 0
    dig_count = 0
    spa_count = 0
    pun_count = 0
    ponctuation = '\'"!()-[]{;}:\\,<>./?@#$%^&*_~+/=|'
    # pas le droit d'importer string

    for caractere in phrase:
        if caractere.isupper():
            upp_count += 1
        if caractere.islower():
            low_count += 1
        if caractere in ponctuation:
            pun_count += 1
        if caractere == ' ' or caractere == '\n':
            spa_count += 1
        if caractere.isnumeric():
            dig_count += 1

    c_count = upp_count + low_count + pun_count + spa_count + dig_count

    print(f"The text contains {c_count} characters:")
    print(f"{upp_count} upper letters")
    print(f"{low_count} lower letters")
    print(f"{pun_count} punctuation marks")
    print(f"{spa_count} spaces")
    print(f"{dig_count} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError()
        if len(sys.argv) == 1:
            # sys.argv[0] est le nom du script donc toujours au moins 1 arg
            print("What is the text to count?")
            phrase = sys.stdin.readline()
            # pas d'utilisation de input() car /n pas compte
        else:
            phrase = sys.argv[1]
        ft_check_char(phrase)
        return

    except AssertionError as e:
        print(type(e).__name__)


if __name__ == "__main__":
    # print(main.__doc__)
    main()
