from typing import Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="도서 제목")
    author: str = Field(..., min_length=1, max_length=100, description="저자")
    publisher: Optional[str] = Field(None, max_length=100, description="출판사")
    published_year: Optional[int] = Field(None, ge=1000, le=2100, description="출판 연도")
    isbn: Optional[str] = Field(None, max_length=20, description="ISBN")
    description: Optional[str] = Field(None, max_length=1000, description="도서 설명")


class BookCreate(BookBase):
    """도서 생성 요청 스키마"""
    pass


class BookUpdate(BaseModel):
    """도서 수정 요청 스키마 (모든 필드 선택)"""
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="도서 제목")
    author: Optional[str] = Field(None, min_length=1, max_length=100, description="저자")
    publisher: Optional[str] = Field(None, max_length=100, description="출판사")
    published_year: Optional[int] = Field(None, ge=1000, le=2100, description="출판 연도")
    isbn: Optional[str] = Field(None, max_length=20, description="ISBN")
    description: Optional[str] = Field(None, max_length=1000, description="도서 설명")


class Book(BookBase):
    """도서 응답 스키마"""
    id: int = Field(..., description="도서 고유 ID")

    model_config = {"from_attributes": True}
