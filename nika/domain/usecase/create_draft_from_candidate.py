from uuid import UUID
import uuid
from nika.domain.entity.listing_candidate import ListingCandidate
from nika.domain.repository.listing_repository import ListingRepository

class CreateDraftFromCandidate:

    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def run(self, listing_candidate_id: UUID) -> UUID:
        candidate = self.listing_repository.get_candidate(listing_candidate_id)
        return uuid.uuid4()
