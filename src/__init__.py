from fastapi import FastAPI
from src.books.routes import router as book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


# #the lifespan event
# @asynccontextmanager
# async def lifespan(app: FastAPI):    
#     print("Server is starting...")
#     await initdb()
#     yield
#     print("server is stopping")



# app = FastAPI(
#     lifespan=lifespan # add the lifespan event to our application
# )

# app.include_router(
#     book_router,
#     prefix="/books",
#     tags=['books']
# )

app = FastAPI(on_startup=[init_db])

app.include_router(book_router, prefix="/books", tags=["books"])