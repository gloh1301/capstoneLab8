import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin_exchange_rate


class TestBitcoinExchangeRate(TestCase):

    @patch('bitcoin_exchange_rate.request_exchange_rate')
    def test_bitcoin_exchange_rate(self, mock_rates):
        mock_rate = 123.4567
        example_api_response = {"rate_float": mock_rate}
        mock_rates.side_effect = [example_api_response]
        converted = bitcoin_exchange_rate.convert(100, mock_rate)
        expected = 12345.67
        self.assertEqual(expected, converted)

    @patch('requests.Response.json')
    def test_bitcoin_exchange_rate_2(self, mock_requests_json):
        mock_rate = 123.4567
        example_api_response = {"rate_float": mock_rate}
        mock_requests_json.return_value = example_api_response
        converted = bitcoin_exchange_rate.convert(100, mock_rate)
        expected = 12345.67
        self.assertEqual(expected, converted)

    @patch('builtins.input', side_effect=[2])
    def test_get_bitcoin_amount(self, mock_input):
        amount = bitcoin_exchange_rate.get_bitcoin_amount()
        self.assertEqual(2, amount)

    @patch('builtins.input', side_effect=['cat', '', '123cat', 'cat123', 2])
    def test_get_bitcoin_amount_for_non_number(self, mock_input):
        amount = bitcoin_exchange_rate.get_bitcoin_amount()
        self.assertEqual(2, amount)

    @patch('builtins.input', side_effect=[-1, -1000, 2])
    def test_get_bitcoin_amount_for_greater_than_zero(self, mock_input):
        amount = bitcoin_exchange_rate.get_bitcoin_amount()
        self.assertEqual(2, amount)

    def test_convert(self):
        amount = 100
        exchange_rate = 123.4567
        total = bitcoin_exchange_rate.convert(amount, exchange_rate)
        expected_total = 100 * 123.4567
        self.assertEqual(total, expected_total)


if __name__ == '__main__':
    unittest.main()
