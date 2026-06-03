from sqlalchemy.orm import Session

from src.database.model import Contact
from src.modules.contact.schema import ContactCreateRequest


def create_contact(db: Session, payload: ContactCreateRequest) -> Contact:
    contact = Contact(
        name=payload.name,
        email=payload.email,
        message=payload.message,
    )
    try:
        db.add(contact)
        db.commit()
        db.refresh(contact)
    except Exception:
        db.rollback()
        raise

    return contact
