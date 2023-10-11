import requests


def main():
    bitcoin = get_bitcoin_amount()
    converted_to_dollars = convert_bitcoin_to_dollars(bitcoin)
    display_result(bitcoin, converted_to_dollars)


def get_bitcoin_amount():
    """ Get number of dollars.  TODO add validation, error handling """
    return float(input('Enter the number of bitcoin: '))


def convert_bitcoin_to_dollars(bitcoin):
    """ Convert amount of dollars to target currency """
    exchange_rate = request_exchange_rate()
    converted = convert(bitcoin, exchange_rate)
    return converted


def request_exchange_rate():
    """ Perform API request, return response. TODO add error handling """
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(coindesk_url).json()
    exchange_rate = data['bpi']['USD']['rate_float']
    return exchange_rate


def convert(bitcoin, exchange_rate):
    """ Convert using the given exchange rate """
    return bitcoin * exchange_rate


def display_result(bitcoin, converted):
    """ Format and display the result """
    print(f'{bitcoin} bitcoin is equivalent to ${converted}')


if __name__ == '__main__':
    main()
