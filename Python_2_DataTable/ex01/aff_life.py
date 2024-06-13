import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_life_expectancy(data: pd.DataFrame, country: str):
    """
    Plots the life expectancy data for the specified country.

    Args:
    data (pd.DataFrame): The dataset containing life expectancy information.
    country (str): The country to plot the data for.
    """
    try:
        if country not in data['country'].values:
            raise ValueError(f"Country '{country}' not found in dataset.")

        # filter rows in a specific column ('country').
        country_data = data[data['country'] == country]
        # All columns except the first one (country name), so 1 to end.
        years = country_data.columns[1:]
        # All values for the country except the first one (country name)
        # 0 specifies the row index (first row in country_data).
        # 1: specifies the column range (from column index 1 to the end).
        values = country_data.iloc[0, 1:]

        plt.plot(years, values, label=country)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        # Set x-axis ticks at intervals of 40 years
        plt.xticks(years[::40])
        plt.show()
    except Exception as e:
        print(f"Error while plotting life expectancy: {e}")


def main():
    try:
        test_path = '../life_expectancy_years.csv'
        dataset = load(test_path)
        if dataset is not None:
            plot_life_expectancy(dataset, 'United Arab Emirates')

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
