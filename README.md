# 🎬 Mood-Based Movie Recommender

A simple **content-based recommender system** built with the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/).  
It suggests movies based on what you’ve already watched and your current **mood**.

---

## 🚀 How It Works
1. **Dataset**: Each movie has binary genre flags (Action, Comedy, Drama, etc.).  
2. **Feature Engineering**: Genres are converted into text strings (e.g., `Action|Thriller|Crime`).  
3. **Vectorization**: Using `CountVectorizer`, genres are transformed into numerical vectors.  
4. **Similarity**: Cosine similarity measures how close movies are in genre space.  
5. **Mood Filter**: User selects a mood (e.g., *intense* → Action/Thriller/Crime).  
6. **Ranking**: Recommendations are sorted by similarity to watched movies and filtered by mood.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **pandas** for data handling
- **scikit-learn** for vectorization + similarity
- **MovieLens 100k dataset**

---

## 📦 Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/csteves1/mood-movie-recommender.git
cd mood-movie-recommender
pip install -r requirements.txt
