import sys


def main():
    '''This function translate an alphanumeric str into morse code.'''

    NESTED_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    ' ': '/'}

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        c_invalides = [c for c in S if not c.isalnum() and not c.isspace()]
        if c_invalides:
            raise AssertionError("the arguments are bad")

        S = S.upper()

        L_morse = []
        for c in S:
            if c in NESTED_MORSE:
                L_morse.append(NESTED_MORSE[c.upper()])

        print(f"{' '.join(L_morse)}")

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    # print(main.__doc__)
    main()
