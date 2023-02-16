from unittest.mock import Mock
from testlib.users import get_user_details_di


def test_assert_called():
    mock_conn = Mock()
    mock_conn.get_users.return_value = [
            {"first_name": "John",  "last_name":  "Doe", "dept": "Eng"},
            {"first_name": "Marylyn",  "last_name":  "Paget", "dept": "Eng"}]
    user_details = get_user_details_di(user_id=2, conn=mock_conn)
    mock_conn.get_users.assert_called_once()


def test_assert_called_with():
    mock_conn = Mock()
    mock_conn.get_users.return_value = [
            {"first_name": "John",  "last_name":  "Doe", "dept": "Eng"},
            {"first_name": "Marylyn",  "last_name":  "Paget", "dept": "Eng"}]
    user_details = get_user_details_di(user_id=2, conn=mock_conn)
    mock_conn.get_users.assert_called_once_with(2)
