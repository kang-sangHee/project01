from typing import List
from fastapi import APIRouter, HTTPException, Query, status

from src.models.book import Book, BookCreate, BookUpdate
from src.services.book_service import book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=List[Book], summary="도서 목록 조회")
def list_books(
    skip: int = Query(0, ge=0, description="건너뛸 항목 수"),
    limit: int = Query(100, ge=1, le=1000, description="최대 반환 수"),
):
    return book_service.get_all(skip=skip, limit=limit)


@router.get("/{book_id}", response_model=Book, summary="도서 단건 조회")
def get_book(book_id: int):
    book = book_service.get_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="도서를 찾을 수 없습니다.")
    return book


@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED, summary="도서 등록")
def create_book(payload: BookCreate):
    return book_service.create(payload)


@router.put("/{book_id}", response_model=Book, summary="도서 수정")
def update_book(book_id: int, payload: BookUpdate):
    book = book_service.update(book_id, payload)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="도서를 찾을 수 없습니다.")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT, summary="도서 삭제")
def delete_book(book_id: int):
    deleted = book_service.delete(book_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="도서를 찾을 수 없습니다.")
