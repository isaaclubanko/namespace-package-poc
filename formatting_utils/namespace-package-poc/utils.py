from decimal import Decimal, ROUND_HALF_UP
import requests


def Money(amount):
    '''Returns a decimal amount rounded to the nearest hundredth unit

    '''
    decimal_amount = Decimal(amount)
    cents = Decimal('.01')
    amount = decimal_amount.quantize(cents, ROUND_HALF_UP)
    return amount

def language_by_country_code(language_code:str ) -> dict:
    re = requests.get('https://restcountries.com/v3.1/alpha/%s' % language_code)
    if re.status_code == 200:
        return re.json()[0]['languages']
    else:
        raise Exception(re.content)


