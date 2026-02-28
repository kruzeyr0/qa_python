import logging
import unittest
from unittest.mock import Mock, patch
from homework_10 import log_event


class TestLogEvent(unittest.TestCase):


    def test_log_event_success(self):

        mock_logger = Mock()
        with patch("homework_10.logging.getLogger", return_value=mock_logger):
            log_event("AndriiKatrych", "success")

        mock_logger.log.assert_called_once_with(logging.INFO,"Login event - Username: AndriiKatrych, Status: success")





    def test_log_event_expired(self):

        mock_logger = Mock()
        with patch("homework_10.logging.getLogger", return_value=mock_logger):
            log_event("AndriiKatrych", "expired")

        mock_logger.log.assert_called_once_with(logging.WARNING,"Login event - Username: AndriiKatrych, Status: expired")




    def test_log_event_failed(self):

        mock_logger = Mock()
        with patch("homework_10.logging.getLogger", return_value=mock_logger):
            log_event("AndriiKatrych", "failed")

        mock_logger.log.assert_called_once_with(logging.ERROR,"Login event - Username: AndriiKatrych, Status: failed")


if __name__ == "__main__":
    unittest.main()
