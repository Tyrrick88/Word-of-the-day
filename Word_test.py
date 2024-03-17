import unittest
from unittest.mock import MagicMock, patch
from your_module import get_word, send_word

class TestWordOfTheDay(unittest.TestCase):
    
    @patch('your_module.requests.get')
    def test_get_word(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"word": "test_word"}
        mock_get.return_value = mock_response
        
        result = get_word()
        
        self.assertEqual(result, "test_word")
        mock_get.assert_called_once_with("http://api.wordnik.com/v4/words.json/wordOFTheDay", params={"api_key": "API_KEY"})
        
    @patch('your_module.Client')
    def test_send_word(self, mock_client):
        mock_message = MagicMock()
        mock_client.messages.create.return_value = mock_message
        
        send_word("test_word")
        
        mock_client.messages.create.assert_called_once_with(
            body="Today's Word of the Day test_word",
            from_='YOUR TWILIO PHONE NUMBER',
            to="YOUR_PHONE_NUMBER"
        )

if __name__ == '__main__':
    unittest.main()
