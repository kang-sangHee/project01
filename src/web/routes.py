from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from src.services.book_service import book_service

import os

router = APIRouter(prefix="/web", tags=["web"])
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@router.get("/books")
def books_page(request: Request):
    books = book_service.get_all()
    return templates.TemplateResponse("books.html", {"request": request, "books": books, "title": "도서 목록"})

@router.post("/books/create")
def create_book(
    request: Request,
    title: str = Form(...),
    author: str = Form(...),
    publisher: str = Form(None),
    published_year: int = Form(None),
    isbn: str = Form(None),
):
    payload = {
        "title": title,
        "author": author,
        "publisher": publisher,
        "published_year": published_year,
        "isbn": isbn,
    }
    book_service.create(payload)
    return RedirectResponse(url="/web/books", status_code=303)

@router.post("/books/delete/{book_id}")
def delete_book(request: Request, book_id: int):
    book_service.delete(book_id)
    return RedirectResponse(url="/web/books", status_code=303)
