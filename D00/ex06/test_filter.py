from ft_filter import ft_filter


def isInt(element):
    return isinstance(element, int)
    

def main():
    # Verification impression __doc__"
    print(f"\nfilter.__doc:\n{filter.__doc__}")
    print(f"\nft_filter.__doc:\n{ft_filter.__doc__}")

    # Test 1 - Traitement avec donnees
    data = [1, "tata", 2, 5.666, 3, 0, "", []]
    result_origin1 = filter(isInt, data)
    result_ft1 = ft_filter(isInt, data)

    print(f"\nList = {data}")
    print(f"filter = {result_origin1}")
    print(f"list(filter) = {list(result_origin1)}")
    print(f"ft_filter = {result_origin1}")
    print(f"list(ft_filter) = {list(result_ft1)}")

    # Test 2 - Traitement avec None
    result_origin2 = filter(None, data)
    result_ft2 = ft_filter(None, data)

    print(f"\nList = {data}")
    print(f"filter = {result_origin2}")
    print(f"list(filter) = {list(result_origin2)}")
    print(f"ft_filter = {result_origin2}")
    print(f"list(ft_filter) = {list(result_ft2)}")


if __name__ == "__main__":
    main()
