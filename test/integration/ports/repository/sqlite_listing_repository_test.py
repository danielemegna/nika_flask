import uuid
from nika.domain.entity.listing_candidate import *
from nika.ports.repository.sqlite_listing_repository import *

class TestSqliteListingRepository:

  def test_get_all_candidates_sort_by_transaction_id(self):
    repository = SqliteListingRepository('db/test.sqlite')

    all = repository.get_candidates()

    assert len(all) == 2
    [first, second] = all
    assert isinstance(first, ListingCandidate), "Invalid instance type"
    assert first.uuid.version == 4
    assert first.property_transaction_id == "22_12345"
    assert first.address.city == "Corsico"
    assert isinstance(second, ListingCandidate), "Invalid instance type"
    assert second.uuid.version == 4
    assert second.property_transaction_id == "22_42345"
    assert second.address.street == "Via Boccaccio"
