import streamlit as st
import pickle
import pandas as pd
import requests

# Inject CSS for border around the entire app
st.markdown(
    """
    <style>
    .css-18e3th9 {
        border: 5px solid #222222;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-sizing: border-box;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Load data
books_dict = pickle.load(open("books.pkl", 'rb'))
books_df = pd.DataFrame(books_dict)
similarity = pickle.load(open("similarity.pkl", 'rb'))

# Function to fetch book cover from Google Books API
def fetch_book_cover(title):
    try:
        query = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title}")
        data = query.json()
        image_url = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        return image_url
    except:
        return "https://via.placeholder.com/150x220?text=No+Image"

# Recommendation function
def recommend(book):
    matches = books_df[books_df['title'] == book]
    if matches.empty:
        return []

    book_index = matches.index[0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_books = []
    for i in book_list:
        title = books_df.iloc[i[0]].title
        img_url = fetch_book_cover(title)
        recommended_books.append((title, img_url))

    return recommended_books

# Streamlit UI
st.title("📚 Book Recommendation System")
st.write("Get recommendations based on your favorite book.")

selected_book = st.selectbox("Select a book", books_df['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_book)
    if recommendations:
        st.subheader("Recommended Books:")
        for title, img_url in recommendations:
            book_html = f"""
            <div style="
                background-color: #222222;
                padding: 10px;
                border-radius: 8px;
                display: flex;
                align-items: center;
                margin-bottom: 15px;
            ">
                <img src="{img_url}" width="120" style="border-radius: 5px;"/>
                <div style="margin-left: 20px;">
                    <h3 style="color: white; margin: 0;">{title}</h3>
                </div>
            </div>
            """
            st.markdown(book_html, unsafe_allow_html=True)
