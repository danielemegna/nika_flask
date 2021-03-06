import sqlite3
import uuid
from ...domain.repository.listing_repository import *
from ...domain.entity.listing_candidate import *

class SqliteListingRepository(ListingRepository):

    def __init__(self, db_path):
        self.db_path = db_path

    def get_candidates(self):
        db = sqlite3.connect(self.db_path)
        db.row_factory = sqlite3.Row
        query = """
            select * from listings
            where is_candidate = true
            order by property_transaction_id
        """
        rows = db.execute(query).fetchall()
        db.close()
        return [self.__row_to_candidate(row) for row in rows]

    def get_candidate(self, id: UUID) -> ListingCandidate:
        db = sqlite3.connect(self.db_path)
        db.row_factory = sqlite3.Row
        query = "select * from listings where uuid = ?"
        row = db.execute(query, [str(id)]).fetchone()
        db.close()
        if(row == None): raise ListingNotFoundError()
        return self.__row_to_candidate(row)

    def add_candidate(self, candidate):
        db = sqlite3.connect(self.db_path)
        db.execute(
            """insert into listings(
                uuid, property_transaction_id, is_candidate,
                address_street, address_street_number,
                address_city, address_zip_code
            ) values (?,?,?,?,?,?,?)
            """,
            [
                str(candidate.uuid),
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
            uuid = uuid.UUID(row["uuid"]),
            property_transaction_id = row["property_transaction_id"],
            address= Address(
                street= row["address_street"],
                street_number= row["address_street_number"],
                city= row["address_city"],
                zip_code= row["address_zip_code"]
            )
        )
