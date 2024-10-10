import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé. Vérifiez le chemin du fichier.")
    except pd.errors.ParserError:
        print("Erreur lors de l'analyse du fichier. Vérifiez le format CSV.")
    except UnicodeDecodeError:
        print("Erreur d'encodage. Essayez un autre encodage.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
