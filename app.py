# -*- coding: utf-8 -*-

import streamlit as st
import pickle
import pandas as pd

def recommender(book):
    
    L = []
    
    # Vì là gợi ý nên chỉ số sẽ từ 1 đến 5, dùng trong trường hợp tên chính xác
    books_list = sorted(list(enumerate(similarity[books[books["TenSach"] == book].index[0]])), reverse=True, key = lambda x : x[1])[1:6]
  
    for i in books_list:
        book_id = i[0]
        # Lấy ảnh bằng API
        L.append(books.iloc[i[0]].TenSach)
    
    return L

books_dict = pickle.load(open('data/books_dict.pkl',"rb"))
books = pd.DataFrame(books_dict)
similarity = pickle.load(open('data/similarity.pkl',"rb"))



st.title('Book Recommender System')
st.markdown("<style>h1{color: teal;}</style>", unsafe_allow_html=True)

selected_book_name = st.selectbox(
   'Nhập hoặc chọn tên sách bạn muốn gợi ý',
    books["TenSach"])

check = st.button('Gợi ý')
st.markdown("<style>{background-color: red;}</style>", unsafe_allow_html=True)

if check:
    recommendation = recommender(selected_book_name)
    for i in recommendation:
        st.write(recommendation.index(i)+1, ". ", i)
