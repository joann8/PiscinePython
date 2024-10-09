import sys
from ft_filter import ft_filter


def main():
    '''
    This function outputs a list a world from a given string
    that have a length greater than a given interger.
    '''
    try:

        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        c_invalides = [c for c in S if not c.isalnum() and not c.isspace()]
        if c_invalides:
            raise AssertionError("the arguments are bad")

        words = S.split(" ")
        list_finale = list(ft_filter(lambda word: len(word) > N, words))
        print(list_finale)

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    # print(main.__doc__)
    main()
