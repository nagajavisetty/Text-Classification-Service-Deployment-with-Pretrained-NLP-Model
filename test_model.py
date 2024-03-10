import unittest
from unittest.mock import patch

# Patch the import of model.py
with patch('model.pipeline'):
    from model import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('model.classifier')
    def test_predict_route(self, mock_classifier):
        mock_classifier.return_value = {'labels': ['positive']}
        with self.app as client:
            response = client.post('/predict', data={'sentence': 'This is a test sentence', 'labels': "['positive', 'negative']"})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Prediction: positive', response.data)

    @patch('model.classifier')
    def test_invalid_input(self, mock_classifier):
        with self.app as client:
            response = client.post('/predict', data={'sentence': '', 'labels': ''})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Error', response.data)


if __name__ == '__main__':
    unittest.main()
