from dataclasses import dataclass
import uuid

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
    uuid: uuid = None

    def __post_init__(self):
        if self.uuid is None: object.__setattr__(self, 'uuid', uuid.uuid4())
