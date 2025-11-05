from fastapi import FastAPI
from routers import us_zipcode
from contextlib import asynccontextmanager
from database_operation import db_conn
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_conn.connect_to_db()
    yield
    db_conn.close_pool()

app = FastAPI(lifespan= lifespan)

app.include_router(us_zipcode.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
