import pandas as pd
import numpy as np 

iris_file = 'lesson-16/homework/iris.json'
titanic_file = 'lesson-16/homework/titanic.xlsx'
flights_file = 'lesson-16/homework/Flights.parquet'
movie_file = 'lesson-16/homework/movie.csv'

try:
    iris_df = pd.read_json(iris_file)
    numerical_cols_iris = iris_df.select_dtypes(include=np.number).columns

    for col in numerical_cols_iris:
        mean_val = iris_df[col].mean()
        median_val = iris_df[col].median()
        std_dev_val = iris_df[col].std()
        print(f"\nColumn: '{col}'")
        print(f"  Mean: {mean_val:.4f}")
        print(f"  Median: {median_val:.4f}")
        print(f"  Standard Deviation: {std_dev_val:.4f}")

except FileNotFoundError:
    print(f"Error: File not found at {iris_file}")
except Exception as e:
    print(f"An error occurred processing {iris_file}: {e}")

try:
    titanic_df = pd.read_excel(titanic_file)

    if 'Age' in titanic_df.columns:
        max_age = titanic_df["Age"].max()
        min_age = titanic_df["Age"].min()
        sum_age = titanic_df["Age"].sum()

        print("Passenger Age Statistics:")
        print(f"  Minimum Age: {min_age}")
        print(f"  Maximum Age: {max_age}")
        print(f"  Sum of Known Ages: {sum_age:.2f}")
    else:
        print("Error: 'Age' column not found in the Titanic dataset")

except FileNotFoundError:
    print(f"Error: File not found at {titanic_file}")
except Exception as e:
    print(f"An error occurred processing {titanic_file}: {e}")


try:
    movie_df = pd.read_csv(movie_file)

    if 'director_name' in movie_df.columns and 'director_facebook_likes' in movie_df.columns:

        director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()

        top_director = director_likes.idxmax()
        max_likes = director_likes.max()

        print(f"Director with the highest total Facebook likes:")
        print(f"  Director: {top_director}")
        print(f"  Total Likes: {max_likes:,.0f}")
    else:
        print("Error: Required columns ('director_name', 'director_facebook_likes') not found.")
        
    if 'movie_title' in movie_df.columns and 'duration' in movie_df.columns and 'director_name' in movie_df.columns:
        movie_df_cleaned = movie_df.dropna(subset='duration')
        longest_movies = movie_df.sort_values('duration', ascending=False).head(5)

        print("\n5 Longest Movies:")
        print(longest_movies[['movie_title', 'director_name', 'duration']])
    else:
         print("Error: Required columns ('movie_title', 'duration', 'director_name') not found.")


except FileNotFoundError:
    print(f"Error: File not found at {movie_file}")
except Exception as e:
    print(f"An error occurred processing {movie_file}: {e}")

try:
    flights_df = pd.read_parquet(flights_file)
    print("Missing values per column (Before Filling):")
    missing_before = flights_df.isnull().sum()
    print(missing_before[missing_before > 0]) 

    col_to_fill = None
    numerical_cols_flights = flights_df.select_dtypes(include=np.number).columns

    for col in numerical_cols_flights:
        if flights_df[col].isnull().any():
            col_to_fill = col
            break 

    if col_to_fill:
        print(f"\nFilling missing values in column '{col_to_fill}' with its mean.")
        mean_val_flights = flights_df[col_to_fill].mean()
        print(f"  Mean of '{col_to_fill}': {mean_val_flights:.4f}")

        flights_df_filled = flights_df.copy()
        flights_df_filled[col_to_fill] = flights_df_filled[col_to_fill].fillna(mean_val_flights)

        missing_after_col = flights_df_filled[col_to_fill].isnull().sum()
        print(f"  Missing values in '{col_to_fill}' after filling: {missing_after_col}")

    elif missing_before.sum() == 0:
         print("\nNo missing values found in the dataset.")
    else:
        print("\nNo missing values found in any *numerical* columns to fill.")


except FileNotFoundError:
    print(f"Error: File not found at {flights_file}")
except ImportError:
    print("Error: Missing library for reading parquet. Install 'pyarrow' or 'fastparquet'.")
    print("Example: pip install pyarrow")
except Exception as e:
    print(f"An error occurred processing {flights_file}: {e}")