import requests

class TestListingCandidatesApi:
  ROUTE_UNDER_TEST ='http://localhost:5000/listings/candidates'

  def test_get_all_candidates(self):
    response = requests.get(self.ROUTE_UNDER_TEST)

    assert response.status_code == requests.codes.ok
    response_body = response.json()
    assert len(response_body) == 2
    assert len(response_body[0]["property_transaction_id"]) > 0
    assert len(response_body[0]["address"]["city"]) > 0
    assert len(response_body[0]["address"]["street"]) > 0
    assert len(response_body[1]["property_transaction_id"]) > 0
    assert len(response_body[1]["address"]["street_number"]) > 0
    assert len(response_body[1]["address"]["zip_code"]) > 0

  def test_post_method_not_allowed(self):
    response = requests.post(self.ROUTE_UNDER_TEST)
    assert response.status_code == requests.codes.method_not_allowed

