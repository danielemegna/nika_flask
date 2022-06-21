from uuid import UUID
from ..entity.listing_candidate import *

class ListingRepository:

    def get_candidates(self) -> list[ListingCandidate]:
        raise NotImplementedError("You're calling an interface method!")

    def get_candidate(self, id: UUID) -> ListingCandidate:
        raise NotImplementedError("You're calling an interface method!")

    def add_candidate(self, candidate: ListingCandidate) -> None:
        raise NotImplementedError("You're calling an interface method!")

class ListingNotFoundError(Exception):
    pass

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

    def get_candidate(self, id):
        return ListingCandidate(
            uuid=id,
            property_transaction_id="22_12345",
            address= Address(
                street="Via Cellini",
                street_number="16",
                city="Corsico",
                zip_code="20094"
            )
        )

    def add_candidate(self, candidate):
        print("Creating candidate on DummyListingRepository ..")
        pass
