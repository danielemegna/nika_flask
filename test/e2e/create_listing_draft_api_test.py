import requests

class TestCreateListingDraftApi:
  APP_BASEURL ='http://localhost:5000'

  def test_create_attempt_with_unexisting_id(self):
    url = f'{self.APP_BASEURL}/listings/candidates/9419bd08-ff95-48c8-9c44-783a234a270d/create-draft'

    response = requests.post(url)

    assert response.status_code == requests.codes.not_found
    assert response.json() == {
      "error_code": "LISTING_CANDIDATE_NOT_FOUND",
      "error_message": "Cannot find listing candidate with id 9419bd08-ff95-48c8-9c44-783a234a270d"
    }

  def test_get_method_not_allowed(self):
    url = f'{self.APP_BASEURL}/listings/candidates/f4d3352b-62e6-41f0-bbc6-ea940612ee8b/create-draft'
    response = requests.get(url)

    assert response.status_code == requests.codes.method_not_allowed
