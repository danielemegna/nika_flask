from nika.ports.repository.sqlite_listing_repository import *

def run():
    print("Writing some fixture data into db ...")

    listing_repository = SqliteListingRepository("db/db.sqlite")
    __listing_candidates(listing_repository)

    print('Done.')

def __listing_candidates(listing_repository):
    print("ListingCandidate ...")
    candidates = [
        ListingCandidate(
            property_transaction_id="22_12345",
            address=Address(
                street="Via Cellini",
                street_number="16",
                city="Corsico",
                zip_code="20094"
            )
        ),
        ListingCandidate(
            property_transaction_id="22_42345",
            address=Address(
                street="Via Boccaccio",
                street_number="13",
                city="Trezzano sul Naviglio",
                zip_code="20106"
            )
        )
    ]
    for c in candidates:
        listing_repository.add_candidate(c)

if __name__ == '__main__':
    run()
