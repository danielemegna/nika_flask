class AddListingCandidate:

    def __init__(self, listing_repository):
        self.listing_repository = listing_repository

    def run(self, listing_candidate):
        return self.listing_repository.add_candidate(listing_candidate)
