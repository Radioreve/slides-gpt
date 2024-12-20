import unittest
from unittest.mock import patch, MagicMock
from app.services.google_slide_service import authenticate_google_api, create_presentation
from googleapiclient.errors import HttpError

class TestGoogleSlideService(unittest.TestCase):

    @patch('google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file')
    def test_authenticate_google_api(self, mock_flow):
        mock_creds = MagicMock()
        mock_flow.return_value.run_local_server.return_value = mock_creds

        creds = authenticate_google_api()

        mock_flow.return_value.run_local_server.assert_called_once()

        self.assertEqual(creds, mock_creds)

if __name__ == '__main__':
    unittest.main()
