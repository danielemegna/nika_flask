from ..entity.listing_candidate import *

class ListingRepository:

    def get_candidates(self):
        raise NotImplementedError("You're calling an interface method!")

    def add_candidate(self, candidate):
        raise NotImplementedError("You're calling an interface method!")

########################################################################

class DummyListingRepository(ListingRepository):

    def get_candidates(self):
        return [
            ListingCandidate(
                property_transaction_id="22_12345",
                address= Address(
                    street="Via Cellini",
                    street_number="16",
                    city="Corsico",
                    zip_code="20094"
                )
            ),
            ListingCandidate(
                property_transaction_id="22_42345",
                address= Address(
                    street="Via Boccaccio",
                    street_number="13",
                    city="Trezzano sul Naviglio",
                    zip_code="20106"
                )
            )
        ]

    def add_candidate(self, candidate):
        print("Creating candidate on DummyListingRepository ..")
        pass
