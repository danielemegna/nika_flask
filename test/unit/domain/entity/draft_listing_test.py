from nika.domain.entity.listing_candidate import *
from nika.domain.entity.draft_listing import *

class TestDraftListing:

  def test_forge_draft_from_candidate(self):
    candidate = ListingCandidate(
      property_transaction_id="candidate_transaction_id",
        address=Address(
          street="Via Cellini",
          street_number="16",
          city="Corsico",
          zip_code="20094"
        )
    )

    draft = DraftListing.forge_from(candidate)

    assert isinstance(draft, DraftListing), "Invalid instance type"
    assert draft.uuid != candidate.uuid
    assert draft.uuid.version == 4
    assert draft.property_transaction_id == "candidate_transaction_id"
    assert draft.address.city == "Corsico"
    assert draft.address.zip_code == "20094"
