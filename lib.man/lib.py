import streamlit as st
import pandas as pd
from utils import load_data, save_data, add_book, delete_book

st.set_page_config(
    page_title="📚 Library Manager",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            color: #212529;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Library Manager")
st.markdown("---")

books_df = load_data()

menu = ["📖 View Books", "➕ Add Book", "❌ Delete Book"]
choice = st.sidebar.radio("Navigation", menu)

if choice == "📖 View Books":
    st.subheader("📘 Current Library Collection")
    if books_df.empty:
        st.info("No books in the library. Add some using the 'Add Book' section.")
    else:
        st.dataframe(books_df, use_container_width=True)

elif choice == "➕ Add Book":
    st.subheader("➕ Add a New Book to the Library")
    with st.form("add_book_form"):
        title = st.text_input("Book Title", placeholder="Enter the title of the book")
        author = st.text_input("Author", placeholder="Enter author's name")
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Biography", "History", "Other"])
        year = st.number_input("Year Published", min_value=0, max_value=2100, value=2024)
        submitted = st.form_submit_button("Add Book")
        
        if submitted:
            if title.strip() and author.strip():
                add_book(title.strip(), author.strip(), genre, int(year))
                st.success(f"✅ Book '{title}' by {author} was added successfully!")
            else:
                st.error("❌ Title and author are required fields.")

elif choice == "❌ Delete Book":
    st.subheader("🗑️ Delete a Book from the Library")
    if books_df.empty:
        st.info("There are no books to delete.")
    else:
        selected_title = st.selectbox("Select a book to delete", books_df["Title"])
        if st.button("Delete Book"):
            delete_book(selected_title)
            st.warning(f"⚠️ Book '{selected_title}' has been removed from the library.")
st.markdown("---")
st.markdown("<small>📘 Built with ❤️ using Streamlit</small>", unsafe_allow_html=True)
