from unittest.mock import patch
from testlib.users import get_user_details


def test_basic_patch():
    with patch('testlib.users.connection') as mock_conn:
        mock_conn.get_users.return_value = [
            {"first_name": "John",  "last_name":  "Doe", "dept": "Eng"},
            {"first_name": "Marylyn",  "last_name":  "Paget", "dept": "Eng"}]
        user_details = get_user_details(user_id=2)
        mock_conn.get_users.assert_called_once_with(2)

