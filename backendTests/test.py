import requests
import pytest


class TestCreateNewUser:
    @classmethod
    def setup_class(cls):
        cls.endpoint = 'https://reqres.in/api/users'
        cls.body = {
            "name": "John Doe",
            "job": "Software Developer"
        }
        cls.response = None  # Initialize response attribute

    def test_send_post_request(self):
        self.response = requests.post(self.endpoint, json=self.body)

        # Verify the status code
        assert self.response.status_code == 201

        # Verify the content of the response body using assertions
        assert 'id' in self.response.json()
        assert 'createdAt' in self.response.json()
        assert 'name' in self.response.json() and self.response.json()['name'] == self.body['name']
        assert 'job' in self.response.json() and self.response.json()['job'] == self.body['job']

        # Print the response text for inspection
        print("Response Text:", self.response.text)