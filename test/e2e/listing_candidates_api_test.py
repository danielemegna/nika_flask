import uuid
import requests

class TestListingCandidatesApi:
  ROUTE_UNDER_TEST ='http://localhost:5000/listings/candidates'

  def test_get_all_candidates(self):
    response = requests.get(self.ROUTE_UNDER_TEST)

    assert response.status_code == requests.codes.ok
    response_body = response.json()
    assert len(response_body) == 2
    [first, second] = response_body
    assert is_valid_uuid4(first["uuid"]), "Invalid uuid in returned body"
    assert len(first["property_transaction_id"]) > 0
    assert len(first["address"]["city"]) > 0
    assert len(first["address"]["street"]) > 0
    assert is_valid_uuid4(second["uuid"]), "Invalid uuid in returned body"
    assert len(second["property_transaction_id"]) > 0
    assert len(second["address"]["street_number"]) > 0
    assert len(second["address"]["zip_code"]) > 0

  def test_post_method_not_allowed(self):
    response = requests.post(self.ROUTE_UNDER_TEST)
    assert response.status_code == requests.codes.method_not_allowed

def is_valid_uuid4(value):
  try:
      uuid.UUID(value, version=4)
      return True
  except ValueError:
      return False