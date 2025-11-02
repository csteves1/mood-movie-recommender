# mood_movie_recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# --- Step 1: Define genre labels (from MovieLens 100k docs) ---
genre_labels = [
    "Unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

# --- Step 2: Load movies file with all genre indicator columns ---
movies_raw = pd.read_csv(
    "ml-100k/u.item",
    sep="|",
    header=None,
    encoding="latin-1"
)

# Extract movie_id, title, and genre flags
movies = movies_raw.iloc[:, [0, 1] + list(range(5, 24))].copy()
movies.columns = ["movie_id", "title"] + genre_labels

# --- Step 3: Build a "genres" string column ---
def get_genres(row):
    genres = [g for g, val in zip(genre_labels, row[2:]) if val == 1]
    return "|".join(genres) if genres else "Unknown"

movies["genres"] = movies.apply(get_genres, axis=1)

# Debug: show first few with genres
print(movies[["title", "genres"]].head())

# --- Step 4: Build similarity matrix based on genres ---
vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = vectorizer.fit_transform(movies['genres'])
similarity = cosine_similarity(genre_matrix)

# --- Step 5: Define mood → genre mapping ---
mood_map = {
    "chill": ["Comedy", "Romance"],
    "intense": ["Action", "Thriller", "Crime"],
    "thoughtful": ["Drama", "Documentary"],
    "feel-good": ["Children's", "Animation", "Musical"],
    "adventurous": ["Adventure", "Sci-Fi", "Fantasy"]
}

# --- Step 6: Recommendation function ---
def recommend(watched_titles, mood, top_n=5):
    # Find indices of watched movies
    watched_idx = movies[movies['title'].isin(watched_titles)].index.tolist()
    if not watched_idx:
        return ["No matches found in dataset. Try different titles."]

    # Average similarity scores across watched movies
    sim_scores = similarity[watched_idx].mean(axis=0)

    # Wrap in a Series aligned with movies DataFrame
    sim_series = pd.Series(sim_scores, index=movies.index)

    # Filter by mood genres
    mood_genres = mood_map.get(mood.lower(), [])
    mask = movies['genres'].apply(lambda g: any(m in g for m in mood_genres))

    # Apply mask and sort
    filtered_scores = sim_series[mask].sort_values(ascending=False)

    # Exclude already watched
    filtered_scores = filtered_scores.drop(watched_idx, errors="ignore")

    # Get top N titles
    recs = movies.loc[filtered_scores.index, "title"].head(top_n).tolist()

    return recs

# --- Step 7: Demo run ---
if __name__ == "__main__":
    # Ask user for input
    watched_input = input("Enter movies you've watched (comma separated, exact titles): ")
    watched = [m.strip() for m in watched_input.split(",")]

    mood = input("Enter your mood (chill, intense, thoughtful, feel-good, adventurous): ").strip().lower()

    print(f"\nWatched: {watched}")
    print(f"Mood: {mood}")
    print("\nRecommendations:")
    for r in recommend(watched, mood):
        print(" -", r)