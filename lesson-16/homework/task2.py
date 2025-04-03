import pandas as pd

iris_file = 'lesson-16/homework/iris.json'
titanic_file = 'lesson-16/homework/titanic.xlsx'
flights_file = 'lesson-16/homework/Flights.parquet'
movie_file = 'lesson-16/homework/movie.csv'

def check_file(file_path):
    try:
        with open(file_path, 'r') as file:
            if file.readable():
                return True
            else:
                return False
    except FileNotFoundError:
        return False
    
if(check_file(iris_file)):
    try:
        iris_df = pd.read_json(iris_file)
        print("Original Iris DataFrame head:")
        print(iris_df.head())
        print("\nOriginal Iris columns:", iris_df.columns.tolist())

        iris_df.columns = iris_df.columns.str.lower()
        print("\nIris columns after renaming to lowercase:", iris_df.columns.tolist())

        iris_sepal_df = iris_df[['sepal_length', 'sepal_width']]
        print(f"\nSelected Iris Sepal heads: {iris_sepal_df.head()}")
    except Exception as error:
        print(f"An error occurred while processing {iris_file}: {error}")
else:
    print(f"File not found.")


if check_file(titanic_file):
    try:
        titanic_df = pd.read_excel(titanic_file)
        print(f"\nOriginal Titanic head: {titanic_df.head()}")

        print(f"Total rows in Titanic data: {len(titanic_df)}")

        if "Age" in titanic_df.columns:
            titanic_over_30_df = titanic_df[titanic_df["Age"].notna() & (titanic_df["Age"] > 30)]
            print(f"\nNumber of passengers with Age > 30: {len(titanic_over_30_df)}")
            print("Head of Titanic filtered for Age > 30:")
            print(titanic_over_30_df.head())
        else:
            print("Column 'Age' not found in Titanic data.")


        if "Sex" in titanic_df.columns:
            gender_counts = titanic_df["Sex"].value_counts()
            print(f"Passanger counts by Sex: {gender_counts}")
        else:
            print("Column 'Sex' not found in Titanic data")
    except Exception as error:
        print(f"Error occured while process: {error}")

if check_file(flights_file):
    try:
        flights_df = pd.read_parquet(flights_file)
        print("\nOriginal Flights head:")
        print(flights_df.head())
        print(f"\nTotal rows in original Flights data: {len(flights_df)}")

        required_columns = ['origin', 'dest', 'carrier']
        if all(col in flights_df.columns for col in required_columns):
            flights_subset_df = flights_df[required_columns]
            print("\nSubset of Flights  (origin, dest, carrier) head:")
            print(flights_subset_df.head())
        else:
            print(f"One or more columns {required_columns} not found in Flights data.")
        
        if 'dest' in flights_df.columns:
            uniques_dest_counts = flights_df['dest'].nunique()
            print(f"Number of unique destinations: {uniques_dest_counts}")
        else:
            print("Column 'dest' not found in Flights data")
    except Exception as e:
        print(f"An error occurred while processing {flights_file}: {e}")

else:
    print(f"Skipping Flights processing as file not found.")



if check_file(movie_file):
    try:
        movie_df = pd.read_csv(movie_file)
        print("\nOriginal Movie DataFrame head:")
        print(movie_df.head())
        print(f"\nTotal rows in original Movie data: {len(movie_df)}")

        if 'duration' in movie_df.columns:
            long_movies_df = movie_df['duration'].notna() & (movie_df['duration'] > 120)
            print(f"\nNumber of movies with duration > 120 minutes: {len(long_movies_df)}")
            print("Head of Movie DataFrame filtered for duration > 120:")
            print(long_movies_df.head())
        else:
            print("Column 'duration' not found in Movie data.")
        if 'director_facebook_likes' in movie_df.columns:
            sorted_long_movies_df = long_movies_df.sort_values(by = 'director_facebook_likes', ascending=False)
            print("\nHead of long movies sorted by director_facebook_likes (desc):")
            print(sorted_long_movies_df[['movie_title', 'duration', 'director_name', 'director_facebook_likes']].head())
        else:
            print("Column 'director_facebook_likes' not found in Movie data")
    except Exception as e:
        print(f"An error occurred while processing {movie_file}: {e}")
else:
    print(f"Skipping Movie processing as file not found.")