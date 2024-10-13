def give_bmi(height: list[int | float], weight: list[int | float]) \
                -> list[int | float]:
    '''
    This function calculate the BMI given two lists of weight (int, float) and
    height (int, float). It returns a list with the results.
    '''
    bmi_list = []

    try:
        if not isinstance(height, list) or\
           not isinstance(weight, list):
            raise ValueError("You must provide two lists of int or float.")
        if not all(isinstance(h, (int, float)) for h in height) or \
           not all(isinstance(w, (int, float)) for w in weight):
            raise ValueError("The two lists must contain int or float only.")
        if not len(height) == len(weight):
            raise ValueError("The two lists must be of the same size.")
        if not all(h > 0 for h in height) or not all(w > 0 for w in weight):
            raise ValueError("Height and weigth should be stricly positive")

        for h, w in zip(height, weight):
            bmi_list.append((w / (h*h)))

        return bmi_list

    except ValueError as e:
        print(type(e).__name__ + ":", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This function applies an int as a limit to a BMI list and
    returns a list of boolean as a result.
    '''
    try:
        if not isinstance(bmi, list):
            raise ValueError("You must provide a list of int or float.")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise ValueError("BMI list must contain int or float only.")
        if not isinstance(limit, int):
            raise ValueError("Limit must be an int.")
        return [b > limit for b in bmi]

    except ValueError as e:
        print(type(e).__name__ + ":", e)
