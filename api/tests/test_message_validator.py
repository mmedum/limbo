import unittest
import message_validator


class TestMessageValidator(unittest.TestCase):

    def test_subject_not_defined(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no subject defined'
        }
        expected_status_code = 400
        expected_should_send = False

        test_body = {
            'from': 'test@test.com',
            'to': ['test@test.com'],
            'message': 'message_test'
        }

        should_send, msg, status_code = message_validator.validate_body(test_body)

        self.assertEqual(should_send, expected_should_send)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(msg, expected_output)

    def test_message_not_defined(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no message defined'
        }
        expected_status_code = 400
        expected_should_send = False

        test_body = {
            'from': 'test@test.com',
            'to': ['test@test.com'],
            'subject': 'test'
        }

        should_send, msg, status_code = message_validator.validate_body(test_body)

        self.assertEqual(should_send, expected_should_send)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(msg, expected_output)

    def test_to_not_defined(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no receivers defined'
        }
        expected_status_code = 400
        expected_should_send = False

        test_body = {
            'from': 'test@test.com',
            'subject': 'test',
            'message': 'test'
        }

        should_send, msg, status_code = message_validator.validate_body(test_body)

        self.assertEqual(should_send, expected_should_send)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(msg, expected_output)

    def test_from_not_defined(self):
        expected_output = {
            'Message': 'not submitted',
            'Problem': 'no from defined'
        }
        expected_status_code = 400
        expected_should_send = False

        test_body = {
            'to': ['test@test.com'],
            'subject': 'test',
            'message': 'test'
        }

        should_send, msg, status_code = message_validator.validate_body(test_body)

        self.assertEqual(should_send, expected_should_send)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(msg, expected_output)
