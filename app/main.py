from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from app.database import Base, engine
from app.routers import auth_router, user, content

# 🔐 Inisialisasi limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for err in exc.errors():
        loc = err["loc"]
        if len(loc) >= 2:
            field = loc[1]
            errors[field] = err["msg"]
    return JSONResponse(status_code=422, content={"errors": errors})

app.state.limiter = limiter

# 🔐 Handler untuk error 429 (Too Many Requests)
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Terlalu banyak permintaan, coba lagi nanti."},
    )

# 📦 Register router
app.include_router(auth_router.router)
app.include_router(user.router)
app.include_router(content.router)

# 🛠️ Auto create tables
Base.metadata.create_all(bind=engine)
