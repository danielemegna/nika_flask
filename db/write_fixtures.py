from nika.ports.repository.sqlite_listing_repository import *

def run(sqlite_filepath):
    print(f'Writing some fixture data into {sqlite_filepath} db file ...')

    listing_repository = SqliteListingRepository(sqlite_filepath)
    __listing_candidates(listing_repository)

    print('Done.')

def __listing_candidates(listing_repository):
    print('ListingCandidate ...')
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
