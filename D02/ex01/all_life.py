from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def all_life(data: pd.DataFrame, country : str) -> None:
    country_data = data.loc[data['country'] == country]
    if country_data.empty:
        return None 
    years = country_data.columns[1:]
    print(years)
    lifeExpentency = country_data.iloc[0, 1:]
    print(lifeExpentency)

    plt.plot(years, lifeExpentency, marker='o')
    plt.title(f'{country} LiTitle')
    plt.xlabel('Years')
    plt.ylabel('Life expectency')
    plt.show()
    return 

def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    all_life(data, 'France')
    all_life(data, 'Andorra')


if __name__ == "__main__":
    main()
