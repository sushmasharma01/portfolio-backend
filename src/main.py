from fastapi import FastAPI
import os
from src.modules.contact.router import router as contact_router
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title="Portfolio Backend")

frontend_url = os.getenv("FRONTEND_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "https://sushma-sharma.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(contact_router, prefix="/api")
