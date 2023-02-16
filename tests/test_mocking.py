from unittest.mock import Mock
from testlib.users import get_user_details_di


def test_basic_mock():
    mock_conn = Mock()
    mock_conn.get_users.return_value = [
        {"first_name": "John",  "last_name":  "Doe", "dept": "Eng"},
        {"first_name": "Marylyn",  "last_name":  "Paget", "dept": "Eng"}]
    user_details = get_user_details_di(2, mock_conn)

