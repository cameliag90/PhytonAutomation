import pytest
import requests
from datetime import datetime
import jsonschema


class TestCreateNewUser:
    @classmethod
    def setup_class(cls):
        cls.endpoint = 'https://reqres.in/api/users'
        cls.body = {
            "name": "John Doe",
            "job": "Software Developer"
        }
        cls.response = requests.post(cls.endpoint, json=cls.body)

    def test_send_post_request(self):
        assert self.response.status_code == 201

    def test_check_id_field(self):
        response_json = self.response.json()
        assert 'id' in response_json
        assert response_json['id'] is not None
        assert isinstance(response_json['id'], str)

    def test_check_created_at_field(self):
        response_json = self.response.json()
        assert 'createdAt' in response_json
        created_at = datetime.strptime(response_json['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
        current_time_utc = datetime.now()
        assert created_at.date() == current_time_utc.date()

    def test_check_response_time_against_the_limit(self):
        start_time = datetime.now()
        requests.post(f"{self.endpoint}/api/users", json=self.body)
        end_time = datetime.now()

        # Calculate the response time in milliseconds
        response_time_ms = (end_time - start_time).total_seconds() * 1000

        # Define the limit for response time
        limit_ms = 300

        # Assert that the response time is less than the limit
        assert response_time_ms < limit_ms

    def test_check_name_and_job_parameters(self):
        response_json = self.response.json()
        assert response_json['name'] == self.body["name"]
        assert response_json['job'] == self.body["job"]

    def test_validates_response_structure_and_data_types(self):
        response_json = self.response.json()

        # Define the JSON schema for response validation
        response_schema = {
            "type": "object",
            "required": ["name", "job", "id", "createdAt"],
            "properties": {
                "name": {"type": "string"},
                "job": {"type": "string"},
                "id": {"type": "string"},
                "createdAt": {"type": "string", "format": "date-time"}
            }
        }
        jsonschema.validate(instance=response_json, schema=response_schema)


# Run the tests programmatically
pytest.main([__file__])
