# project01 — 도서 관리 API 서버

FastAPI + Poetry 기반의 도서 CRUD API 서버입니다. 도서 데이터는 메모리(리스트)에 저장됩니다.

## 프로젝트 구조

```
project01/
├── app.py                  # 서버 실행 진입점
├── pyproject.toml          # Poetry 의존성 관리
└── src/
    ├── main.py             # FastAPI 앱 인스턴스 및 라우터 등록
    ├── models/
    │   └── book.py         # Pydantic 모델 (Book, BookCreate, BookUpdate)
    ├── routers/
    │   └── books.py        # /api/v1/books CRUD 엔드포인트
    └── services/
        └── book_service.py # 메모리 저장소 및 비즈니스 로직
```

## 빠른 시작

### 의존성 설치

```bash
poetry install
```

### 서버 실행

```bash
poetry run python app.py
```

또는

```bash
poetry run uvicorn src.main:app --reload
```

## API 엔드포인트

| 메서드   | 경로                   | 설명          |
|--------|----------------------|-------------|
| GET    | /api/v1/books        | 도서 목록 조회    |
| GET    | /api/v1/books/{id}   | 도서 단건 조회    |
| POST   | /api/v1/books        | 도서 등록       |
| PUT    | /api/v1/books/{id}   | 도서 수정       |
| DELETE | /api/v1/books/{id}   | 도서 삭제       |

Swagger UI: http://localhost:8000/docs
