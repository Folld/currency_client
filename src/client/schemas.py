from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Currency(Enum):
    rub: str = 'RUB'
    euro: str = 'EUR'
    dollar_usa: str = 'USD'
    pound_sterling: str = 'GBR'
    hryvnia: str = 'UAH'
    rub_bel: str = 'BYN'
    tenge: str = 'KZT'
    manat: str = 'AZN'
    frank_swiss: str = 'CHF'
    crown: str = 'CZK'
    dollar_canadian: str = 'CAD'
    zloty: str = 'PLN'
    swed_krona: str = 'SEK'
    lira: str = 'TRY'
    yuan: str = 'CNY'
    rupee: str = 'INR'
    real: str = 'BRL'
    rand: str = 'ZAR'
    sum_uzb: str = 'UZS'
    lev: str = 'BGN'
    leu: str = 'RON'
    dollar_australian: str = 'AUD'
    dollar_hong_kong: str = 'HKD'
    lari: str = 'GEL'
    som_krg: str = 'KGS'
    dram: str = 'AMD'
    dirham: str = 'AED'


class CultureName(Enum):
    russian: str = 'ru-RU'
    US: str = 'en-US'
    latvian: str = 'lv'
    azerbaijani: str = 'az'
    ukrainian: str = 'uk'
    polish: str = 'pl'
    vietnamese: str = 'vi'
    turkish: str = 'tr'


@dataclass
class Payer:
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    MiddleName: Optional[str] = None
    Birth: Optional[str] = None
    Street: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    Phone: Optional[str] = None
    Postcode: Optional[str] = None
