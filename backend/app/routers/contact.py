
import os
import smtplib
from email.message import EmailMessage

from fastapi import APIRouter, HTTPException, status

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
def submit_contact(contact: ContactRequest):

    gmail_address = os.getenv("GMAIL_ADDRESS")
    gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")

    if not gmail_address or not gmail_app_password:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email service is not configured."
        )

    email_message = EmailMessage()

    email_message["Subject"] = f"Portfolio Contact: {contact.subject}"
    email_message["From"] = gmail_address
    email_message["To"] = gmail_address
    email_message["Reply-To"] = str(contact.email)

    email_message.set_content(
        f"""
New message from Martha Moses' portfolio.

Name: {contact.name}
Email: {contact.email}
Subject: {contact.subject}

Message:
{contact.message}
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(gmail_address, gmail_app_password)
            smtp.send_message(email_message)

        return ContactResponse(
            success=True,
            message="Your message has been sent successfully."
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to send your message. Please try again later."
        )
