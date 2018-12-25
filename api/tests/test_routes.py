from api import app
import unittest
import json


class TestRoutes(unittest.TestCase):

    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        self.assertEqual(response.status, 200)

    def test_health_returns_200(self):
        request, response = app.test_client.get('/health')
        self.assertEqual(response.status, 200)

    def test_metrics_returns_200(self):
        request, response = app.test_client.get('/metrics')
        self.assertEqual(response.status, 200)

    def test_mail_submit_returns_200_and_expected_output(self):
        expected_output = {
            'Message': 'submitted'
        }

        test_body = {
            'from': 'from@test.com',
            'to': ['test@test.com'],
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_no_from_returns_400_and_expected_output(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no from defined'
        }

        test_body = {
            'to': ['test@test.com'],
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 400)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_no_to_returns_400_and_expected_output(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no receivers defined'
        }

        test_body = {
            'from': 'test@test.com',
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 400)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_no_subject_returns_400_and_expected_output(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no subject defined'
        }

        test_body = {
            'from': 'test@test.com',
            'to': ['test@test.com'],
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 400)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_no_message_returns_400_and_expected_output(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no message defined'
        }

        test_body = {
            'from': 'test@test.com',
            'to': ['test@test.com'],
            'subject': 'subject_test',
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 400)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_multiple_receivers_returns_200(self):
        expected_output = {
            'Message': 'submitted'
        }

        test_body = {
            'from': 'from@test.com',
            'to': ['test@test.com', 'test2@test2.com'],
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_multiple_ccs_returns_200(self):
        expected_output = {
            'Message': 'submitted'
        }

        test_body = {
            'from': 'from@test.com',
            'to': ['test@test.com'],
            'cc': ['test@test.com', 'test@test.com'],
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json, expected_output)

    def test_mail_submit_multiple_bccs_returns_200(self):
        expected_output = {
            'Message': 'submitted'
        }

        test_body = {
            'from': 'from@test.com',
            'to': ['test@test.com'],
            'bcc': ['test@test.com'],
            'subject': 'subject_test',
            'message': 'message_test'
        }
        request, response = app.test_client.post('/v1/mail', data=json.dumps(test_body))
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json, expected_output)
