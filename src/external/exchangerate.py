from typing import Dict

import requests
from requests import Response

from src import config
from src.utils import build_url


class ExchangerateClient:
    @classmethod
    def convert_currency(cls, from_currency: str, to_currency: str, amount: str) -> str:
        result = cls._make_request("/convert", {"from": from_currency, "to": to_currency, "amount": amount})
        return result["result"]

    @classmethod
    def latest_rates(cls, base: str, symbols: str) -> Dict:
        result = cls._make_request("/latest", {"base": base, "symbols": symbols})
        return result["rates"]

    @classmethod
    def _make_request(cls, path: str, params: Dict) -> Dict:
        url = build_url(config.EXCHANGERATE_BASE_URL, path, params)
        response = requests.get(url)
        return cls._parse_response(response)

    @staticmethod
    def _parse_response(response: Response) -> Dict:
        return response.json()
