from mock_data import response_mock_data
import requests
import pytest
import json

BASE_URL = "https://api.ssv.network/api/v4/mainnet/validators"


@pytest.mark.parametrize("validator_id", ["9524b215b7c918c896b09a523308dadc1c6504d5abff4ac93c0153b704cc64229ac2fe906b77372edf2adf4239e46645"])
def test_valid_validator_id(validator_id):
    url = f"{BASE_URL}/{validator_id}"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    json_response = json.loads(response.text)
    assert json_response['public_key'] == response_mock_data['public_key']
    assert json_response['cluster'] == response_mock_data['cluster']
    assert json_response['owner_address'] == response_mock_data['owner_address']


def test_invalid_validator_id():
    invalid_id = "1"
    url = f"{BASE_URL}/{invalid_id}"
    response = requests.get(url)

    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

