import unittest
import uuid
import requests

class TestCreateListingDraftApi:
  LISTING_CANDIDATES_BASEURL ='http://localhost:5000/listings/candidates'

  @unittest.skip("WIP")
  def test_create_draft_from_candidate(self):
    existing_candidate_id = self.retrieve_existing_listing_candidate_id()
    url = f'{self.LISTING_CANDIDATES_BASEURL}/{existing_candidate_id}/create-draft'

    response = requests.post(url)

    assert response.status_code == requests.codes.created
    response_body = response.json()
    assert is_valid_uuid4(response_body["id"]), "Invalid uuid in returned body"

  def test_create_attempt_with_unexisting_id(self):
    url = f'{self.LISTING_CANDIDATES_BASEURL}/9419bd08-ff95-48c8-9c44-783a234a270d/create-draft'

    response = requests.post(url)

    assert response.status_code == requests.codes.not_found
    assert response.json() == {
      "error_code": "LISTING_CANDIDATE_NOT_FOUND",
      "error_message": "Cannot find listing candidate with id 9419bd08-ff95-48c8-9c44-783a234a270d"
    }

  def test_get_method_not_allowed(self):
    url = f'{self.LISTING_CANDIDATES_BASEURL}/f4d3352b-62e6-41f0-bbc6-ea940612ee8b/create-draft'
    response = requests.get(url)

    assert response.status_code == requests.codes.method_not_allowed

  def retrieve_existing_listing_candidate_id(self):
    response = requests.get(self.LISTING_CANDIDATES_BASEURL)
    first_listing = response.json()[0]
    return first_listing["uuid"]

def is_valid_uuid4(value):
  try:
    uuid.UUID(value, version=4)
    return True
  except ValueError:
    return False
