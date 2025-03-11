🎬 Movie Recommender System  

This is a movie recommendation system** that suggests similar movies based on user selection.  
It uses a precomputed similarity matrix stored in `similarity.pkl` and fetches movie posters from **The Movie Database (TMDb) API.  

---

 🚀 Features  
- Movie Recommendations: Select a movie to get similar movie suggestions.  
- Poster Display: Fetches posters of recommended movies.  
- Dark Mode & Light Mode:** Users can switch themes for better visibility.  

---

 📁 Project Structure  
 app.py # Main Streamlit app
 movie_dict.pkl # Pickled file containing movie data
 requirements.txt # List of required Python libraries

 
> Note: `similarity.pkl` is not stored in this repository. It is automatically downloaded from GitHub Releases.

---

 🛠️ Setup Instructions  

 1️⃣ Clone the Repository**  
bash
git clone https://github.com/YOUR-USERNAME/movie-recommender-app.git
cd movie-recommender-app

NOTE:Similarity.pkl
The file is not stored in the repository.
It is downloaded automatically from GitHub Releases when the app starts.
If the download fails, the app will show an error message.

You can run the streamlit app using streamlit run app.py
 

