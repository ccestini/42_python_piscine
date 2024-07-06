import matplotlib.pyplot as plt
import polars as pl  # pip3 install pyarrow, python -c "import pyarrow"
from load_csv import load


def plot_gdp(data_income: pl.DataFrame, data_life: pl.DataFrame, year: int):
    """
    Plots a graph with projection of life expectancy in relation with GDP
    per capita for a given year for each country.

    Args:
    data_income (pl.DataFrame): DataFrame containing income per person data.
    data_life (pl.DataFrame): DataFrame containing life expectancy data.
    year (int): The year for which to plot the data.
    """
    try:
        # Ensure 'country' is a common column in both datasets
        if 'country' not in data_income.columns or \
           'country' not in data_life.columns:
            raise ValueError("Both datasets must contain 'country' column.")

        year_str = str(year)

        # Filter data for the specified year, creating 2 dataframes
        income_year = data_income.select(['country', year_str])\
            .rename({year_str: 'income'})
        life_year = data_life.select(['country', year_str])\
            .rename({year_str: 'life'})

        # Merge datasets on 'country' to align income and life expectancy data
        merged_data = income_year.join(life_year, on='country', how='inner')
        # 'inner' only rows with matching values in both DFrames should
        # be included in the result.

        # Convert specific columns to NumPy arrays for plotting
        income_np = merged_data['income'].to_numpy()
        life_np = merged_data['life'].to_numpy()

        # Plotting with Matplotlib and NumPy arrays
        plt.scatter(income_np, life_np)
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.title(f'Year {year}')
        plt.xlabel('Gross Domestic Product')
        plt.ylabel('Life Expectancy')
        plt.show()

    except Exception as e:
        print(f"Error plotting projection: {e}")


def main():
    try:
        income_data = load(
            '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        life_data = load('../life_expectancy_years.csv')
        year = 1900

        if income_data is not None and life_data is not None:
            plot_gdp(income_data, life_data, year)
        else:
            print("Failed to load dataset(s).")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()

'''
Countries with higher GDP per capita often have better access to healthcare,
education, sanitation, and nutrition,
which might contribute to longer life expectancies.
'''
