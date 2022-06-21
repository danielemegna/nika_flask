from dataclasses import dataclass, replace as clone
from uuid import UUID, uuid4
from .listing_candidate import ListingCandidate
from .address import *

@dataclass(frozen=True)
class DraftListing:
    uuid: UUID
    property_transaction_id: str
    address: Address

    @staticmethod
    def forge_from(candidate: ListingCandidate) -> 'DraftListing':
        return DraftListing(
            uuid=uuid4(),
            property_transaction_id=candidate.property_transaction_id,
            address=clone(candidate.address)
        )
