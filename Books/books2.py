from fastapi import Body, FastAPI, Path, Query, HTTPException
from starlette import status
from Book import Book
from BookRequest import BookRequest

app = FastAPI()

BOOKS = [
    Book(1, "Book One", "Author A", "Description of Book One", 5, 2021),
    Book(2, "Book Two", "Author B", "Description of Book Two", 4, 2023),
    Book(3, "Book Three", "Author C", "Description of Book Three", 3, 2021),
    Book(4, "Book Four", "Author D", "Description of Book Four", 2, 2002),
    Book(5, "Book Five", "Author E", "Description of Book Five", 1, 2010),
    Book(6, "Book Six", "Author F", "Description of Book Six", 5, 2017),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
        
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_to_return.append(book)
    return book_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(book_published_date: int = Query(gt=1999, lt=2031)):
    book_to_return = []
    for book in BOOKS:
        if book.published_date == book_published_date:
            book_to_return.append(book)
    return book_to_return

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: int):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed 
            return
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

    
   