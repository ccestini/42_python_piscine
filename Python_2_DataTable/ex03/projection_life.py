import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_gdp(data_income: pd.DataFrame, data_life: pd.DataFrame, year: int):
    """
    Plots a graph with projection of life expectancy in relation with GDP
    per capita of the year 1900 for each country.

    Args:
    data_income (pd.DataFrame): DataFrame containing income per person data.
    data_life (pd.DataFrame): DataFrame containing life expectancy data.
    """
    try:
        # Ensure each 'country' is a common column in both datasets
        if 'country' not in data_income.columns or \
                'country' not in data_life.columns:
            raise ValueError("Both datasets must contain 'country' column.")

        year_str = str(year)

        # Filter data for the specified year, creating 2 dataframes
        income_year = data_income[['country', year_str]].rename(
            columns={year_str: 'income'})
        life_year = data_life[['country', year_str]].rename(
            columns={year_str: 'life'})

        # Merge datasets on 'country' to align income and life expectancy data
        merged_data = pd.merge(income_year, life_year, on='country')

        # Plotting
        plt.scatter(merged_data['income'], merged_data['life'])
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
        income_data = \
          load('../income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
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
