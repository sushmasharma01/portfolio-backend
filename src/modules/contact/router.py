from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.session import get_db
from modules.contact.schema import (
    ContactCreateRequest,
    ContactResponse,
)
from modules.contact.service import ContactService

router = APIRouter(prefix="/contact", tags=["contact"])
service = ContactService()


@router.post("/us", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(
    payload: ContactCreateRequest,
    db: Session = Depends(get_db),
) -> ContactResponse:
    return service.create(db, payload)
