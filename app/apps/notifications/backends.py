import logging
from abc import ABC, abstractmethod

from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


class BaseEmailBackend(ABC):
    """Abstract interface for email sending."""

    @abstractmethod
    def send(self, recipient, subject, body, html_body=None, from_email=None):
        pass


class DjangoSMTPBackend(BaseEmailBackend):
    """Uses Django's default SMTP backend."""

    def send(self, recipient, subject, body, html_body=None, from_email=None):
        from_email = from_email or settings.DEFAULT_FROM_EMAIL
        try:
            django_send_mail(
                subject,
                body,
                from_email,
                [recipient],
                html_message=html_body,
                fail_silently=False,
            )
            logger.info(f"Email sent to {recipient}: {subject}")
            return True
        except Exception as e:
            logger.exception(f"Failed to send email to {recipient}: {e}")
            raise


class BaseSMSBackend(ABC):
    @abstractmethod
    def send(self, phone_number, message):
        pass


class ConsoleSMSBackend(BaseSMSBackend):
    """For development – prints SMS to console."""

    def send(self, phone_number, message):
        print(f"[SMS to {phone_number}] {message}")
        return True


class TwilioSMSBackend(BaseSMSBackend):
    """Twilio implementation."""

    def __init__(self):
        from twilio.rest import Client

        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        self.from_number = settings.TWILIO_PHONE_NUMBER
        self.client = Client(account_sid, auth_token)

    def send(self, phone_number, message):
        try:
            self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=phone_number,
            )
            logger.info(f"SMS sent to {phone_number}")
            return True
        except Exception as e:
            logger.exception(f"Failed to send SMS to {phone_number}: {e}")
            raise
