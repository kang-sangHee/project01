from typing import List, Optional
from src.models.book import Book, BookCreate, BookUpdate


class BookService:
    """메모리 기반 도서 관리 서비스"""

    def __init__(self) -> None:
        self._books: List[Book] = []
        self._next_id: int = 1

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Book]:
        return self._books[skip : skip + limit]

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return next((b for b in self._books if b.id == book_id), None)

    def create(self, payload: BookCreate) -> Book:
        book = Book(id=self._next_id, **payload.model_dump())
        self._books.append(book)
        self._next_id += 1
        return book

    def update(self, book_id: int, payload: BookUpdate) -> Optional[Book]:
        book = self.get_by_id(book_id)
        if book is None:
            return None

        updated_data = book.model_dump()
        for field, value in payload.model_dump(exclude_unset=True).items():
            updated_data[field] = value

        updated_book = Book(**updated_data)
        idx = next(i for i, b in enumerate(self._books) if b.id == book_id)
        self._books[idx] = updated_book
        return updated_book

    def delete(self, book_id: int) -> bool:
        book = self.get_by_id(book_id)
        if book is None:
            return False
        self._books = [b for b in self._books if b.id != book_id]
        return True


# 애플리케이션 전역 싱글턴 인스턴스
book_service = BookService()
