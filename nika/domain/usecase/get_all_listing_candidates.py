from nika.domain.entity.listing_candidate import ListingCandidate
from nika.domain.repository.listing_repository import ListingRepository


class GetAllListingCandidates:

    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def run(self) -> list[ListingCandidate]:
        return self.listing_repository.get_candidates()
