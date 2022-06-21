from uuid import uuid4, UUID
from dataclasses import dataclass
from .address import *

@dataclass(frozen=True)
class ListingCandidate:
    property_transaction_id: str
    address: Address
    uuid: UUID = None

    def __post_init__(self):
        if self.uuid is None: object.__setattr__(self, 'uuid', uuid4())
