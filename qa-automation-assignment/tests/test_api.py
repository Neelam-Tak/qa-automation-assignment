import requests
import time
from jsonschema import validate

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

def test_response_time(base_url):
    start = time.time()
    response = requests.get(f"{base_url}/posts")
    end = time.time()
    assert response.status_code == 200
    assert (end - start) < 2

def test_schema_validation(base_url):
    response = requests.get(f"{base_url}/posts")
    validate(instance=response.json()[0], schema=post_schema)

import pytest

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_multiple_endpoints(base_url, endpoint):
    response = requests.get(base_url + endpoint)
    assert response.status_code == 200