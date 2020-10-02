import streamlit as st
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import omdb

st.title("Movie Recommender")

st.subheader("Confused which movie to watch?")
st.write("Try entering the name of your favourite movie and let the recommender system work its magic :sparkles:")
def load_data():
    data = pd.read_csv("movie_dataset.csv")
    return data

movies = load_data()

omdb.set_default('apikey','51761c2c')

features = ["keywords","genres","cast","director"]
for i in features:
    movies[i] = movies[i].fillna(" ")
    
# Adding new column which contains string of all features

def combined_features(row):
    return row["keywords"] + " " + row["genres"] + " " + row["cast"] + " " + row["director"] 

movies["combined_features"] = movies.apply(combined_features, axis=1)

# Computing the cosine similarity after vectorizing features

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies["combined_features"])

cos_sim = cosine_similarity(count_matrix)

def get_index(movie):
    return movies[movies["title"] == movie]["index"].values[0]
def get_movie(index):
    return movies[movies["index"] == index]["title"].values[0]

def recommend_movies(movie):
    
    try:
        movie = ' '.join(i.capitalize() for i in movie.split())
        movie_index = get_index(movie)
        similiar_movies = list(enumerate(cos_sim[movie_index]))
        sorted_movies = sorted(similiar_movies,key=lambda x:x[1],reverse=True)

        top_matched = []

        for i in sorted_movies[1:]:
            if i[1] > 0.1:
                top_matched.append(i[0])

        recommended_movies = []
        for i in top_matched:
            recommended_movies.append(get_movie(i))

        st.write("## Because you liked:",movie)
        st.write("## You should probably watch our Top 10!")
        for i in recommended_movies[0:11]:
            mov_list = omdb.title(i)
            if bool(mov_list) == False:
                st.write("## Movie Title: ",i)
            else:
                movie_title = mov_list["title"]
                movie_year = mov_list["year"]
                movie_genre = mov_list["genre"]
                movie_actors = mov_list["actors"]
                #st.write(mov_list)
                if mov_list['poster'] != "N/A":
                    st.image(mov_list['poster'], width=300)
                st.write("## Movie Title: ",movie_title)
                st.write('\n')
                if st.button("Show More",key=movie_title):
                    st.write("Year of Release: ",movie_year)
                    st.write('\n')
                    st.write("Genre: ",movie_genre)
                    st.write('\n')
                    st.write("Cast: ",movie_actors)
                    if (mov_list["plot"] != "N/A"):
                        st.write(mov_list["plot"])
        st.write("## Looking for more? Drag the slider!")
        x = st.slider("Number of movies",1,len(recommended_movies),5)
        end = 11+x
        for i in recommended_movies[11:end]:
            mov_list = omdb.title(i)
            if bool(mov_list) == False:
                st.write("## Movie Title: ",i)
            else:
                movie_title = mov_list["title"]
                movie_year = mov_list["year"]
                movie_genre = mov_list["genre"]
                movie_actors = mov_list["actors"]
                #st.write(mov_list)
                if mov_list['poster'] != "N/A":
                    st.image(mov_list['poster'], width=300)
                st.write("## Movie Title: ",movie_title)
                st.write('\n')
                if st.button("Show More",key=movie_title):
                    st.write("Year of Release: ",movie_year)
                    st.write('\n')
                    st.write("Genre: ",movie_genre)
                    st.write('\n')
                    st.write("Cast: ",movie_actors)
                    if (mov_list["plot"] != "N/A"):
                        st.write(mov_list["plot"])
    except IndexError:
        st.warning("Oops! :worried: Looks like the movie you entered is not in our database. Please re-enter the movie title. ")

st.write("### Enter movie title")                    
movie = st.text_input("") 
recommend_movies(movie)

st.write("### List of movies available in our database")
if st.checkbox("Show"):
    st.write(movies["original_title"].unique())
    
st.write("### Like this? Give us a :star: on the GitHub repo!")
st.markdown("[GitHub Repository](https://github.com/Kinza-Raza/movie-recommender)")
st.write("### Follow me on Linkedin")
st.markdown("[Linkedin Profile](https://www.linkedin.com/in/kinza-raza/)")