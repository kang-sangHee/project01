from fastapi import FastAPI

from src.routers.books import router as books_router

app = FastAPI(
    title="도서 관리 API",
    description="FastAPI 기반 도서 CRUD 서버 (메모리 저장)",
    version="0.1.0",
    redirect_slashes=False,
)

app.include_router(books_router, prefix="/api/v1")


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "message": "도서 관리 API 서버가 실행 중입니다."}
