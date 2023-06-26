from typing import List

def is_available_currency(currency: str) -> bool:
    """ Checks if the currency is available on Steam

    Parameters
    ----------
    currency: :class:`str`
        Currency to be checked.

    Returns
    -------
    :class:`bool`
    """

    available_currencies: List[str] = [
        "AED", # United Arab Emirates Dirham
        "ARS", # Argentine Peso
        "AUD", # Australian Dollars
        "BRL", # Brazilian Reals
        "CAD", # Canadian Dollars
        "CHF", # Swiss Francs
        "CLP", # Chilean Peso
        "CNY", # Chinese Renminbi (yuan)
        "COP", # Colombian Peso
        "CRC", # Costa Rican Colón
        "EUR", # European Union Euro
        "GBP", # United Kingdom Pound
        "HKD", # Hong Kong Dollar
        "ILS", # Israeli New Shekel
        "IDR", # Indonesian Rupiah
        "INR", # Indian Rupee
        "JPY", # Japanese Yen
        "KRW", # South Korean Won
        "KWD", # Kuwaiti Dinar
        "KZT", # Kazakhstani Tenge
        "MXN", # Mexican Peso
        "MYR", # Malaysian Ringgit
        "NOK", # Norwegian Krone
        "NZD", # New Zealand Dollar
        "PEN", # Peruvian Sol
        "PHP", # Philippine Peso
        "PLN", # Polish Złoty
        "QAR", # Qatari Riyal
        "RUB", # Russian Rouble
        "SAR", # Saudi Riyal
        "SGD", # Singapore Dollar
        "THB", # Thai Baht
        "TRY", # Turkish Lira
        "TWD", # New Taiwan Dollar
        "UAH", # Ukrainian Hryvnia
        "USD", # United States Dollar
        "UYU", # Uruguayan Peso
        "VND", # Vietnamese Dong
        "ZAR"  # South African Rand
    ]

    for available_currency in available_currencies:
        if(currency.upper() == available_currency):
            return True
        
        return False

def formatCurrency(currency: str) -> str:
    """ Formats the currency passed into the format that Steam accepts. If the 
    currency passed is not valid, the default currency is the dollar (USD).

    Parameters
    -----------
    currency: :class:`str`
        Currency to be formatted.

    Returns
    -------
    :class:`str`
    """
    
    if(self.currencyExists(currency)):
        return currency[0:2].lower()
    
    return "us"