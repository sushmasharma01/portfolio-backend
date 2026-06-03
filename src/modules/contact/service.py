import logging

from sqlalchemy.orm import Session

from src.helper.email import send_contact_email
from src.modules.contact import crud
from src.modules.contact.schema import ContactCreateRequest, ContactResponse


logger = logging.getLogger(__name__)


class ContactService:
    def create(self, db: Session, payload: ContactCreateRequest) -> ContactResponse:
        contact = crud.create_contact(db, payload)

        try:
            send_contact_email(
                name=payload.name,
                email=payload.email,
                message=payload.message,
            )
        except Exception:
            logger.exception(
                "Failed to send contact email for contact_id=%s", contact.id
            )

        return contact
