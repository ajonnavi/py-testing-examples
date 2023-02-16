import unittest
import pytest

from unittest.mock import Mock
from testlib.users import get_user_details_di
from testlib.exceptions import RecordNotFoundException, InvalidRequestException


class TestExample(unittest.TestCase):
    def test_exception_notfound(self):
        mock_conn = Mock()
        mock_conn.get_users = Mock(side_effect=RecordNotFoundException)
        with self.assertRaises(RecordNotFoundException):
            user_details = get_user_details_di(user_id=5, conn=mock_conn)
            mock_conn.get_users.assert_called_once_with(5)


def test_exception_invalid():
    mock_conn = Mock()
    mock_conn.get_users = Mock(side_effect=InvalidRequestException)
    with pytest.raises(InvalidRequestException):
        user_details = get_user_details_di(user_id="blah", conn=mock_conn)
        mock_conn.get_users.assert_called_once_with("blah")
