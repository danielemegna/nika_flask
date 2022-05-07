import sqlite3
from ...domain.repository.listing_repository import *
from ...domain.entity.listing_candidate import *

class SqliteListingRepository(ListingRepository):

    def __init__(self, db_path):
        self.db_path = db_path

    def get_candidates(self):
        db = sqlite3.connect(self.db_path)
        db.row_factory = sqlite3.Row
        query = "select * from listings where is_candidate = true"
        rows = db.execute(query)
        listings = [self.__row_to_candidate(row) for row in rows]
        db.close()
        return listings

    def add_candidate(self, candidate):
        db = sqlite3.connect(self.db_path)
        db.execute(
            """insert into listings(
                property_transaction_id, is_candidate,
                address_street, address_street_number,
                address_city, address_zip_code
            ) values (?,?,?,?,?,?)
            """,
            [
                candidate.property_transaction_id,
                True,
                candidate.address.street,
                candidate.address.street_number,
                candidate.address.city,
                candidate.address.zip_code
            ]
        )
        db.commit()
        db.close()

    def __row_to_candidate(self, row):
        return ListingCandidate(
            property_transaction_id = row["property_transaction_id"],
            address= Address(
                street= row["address_street"],
                street_number= row["address_street_number"],
                city= row["address_city"],
                zip_code= row["address_zip_code"]
            )
        )
