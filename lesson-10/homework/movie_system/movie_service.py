import requests
import random
from requests.exceptions import HTTPError, RequestException

def get_genre_id(genre_name):
    API_KEY = "0721dfd992e197ca11a1f7c0a698b9fb"
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        genres = response.json().get("genres", [])
        
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
        
        print("Genre not found.")
        return None
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def get_random_movie(genre_id):
    API_KEY = "0721dfd992e197ca11a1f7c0a698b9fb"
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {"api_key": API_KEY, "with_genres": genre_id, "language": "en-US", "page": random.randint(1, 10)}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movies = response.json().get("results", [])
        
        if movies:
            movie = random.choice(movies)
            return movie["title"], movie["overview"]
        
        print("No movies found for this genre.")
        return None, None
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None, None

if __name__ == "__main__":
    genre = input("Enter a movie genre: ")
    genre_id = get_genre_id(genre)
    
    if genre_id:
        title, overview = get_random_movie(genre_id)
        if title:
            print(f"\nRecommended Movie: {title}")
            print(f"Overview: {overview}")
