Mood-Based Movie Recommender
============================

A simple content-based recommender system built with the MovieLens 100k dataset.  
It suggests movies based on what you’ve already watched and your current mood.

How It Works
------------
1. Dataset: Each movie has binary genre flags (Action, Comedy, Drama, etc.).  
2. Feature Engineering: Genres are converted into text strings (e.g., Action|Thriller|Crime).  
3. Vectorization: Using CountVectorizer, genres are transformed into numerical vectors.  
4. Similarity: Cosine similarity measures how close movies are in genre space.  
5. Mood Filter: User selects a mood (e.g., intense → Action/Thriller/Crime).  
6. Ranking: Recommendations are sorted by similarity to watched movies and filtered by mood.

Tech Stack
----------
- Python 3.10+  
- pandas for data handling  
- scikit-learn for vectorization and similarity  
- MovieLens 100k dataset  

Installation
------------
Clone the repo and install dependencies:

git clone https://github.com/csteves1/mood-movie-recommender.git  
cd mood-movie-recommender  
pip install -r requirements.txt  

Create a requirements.txt file with:
pandas  
scikit-learn  

Usage
-----
Run the script from terminal:

python mood_movie_recommender.py

You’ll be prompted to enter:
- Movies you’ve watched (comma separated, exact titles from MovieLens 100k)  
- Your mood (chill, intense, thoughtful, feel-good, adventurous)  

Example:

Enter movies you've watched (comma separated, exact titles): Toy Story (1995), Heat (1995)  
Enter your mood (chill, intense, thoughtful, feel-good, adventurous): intense  

Output:

Watched: ['Toy Story (1995)', 'Heat (1995)']  
Mood: intense  

Recommendations:  
 - GoldenEye (1995)  
 - Die Hard: With a Vengeance (1995)  
 - Casino (1995)  
 - Seven (Se7en) (1995)  
 - Braveheart (1995)  

Features
--------
- Interactive terminal input  
- Mood to genre mapping  
- Content-based recommendations  
- Easily extendable (add ratings, NLP on plot summaries, or a Streamlit UI)  

Next Steps
----------
- Add a Streamlit web app for dropdowns and text boxes  
- Expand mood mappings for more nuanced recommendations  
- Incorporate user ratings for a hybrid recommender  

Author
------
Built by csteves1 as a portfolio project.  
