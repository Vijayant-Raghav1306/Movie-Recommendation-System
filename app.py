import pickle
import streamlit as st
import requests
import pandas as pd

# Theme Selection
theme = st.radio("Choose Theme:", ["Light Mode", "Dark Mode"])

# Custom CSS for full-page Dark and Light Modes
dark_mode_css = """
    <style>
        body, .stApp {
            background-color: #121212;
            color: white;
        }
        .stSelectbox, .stTextInput, .stButton, .stRadio, .stWarning, .stColumns {
            background-color: #1e1e1e;
            color: white;
            border-radius: 5px;
        }
        .stImage img {
            border-radius: 10px;
        }
    </style>
"""

light_mode_css = """
    <style>
        body, .stApp {
            background-color: white;
            color: black;
        }
        .stSelectbox, .stTextInput, .stButton, .stRadio, .stWarning, .stColumns {
            background-color: #f0f0f0;
            color: black;
            border-radius: 5px;
        }
        .stImage img {
            border-radius: 10px;
        }
    </style>
"""

# Apply the chosen theme
st.markdown(dark_mode_css if theme == "Dark Mode" else light_mode_css, unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

def recommend(movie):
    index_list = movies[movies['title'] == movie].index.tolist()
    if not index_list:
        return [], []

    index = index_list[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.title('🎬 Movie Recommender System')

movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Type or select a movie", movie_list)

if st.button('🔍 Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    if recommended_movie_names:
        cols = st.columns(5)
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:
                st.text(name)
                st.image(poster)
    else:
        st.warning("⚠️ No recommendations found for this movie.")








