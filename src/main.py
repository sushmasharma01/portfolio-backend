from fastapi import FastAPI

from modules.contact.router import router as contact_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Portfolio Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",  # Angular dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(contact_router, prefix="/api")
