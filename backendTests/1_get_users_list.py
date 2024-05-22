import pytest
import requests


class TestGetUserList:
    @classmethod
    def setup_class(cls):
        cls.endpoint = 'https://reqres.in'
        cls.response = requests.get(f"{cls.endpoint}/api/users?page=2")
        assert cls.response.status_code == 200

    def test_check_totals_field(self):
        response_json = self.response.json()
        assert 'total' in response_json
        assert isinstance(response_json['total'], int)
        assert response_json['total'] == 12

    def test_check_last_name_of_first_user(self):
        response_json = self.response.json()
        assert 'data' in response_json
        assert 'last_name' in response_json['data'][0]
        assert isinstance(response_json['data'][0]['last_name'], str)
        assert response_json['data'][0]['last_name'] == 'Lawson'

    def test_check_last_name_of_second_user(self):
        response_json = self.response.json()
        assert 'data' in response_json
        assert 'last_name' in response_json['data'][1]
        assert isinstance(response_json['data'][1]['last_name'], str)
        assert response_json['data'][1]['last_name'] == 'Ferguson'

    def test_compare_count_users_to_totals(self):
        response_json = self.response.json()
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) != response_json['total']

    def test_check_data_types_of_fields(self):
        response_json = self.response.json()

        # Check the presence of keys
        keys = ['page', 'per_page', 'total', 'total_pages', 'data']
        for key in keys:
            assert key in response_json

        assert isinstance(response_json['data'], list)
        for user in response_json['data']:
            user_keys = ['id', 'email', 'first_name', 'last_name', 'avatar']
            for key in user_keys:
                assert key in user

            # Validate the data types
            assert isinstance(user['id'], int)
            assert isinstance(user['email'], str)
            assert isinstance(user['first_name'], str)
            assert isinstance(user['last_name'], str)
            assert isinstance(user['avatar'], str)

        assert isinstance(response_json['page'], int)
        assert isinstance(response_json['per_page'], int)
        assert isinstance(response_json['total'], int)
        assert isinstance(response_json['total_pages'], int)


# This allows the script to be run directly with `pytest` without requiring additional configuration
if __name__ == '__main__':
    pytest.main()
