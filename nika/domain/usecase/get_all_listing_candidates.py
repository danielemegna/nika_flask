class GetAllListingCandidates:

    def __init__(self, listing_repository):
        self.listing_repository = listing_repository

    def run(self):
        return self.listing_repository.get_candidates()
