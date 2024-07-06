import matplotlib.pyplot as plt
import polars as pl
from load_csv import load


def plot_graph_life_expectancy(data: pl.DataFrame, country: str):
    """
    Plot a graph with the life expectancy data for the specified country.

    Args:
    data (pl.DataFrame): The dataset containing life expectancy information.
    country (str): The country to plot the data for.
    """
    try:
        if country not in data['country'].to_list():
            raise ValueError(f"Country '{country}' not found in dataset.")

        # filter rows in a specific column ('country').
        country_data = data.filter(pl.col('country') == country)
        # Extract years and values
        years = country_data.columns[1:]
        # All columns except the first one (country name)
        values = country_data.row(0)[1:]
        # All values for the country except the first one (country name)

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
            plot_graph_life_expectancy(dataset, 'France')

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
