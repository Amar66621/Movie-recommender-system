import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances =similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    #recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].movie_id
        #recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies



movies_dict = pickle.load(open('movie_dict.pkl','rb')) 
movies = pd.DataFrame(movies_dict)




st.title('Movie recommender system')
#movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))






selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


