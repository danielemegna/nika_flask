import pytest
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

  def test_get_candidate_by_id(self):
    repository = SqliteListingRepository('db/test.sqlite')
    uuid = repository.get_candidates()[0].uuid
    
    c = repository.get_candidate(uuid)

    assert isinstance(c, ListingCandidate), "Invalid instance type"
    assert c.uuid == uuid
    assert c.property_transaction_id == "22_12345"
    assert c.address.city == "Corsico"
    assert c.address.street == "Via Cellini"
    assert c.address.zip_code == "20094"

  def test_get_unexisting_candidate_by_id(self):
    repository = SqliteListingRepository('db/test.sqlite')
    with pytest.raises(ListingNotFoundError):
      repository.get_candidate(uuid.uuid4())