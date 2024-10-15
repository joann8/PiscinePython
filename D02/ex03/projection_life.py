from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def format_GPD(x, pos):
    '''
    Function that formats GPD as float into a STR
    '''
    return f'{x * 1e-3:.0f}k' if x > 999 else f'{x}'


def projection_life(data_life: pd.DataFrame, data_income: pd.DataFrame,
                    year: int) -> None:
    '''
    Display the projection of life expectancy in relation to the gross
    national product of the year 1900 for each country
    '''

    # on enleve les donnees autres que 1900
    col_to_delete1 = [col for col in data_life.columns if col.isdigit()
                      and int(col) != year]
    data_life.drop(col_to_delete1, axis=1, inplace=True)
    col_to_delete2 = [col for col in data_income.columns if col.isdigit()
                      and int(col) != year]
    data_income.drop(col_to_delete2, axis=1, inplace=True)
    # axis = 1 --> colonne
    # Inplace= true -> suppression directement sur le DataFrame original

    # on verifie qu'on a bien des donnees pour l'annee selectionnee
    if len(data_income.columns) < 2 or len(data_life.columns) < 2:
        print(f"{year} not found in one of the dataset")
        return None

    data_merged = pd.merge(data_income, data_life, on='country',
                           suffixes=('_income', '_life'))

    # graphique de points
    plt.scatter(data_merged[f'{year}_income'], data_merged[f'{year}_life'],
                s=50)
    plt.title(f'{year}')
    plt.ylabel('Life expectancy')
    # ---> Formattage de l'abcisse
    plt.xlabel('Gross domestic product')
    plt.xscale('log')  # compression sur les donnees les + grandes
    plt.xticks([300, 1000, 10000])
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_GPD))
    plt.show()
    return


def main():
    d_life = load("life_expectancy_years.csv")
    d_inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if d_life is None or d_inc is None:
        return
    projection_life(d_life, d_inc, 1900)


if __name__ == "__main__":
    main()
