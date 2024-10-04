import sys
from ft_filter import ft_filter

def isInt(element):
    if isinstance(element, int):
        return True
    return False

def main():
    print(filter.__doc__)
    list = [1,"tata", 2, 5.666, 3]
    list1 = filter(isInt, list)
    list2 = ft_filter(isInt, list)

    print(f"List = {list}")
    print(f"filter = {list1}")
    print(f"filter = {list2}")

if __name__ == "__main__":
    # print(main.__doc__)
    main()
