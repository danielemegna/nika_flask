from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    street_number: str
    city: str
    zip_code: str