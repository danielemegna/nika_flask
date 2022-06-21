import sqlite3
from nika.ports.repository.sqlite_listing_repository import *

def run(sqlite_filepath):
    print(f'Writing some fixture data into {sqlite_filepath} db file ...')
    __truncate_tables(['listings'], sqlite_filepath)

    listing_repository = SqliteListingRepository(sqlite_filepath)
    __listing_candidates(listing_repository)

    print('Done.')

def __listing_candidates(listing_repository):
    print('Writing listing candidates ...')
    candidates = [
        ListingCandidate(
            property_transaction_id="22_42345",
            address=Address(
                street="Via Boccaccio",
                street_number="13",
                city="Trezzano sul Naviglio",
                zip_code="20106"
            )
        ),
        ListingCandidate(
            property_transaction_id="22_12345",
            address=Address(
                street="Via Cellini",
                street_number="16",
                city="Corsico",
                zip_code="20094"
            )
        )
    ]
    for c in candidates:
        listing_repository.add_candidate(c)

def __truncate_tables(tables, sqlite_filepath):
    print('Truncate tables ...')
    db = sqlite3.connect(sqlite_filepath)
    for table in tables:
        db.execute(f"delete from {table}")
    db.commit()