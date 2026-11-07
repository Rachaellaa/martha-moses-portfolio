
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.contact import ContactMessage
from app.schemas.contact import ContactRequest, ContactResponse


router = APIRouter(
    prefix="/api/contact",
    tags=["Contact"]
)


@router.post(
    "/",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED
)
def submit_contact(
    contact: ContactRequest,
    db: Session = Depends(get_db)
):
    try:
        new_message = ContactMessage(
            name=contact.name,
            email=str(contact.email),
            subject=contact.subject,
            message=contact.message
        )

        db.add(new_message)
        db.commit()
        db.refresh(new_message)

        return ContactResponse(
            success=True,
            message="Your message has been received successfully."
        )

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to save your message. Please try again."
        )
