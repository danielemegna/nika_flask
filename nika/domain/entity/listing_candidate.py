from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    street_number: str
    city: str
    zip_code: str

@dataclass(frozen=True)
class ListingCandidate:
    property_transaction_id: str
    address: Address

