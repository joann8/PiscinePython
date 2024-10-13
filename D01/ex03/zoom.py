from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt  # manip d'une img sous forme de np.array


def zoom_image(img: np.array, x_start: int, x_end: int,
               y_start: int, y_end: int) -> np.array:
    """
    Zoom on an image provided as an array, and given some specific dimensions.
    """
    try:
        new_img = img[y_start:y_end, x_start:x_end]
        return new_img

    except ValueError as e:
        print(type(e).__name__ + ":", e)


def img_to_gray(img: np.array) -> np.array:
    '''
    Convert an image to GRAYSCALE
    '''
    img_tmp = Image.fromarray(img)
    # Propriete Luminance pour convertir une image en gris
    img_tmp_gray = img_tmp.convert("L")
    # L'image résultante est un tableau 2D (h x l) où chaque élément représente
    # l'intensité des pixels.
    img_gray = np.array(img_tmp_gray)
    return img_gray


def shape_array(img: np.array):
    '''
    Add  a cannal to a 2D array representing a gray image
    '''
    # Pour reconvertir l'image soit dans un format 3D (h x l x canaux),
    # on utilise np.expand_dims, qui  ajoute une nouvelle dimension à
    # un tableau NP à l'emplacement spécifié (ici la fin)
    img_shaped = np.expand_dims(img, axis=-1)
    print(f"New shape after slicing: {img_shaped.shape} or "
          f"{img.shape}")
    print(img_shaped)
    return


def display_gray_img(img: np.array) -> None:
    '''
    Display a gray image directly on screen
    '''
    if img.size == 0:  # on check qu'on a bien un tableau a afficher
        print("No image to display")
    else:
        plt.imshow(img, cmap='gray')  # sert a l'affichage en niveaux de gris
        plt.show()


def main():
    img_np = ft_load("animal.jpeg")
    if img_np is None:
        return
    try:
        img_zoom = zoom_image(img_np, 450, 850, 100, 500)
        img_gray = img_to_gray(img_zoom)
        shape_array(img_gray)
        display_gray_img(img_gray)

    except AssertionError as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
