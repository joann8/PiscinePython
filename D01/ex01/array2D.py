import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Function that takes as parameters a 2D array, prints its shape, and
    returns a truncated version of the array based on the provided
    start and end arguments.
    '''

    try:
        if not isinstance(family, list) or not isinstance(start, int) or\
           not isinstance(end, int):
            raise AssertionError("You must provide a list and 2 integers")
        np_family = np.array(family)
        np_new_family = np_family[start:end:1]
        print(f"My shape is: {np_family.shape}")
        print(f"My new shape is: {np_new_family.shape}")
        return np_new_family.tolist()

    except AssertionError as e:
        print(type(e).__name__ + ":", e)
