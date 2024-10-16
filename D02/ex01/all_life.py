from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def all_life(data: pd.DataFrame, country: str) -> None:
    '''
    Display information graph from a dataset about a specific country.
    '''
    country_data = data.loc[data['country'] == country]
    if country_data.empty:
        return None

    # on prend les donnes du noms des colonnes et on convertit toutes les
    # valeurs en int a partir de la 2e colonne
    years = country_data.columns[1:].astype(int)

    # iloc est une méthode qui permet d'indexer un DataFrame par position
    # 0 fait référence à la 1re ligne du DataFrame (index 0).
    lifeExpectancy = country_data.iloc[0, 1:]

    # Mise en forme du  graph
    plt.plot(years, lifeExpectancy)
    plt.title(f'{country} Life expectancy projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks([x for x in range(1800, 2100, 40)])
    plt.show()
    return None


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    all_life(data, 'France')


if __name__ == "__main__":
    main()
