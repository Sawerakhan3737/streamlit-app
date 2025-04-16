import pandas as pd
import os

DATA_FILE = "books.csv"
def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        if df.empty:
            return add_sample_books()
        return df
    else:
        return add_sample_books()

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_book(title, author, genre, year):
    df = load_data()
    new_book = pd.DataFrame([[title, author, genre, year]], columns=df.columns)
    updated_df = pd.concat([df, new_book], ignore_index=True)
    save_data(updated_df)

# Delete a book
def delete_book(title):
    df = load_data()
    df = df[df["Title"] != title]
    save_data(df)

def add_sample_books():
    sample_books = pd.DataFrame([
        ["1984", "George Orwell", "Fiction", 1949],
        ["Sapiens", "Yuval Noah Harari", "Non-Fiction", 2011],
        ["A Brief History of Time", "Stephen Hawking", "Science", 1988],
        ["The Diary of a Young Girl", "Anne Frank", "Biography", 1947],
        ["The Art of War", "Sun Tzu", "History", -500],
        ["Atomic Habits", "James Clear", "Other", 2018],
    ], columns=["Title", "Author", "Genre", "Year"])

    save_data(sample_books)
    return sample_books
