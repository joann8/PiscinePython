from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def projection_life(data: pd.DataFrame) -> None:
    '''
    Display the projection of life expectancy in relation to the gross
    national product of the year 1900 for each country
    '''

    plt.show()
    return


def main():
    data = load("population_total.csv")
    if data is None:
        return
    projection_life(data)


if __name__ == "__main__":
    main()
