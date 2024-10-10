from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt  # ouvrrir une image sous forme de np.array
import array
from PIL import Image


def cut_quare_image(img: array, x_start: int, y_start: int,
                    length: int) -> array:
    """
    Cut a square on an image provided as an array, and given
    some specific dimensions.
    """
    try:
        new_img = img[y_start:(y_start + length), x_start:(x_start + length)]
        return new_img

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


def img_to_gray(img: array) -> array:
    '''
    Convert an image to GRAYSCALE
    '''
    img_tmp = Image.fromarray(img)
    # Propriete Luminance pour convertir une image en gris
    img_tmp_gray = img_tmp.convert("L")
    # L'image résultante est un tableau 2D (h x l) où chaque élément représente
    # l'intensité des pixels.
    img_gray = np.array(img_tmp_gray)
    # le resultat est un tableau 2D (h x l)
    return img_gray


def shape_array(img: array) -> array:
    '''
    Add  a cannal to a 2D array representing a gray image
    '''
    # Pour reconvertir l'image soit dans un format 3D (h x l x canaux),
    # on utilise np.expand_dims, qui  ajoute une nouvelle dimension à
    # un tableau NP à l'emplacement spécifié
    img_shaped = np.expand_dims(img, axis=-1)
    print(f"The shape of image is: {img.shape} or "
          f"{img_shaped.shape}")
    print(img_shaped)
    return img_shaped


def display_gray_img(img: array) -> None:
    '''
    Display a gray image directly on screen
    '''
    if img.size == 0:  # on check qu'on a bien un tableau a afficher
        print("No image to display")
    else:
        plt.imshow(img, cmap='gray')  # sert a l'affichage en niveaux de gris
        plt.show()


def transpose_array(img: array) -> array:
    '''
    Transpose a given array
    '''

    # Tableau --> list --> Tableau
    tsp_list = []
    for i in range(len(img[0])):
        new_row = []
        for row in img:
            new_row.append(int(row[i]))
        tsp_list.append(new_row)
    new_array = np.array(tsp_list)
    print(f"New shape after Transpose: {new_array.shape}")
    return new_array


def main():
    img_np = ft_load("animal.jpeg")
    if img_np is None:
        return
    try:
        img_zoom = cut_quare_image(img_np, 400, 200, 400)
        img_gray = img_to_gray(img_zoom)
        shape_array(img_gray)
        img_rotate = transpose_array(img_gray)
        print(img_rotate)
        display_gray_img(img_rotate)

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
