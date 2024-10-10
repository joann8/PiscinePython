import numpy as np
import matplotlib.pyplot as plt  # ouvrrir une image sous forme de np.array
import array


def ft_invert(array) -> array:
    '''Apply an inverting filter on img with operators =, +, -, * '''
    if array is None:
        return None
    img_invert = 255 - array
    display_img(img_invert)
    return img_invert


def ft_red(array) -> array:
    '''Apply a red filter on img with operators = * '''
    if array is None:
        return None
    red_img = np.copy(array)
    red_img = red_img * [1, 0, 0]
    display_img(red_img)
    return red_img


def ft_green(array) -> array:
    '''Apply a green filter on img with operators = - '''
    if array is None:
        return None
    green_img = np.copy(array)
    green_img[:, :, 0] -= green_img[:, :, 0]  # On enleve le rouge
    green_img[:, :, 2] -= green_img[:, :, 2]  # On enleve le bleu
    display_img(green_img)
    return green_img


def ft_blue(array) -> array:
    '''Apply a blue filter on img with operator = '''
    if array is None:
        return None
    blue_img = np.copy(array)
    blue_img[:, :, 0] = 0  # Canal rouge a 0
    blue_img[:, :, 1] = 0  # Canal vert a 0
    display_img(blue_img)
    return blue_img


def ft_grey(array) -> array:
    '''Apply a grey filter on img with operator = / '''
    if array is None:
        return None
    red = array[:, :, 0]
    green = array[:, :, 1]
    blue = array[:, :, 2]

    grey_img = (red / 3 + green / 3 + blue / 3).astype(np.uint8)

    grey_img = np.stack((grey_img, grey_img, grey_img), axis=2)
    display_img(grey_img)
    return grey_img


def display_img(img: array) -> None:
    if img.size == 0:  # on check qu'on a bien un tableau a afficher
        print("No image to display")
    else:
        # print("image size check: ", img.shape)
        plt.imshow(img)
        plt.show()
