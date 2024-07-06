import matplotlib.pyplot as plt
import polars as pl
import numpy as np
from load_csv import load


def convert_to_float(value):
    """
    Converts a string value with 'M', 'k' or 'B' suffix to a float.
    """
    if isinstance(value, str) and value.endswith('M'):
        return float(value[:-1]) * 1000000
    elif isinstance(value, str) and value.endswith('k'):
        return float(value[:-1]) * 1000
    elif isinstance(value, str) and value.endswith('B'):
        return float(value[:-1]) * 1000000000
    else:
        return float(value)


def plot_graph_population(data: pl.DataFrame, country1: str, country2: str):
    """
    Plots a graph with the population for the specified countries.

    Args:
    data (pl.DataFrame): The dataset containing population information.
    country1 (str): The first country to plot the data for.
    country2 (str): The second country to plot the data for.
    """
    try:
        # Check if the countries are in the dataset
        if country1 not in data['country'].to_list():
            raise ValueError(f"Country '{country1}' not found in dataset.")
        if country2 not in data['country'].to_list():
            raise ValueError(f"Country '{country2}' not found in dataset.")

        # Filter data for the specified countries
        country1_data = data.filter(pl.col('country') == country1)
        country2_data = data.filter(pl.col('country') == country2)

        # Extract years and convert to int
        years = [int(col) for col in country1_data.columns[1:]
                 if col.isdigit()]
        years = [year for year in years if 1800 <= year <= 2050]

        # Convert population values to floats for country1
        country1_values = country1_data.select(pl.col([str(year)
                                               for year in years]))
        country1_values = country1_values.to_numpy()[0]
        values1 = np.array([convert_to_float(value)
                            for value in country1_values])

        # Convert population values to floats for country2
        country2_values = country2_data.select(pl.col([str(year)
                                               for year in years]))
        country2_values = country2_values.to_numpy()[0]
        values2 = np.array([convert_to_float(value)
                            for value in country2_values])

        plt.plot(years, values1, label=country1, color='blue')
        plt.plot(years, values2, label=country2, color='green')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(np.arange(1800, 2050, 40))

        # Set y-axis ticks at intervals of 20 million
        max_value = max(values1.max(), values2.max())
        y_ticks = np.arange(20000000, max_value, 20000000)
        plt.yticks(y_ticks, [f'{int(tick / 1000000)}M' for tick in y_ticks])

        plt.legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(f"Error while plotting population comparison: {e}")


def main():
    try:
        test_path = '../population_total.csv'
        dataset = load(test_path)
        if dataset is not None:
            plot_graph_population(dataset, 'Belgium', 'France')
        else:
            print("Failed to load dataset.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
