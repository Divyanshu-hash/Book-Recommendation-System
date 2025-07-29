# 📚 Book Recommendation System

A clean and responsive **Book Recommendation System** built with **Streamlit** that suggests similar books based on your selected title. It uses a content-based filtering approach and fetches real-time book covers from the **Google Books API**.

---

## 🚀 Features

- ✅ Select a book from a preloaded list
- 🔍 Get top 5 similar book recommendations
- 🖼️ Real-time book cover images using Google Books API
- 🎨 Neat and modern Streamlit user interface
- 💻 Custom CSS styling for enhanced visuals

---

## 🖼️ Demo

### Recommendation Display

![Recommendations](images/screenshot2.png)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
```
### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the App

```bash
streamlit run app.py
```

## 📁 Project Structure

```bash
book-recommendation-system/
│
├── app.py                  # Streamlit main app file
├── books.pkl               # Pickled book metadata
├── similarity.pkl          # Pickled similarity matrix
├── dataProcessing.py        # (Optional) For Testing Purpose
├── requirements.txt        # Python dependencies
├── images/                 # (Optional) Folder for screenshots
└── README.md               # This file
```

## 🧠 How It Works
The app uses cosine similarity to compare books based on content features.

A similarity matrix (similarity.pkl) is precomputed and loaded for fast retrieval.

Based on the selected book title, it retrieves the top 5 most similar books.

Cover images are fetched using the Google Books API for better visualization.

## 📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it.

## 🙋‍♂️ Author
Made with 💙 by Divyanshu Giri
