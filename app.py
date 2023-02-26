import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')
#run the progrem by writing the following command in terminal:
#streamlit run app.py
#refer streamlit documentation

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in movies_list[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
    'Type or Select Movie From the dropdown',
    movies['title'].values
)

if st.button('Recommend'):
        recommendations = recommend(selected_movie_name)
        for i in recommendations:
            st.write(i)

