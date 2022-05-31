from nika.domain.entity.listing_candidate import ListingCandidate
from nika.domain.repository.listing_repository import ListingRepository


class AddListingCandidate:

    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository

    def run(self, listing_candidate: ListingCandidate) -> None:
        return self.listing_repository.add_candidate(listing_candidate)
