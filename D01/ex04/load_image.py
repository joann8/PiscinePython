import numpy as np
from PIL import Image
import array


def ft_load(path: str) -> array:

    try:
        image = Image.open(path)
        image_array = np.array(image)
        # print("The shape of image is:", image_array.shape)
        # print(image_array)
        return image_array

    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    except IOError:
        print("Le fichier ne peut pas être ouvert. "
              "Assurez-vous qu'il s'agit d'une image valide.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
