# Movie Recommender System

A content-based movie recommender which takes input from the user and displays the most similar movies. A project built using Python and Streamlit.
The dataset used is available on Kaggle https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv.

The notebook Content-based recommender.ipynb contains the working and building the movie recommender from scratch. By computing the cosine similarity of the selected features and sorting the list in descending order, we have obtained movies which are similar to the entered input. 

The Python file "movie-rec.py" contains the code compatible with Streamlit which is deployed using Heroku.

Information of movies is retrieved using The Open Movie Database API http://www.omdbapi.com/

Credits to https://github.com/dgilland/omdb.py for the Python wrapper of omdb.
