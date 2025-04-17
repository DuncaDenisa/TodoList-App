from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

BOOKS = [
    {"title": "1984", "author": "George Orwell", "category": "Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science"},
    {"title": "The Selfish Gene", "author": "Richard Dawkins", "category": "Science"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History"},
    {"title": "Educated", "author": "Tara Westover", "category": "Memoir"},
    {"title": "Becoming", "author": "Michelle Obama", "category": "Memoir"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/search/{book_author}/")
async def get_books_by_author(book_author: str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            books_by_author.append(book)
    return books_by_author

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

        