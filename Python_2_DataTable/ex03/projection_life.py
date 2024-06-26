import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_projection_life(data_income: pd.DataFrame, data_life: pd.DataFrame):
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

        # Filter data for the year 1900, creating 2 dataframes
        income_1900 = data_income[['country', '1900']]
        life_1900 = data_life[['country', '1900']]

        # Merge datasets on 'country' to align income and life expectancy data
        merged_data = pd.merge(income_1900, life_1900, on='country',
                               suffixes=('_income', '_life'))  # col name

        # Plotting
        plt.scatter(merged_data['1900_income'], merged_data['1900_life'],
                    label='1900')
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.title('Year 1900')
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

        if income_data is not None and life_data is not None:
            plot_projection_life(income_data, life_data)
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
