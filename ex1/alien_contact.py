from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_alien_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("ContactID has to start with 'AC'!")
        if not self.is_verified and self.contact_type == ContactType.PHYSICAL:
            raise ValueError("Alien Contacts have to be verified!")
        if (self.witness_count < 3
                and self.contact_type == ContactType.TELEPATHIC):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses!"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages!"
                )
        return self


def print_contact(_alien_contact: AlienContact) -> None:
    print("========================================")
    print(f"ID: {_alien_contact.contact_id}")
    print(f"Type: {_alien_contact.contact_type}")
    print(f"Location: {_alien_contact.location}")
    print(f"Signal: {_alien_contact.signal_strength}/10")
    print(f"Duration: {_alien_contact.duration_minutes} minutes")
    print(f"Witnesses: {_alien_contact.witness_count}")
    if _alien_contact.message_received:
        print(f"Message: '{_alien_contact.message_received}'")
    print("========================================\n")


def main() -> None:
    print("Alien Contact Log Validation")
    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print_contact(alien_contact)

    print("Expected validation error:")
    try:
        invalid_alien_contact = AlienContact(
            contact_id="AC_2024_002",
            contact_type=ContactType.TELEPATHIC,
            location="Roswell",
            signal_strength=2.0,
            duration_minutes=100,
            witness_count=1,
            is_verified=True
        )
        print_contact(invalid_alien_contact)
    except ValidationError as e:
        print(f"{e.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
