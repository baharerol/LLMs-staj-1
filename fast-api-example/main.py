from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# FastAPI uygulaması başlatılıyor
app = FastAPI()

# Kitap modelini tanımlıyoruz (Pydantic ile veri doğrulama)
class Book(BaseModel):
    title: str
    author: str
    year: int

# Kitapları saklamak için bir liste
books = []

# GET /books - Tüm kitapları listele
@app.get("/books/", response_model=List[Book])
def get_books():
    return books

# GET /books/{book_id} - Belirli bir kitabı ID'ye göre al
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    if 0 <= book_id < len(books):
        return books[book_id]
    return {"message": "Book not found!"}

# POST /books - Yeni bir kitap ekle
@app.post("/books/", response_model=Book)
def add_book(book: Book):
    books.append(book)
    return book

# PUT /books/{book_id} - Belirli bir kitabı ID'ye göre güncelle
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    if 0 <= book_id < len(books):
        books[book_id] = book
        return book
    return {"message": "Book not found!"}

# PATCH /books/{book_id} - Belirli bir kitabın verilerini kısmi olarak güncelle
@app.patch("/books/{book_id}", response_model=Book)
def partial_update_book(book_id: int, book: Book):
    if 0 <= book_id < len(books):
        updated_book = books[book_id]
        if book.title:
            updated_book.title = book.title
        if book.author:
            updated_book.author = book.author
        if book.year:
            updated_book.year = book.year
        books[book_id] = updated_book
        return updated_book
    return {"message": "Book not found!"}

# DELETE /books/{book_id} - Kitap sil
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    if 0 <= book_id < len(books):
        deleted_book = books.pop(book_id)
        return deleted_book
    return {"message": "Book not found!"}






