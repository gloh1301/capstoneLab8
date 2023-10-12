import requests


def main():
    bitcoin = get_bitcoin_amount()
    converted_to_dollars = convert_bitcoin_to_dollars(bitcoin)
    display_result(bitcoin, converted_to_dollars)


def get_bitcoin_amount():
    """ Get number of bitcoin """
    positive_number = False
    while not positive_number:
        try:
            bitcoin = float(input('Enter the number of bitcoin: '))
            if bitcoin >= 0:
                positive_number = True
            else:
                print('Enter zero or positive value.')
        except ValueError:
            print('Enter zero or positive value.')
    return bitcoin


def convert_bitcoin_to_dollars(bitcoin):
    """ Convert amount of bitcoin to USD """
    exchange_rate = request_exchange_rate()
    converted = convert(bitcoin, exchange_rate)
    return converted


def request_exchange_rate():
    """ Perform API request, return response. """
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
