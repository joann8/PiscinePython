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
    years = country_data.columns[1:].astype(int)
    lifeExpentency = country_data.iloc[0, 1:]

    plt.plot(years, lifeExpentency)
    plt.title(f'{country} Life expentancy projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectency')
    plt.xticks([x for x in range(1800, 2100, 40)])
    plt.show()
    return


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    all_life(data, 'France')


if __name__ == "__main__":
    main()
