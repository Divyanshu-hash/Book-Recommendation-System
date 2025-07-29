import numpy as np
import pandas as pd
import pickle

books=pd.read_csv(r"C:\Users\Divyanshu\Downloads\books.csv\books.csv")

books=books[["isbn10","title","authors","categories","description"]]
books.dropna(inplace=True)

books["summary"]=books["description"].apply(lambda x: x.split() )

books['categories']=books['categories'].str.replace(" ", "")
books['genre']=books["categories"].apply(lambda x: x.split() )

books['authors']=books['authors'].str.replace(" ", "")
books['authors']=books["authors"].apply(lambda x: x.split() )

books['tags']=books['authors']+books['genre']+books['summary']
df_books=books[["isbn10","title","tags"]]

df_books['tags']=df_books['tags'].apply(lambda x:" ".join(x))
df_books['tags']=df_books['tags'].astype(str).str.lower()

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words='english')
vectors=cv.fit_transform(df_books['tags']).toarray()

from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)

def recommend(book):
    book_index=df_books[df_books['title']==book].index[0]
    distances=similarity[book_index]
    print(distances)
    book_list=sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    for i in book_list:
        
        print(books.iloc[i[0]].title)

recommend("The Four Loves")

