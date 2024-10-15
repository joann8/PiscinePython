from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert_population(pop: str) -> float:
    '''
    Convert the population string into a float
    '''
    if 'k' in pop:
        return float(pop.replace('k', '').strip()) * 1e3
    elif 'M' in pop:
        return float(pop.replace('M', '').strip()) * 1e6
    elif 'B' in pop:
        return float(pop.replace('B', '').strip()) * 1e9
    return float(pop.strip())


def format_millions(x, pos):
    '''
    Function that formats millions as float into a STR
    '''
    return f'{x * 1e-6:.0f}M'


def aff_pop(data: pd.DataFrame, country1: str, country2: str) -> None:
    '''
    Display information graph from a dataset comparing two countries.
    '''

    # on enleve les donnees apres 2050
    col_to_delete = [col for col in data.columns if col.isdigit()
                     and int(col) >= 2051]
    data.drop(col_to_delete, axis=1, inplace=True)
    # axis = 1 --> colonne
    # Inplace= true -> suppression directement sur le DataFrame original

    # on recupere les donnees de nos deux pays
    c1_data = data.loc[data['country'] == country1]
    c2_data = data.loc[data['country'] == country2]
    if c1_data.empty or c2_data.empty:
        print(f"{country1} and/or {country2} not found in dataset")
        return None

    # on recupere et convertit les donnees des pays en float
    c1_data_raw = c1_data.iloc[0, 1:].values
    c1_data_clean = [convert_population(pop) for pop in c1_data_raw]
    c2_data_raw = c2_data.iloc[0, 1:].values
    c2_data_clean = [convert_population(pop) for pop in c2_data_raw]

    years = data.columns[1:].astype(int)

    # on construit notre graph
    plt.plot(years, c2_data_clean, label=country2)
    plt.plot(years, c1_data_clean, label=country1, color="green")
    plt.title('Population Projections')
    # ---> Formattage de l'abcisse
    plt.xlabel('Year')
    plt.xticks(range(1800, 2051, 40))
    # ---> Formattage de l'ordonne
    plt.ylabel('Population')
    plt.yticks(range(int(20 * 1e6), int(70 * 1e6), int(20 * 1e6)))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_millions))
    plt.legend(loc="lower right")

    # affchage du graph
    plt.show()
    return


def main():
    data = load("population_total.csv")
    if data is None:
        return
    aff_pop(data, 'France', 'Belgium')
    # aff_pop(data, 'Franc', 'Belgium')


if __name__ == "__main__":
    main()
