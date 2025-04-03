import sqlite3
import pandas as pd

#problem1
try:
    connection = sqlite3.connect('lesson-16/homework/chinok.db')
    
    query = 'SELECT * FROM customers'
    customers_df = pd.read_sql_query(query, connection)

    print(customers_df.head(10))

except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
except pd.errors.DatabaseError as e:
    print(f"Pandas SQL error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# problem 2:
try:
    iris_df = pd.read_json('lesson-16/homework/iris.json')

    print(f"Shape of the dataset: {iris_df.shape}")
    print(f"Column names: {iris_df.columns}")

except ValueError as e:
    print(f"JSON file error: {e}")
except FileNotFoundError:
    print("JSON file not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Problem 3:
try:
    titanic_pd = pd.read_excel('lesson-16/homework/titanic.xlsx')

    print(f"First 5 rows:\n{titanic_pd.head()}")

except ValueError as e:
    print(f"Excel file error: {e}")
except FileNotFoundError:
    print("Excel file not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Problem 4:
try:
    flights_df = pd.read_parquet('flights.parquet')

    print("Flights dataset info:")
    flights_df.info()

except ValueError as e:
    print(f" Parquet file error: {e}")
except FileNotFoundError:
    print("Parquet file not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Problem 5: 
try:
    movie_df = pd.read_csv('movie.csv')

    print("Random 10 movie samples:")
    print(movie_df.sample(10))

except ValueError as e:
    print(f"CSV file error: {e}")
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")