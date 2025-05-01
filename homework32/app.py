from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi", "duration": 148},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Action", "duration": 136},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime", "duration": 175},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime", "duration": 154},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
]

total_movies = len(movies)
average_duration = sum(movie["duration"] for movie in movies) / total_movies

@app.route("/")
def index():
    return render_template("index.html", movies=movies, total=total_movies, average=average_duration)

if __name__ == "__main__":
    app.run(debug=True)