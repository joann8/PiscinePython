def ft_list_size(list1: list, list2: list) -> bool:
    """Check that two lists are the same size"""
    return True if len(list1) == len(list2) else False


def ft_list_type(list: list) -> bool:
    """Check the list type"""
    for item in list:
        if not isinstance(item, (int, float)):
            return False
    return True


def ft_check_weight(weight: int | float) -> bool:
    """Check that weight is different from 0 for division"""
    for w in weight:
        if w == 0:
            return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float]) \
                -> list[int | float]:
    bmi_list = []

    # tests des donnees
    try:
        if not ft_list_size(height, weight):
            raise ValueError("The two lists must be of the same size.")
        if not ft_list_type(height) or not ft_list_type(weight):
            raise ValueError("The two lists must contain int or float only.")
        if not ft_check_weight(weight):
            raise ValueError("Weight cannot be 0")

        for h, w in zip(height, weight):
            bmi_list.append((w / (h*h)))

        return bmi_list

    except ValueError as e:
        print(type(e).__name__ + ":", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        result_list = []
        if not ft_list_type(bmi):
            raise ValueError("BMI list must contain int or float only.")
        if not isinstance(limit, int):
            raise ValueError("Limit must be an int.")
        for result in bmi:
            result_list.append(True if result > limit else False)
        return result_list

    except ValueError as e:
        print(type(e).__name__ + ":", e)
