from enum import Enum
from typing import Dict, Any

from aiohttp import TCPConnector, BaseConnector

from client.abstract_client import AbstractInteractionClient
from client.config import config


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector(verify_ssl=False)

    REQUEST_TIMEOUT = config.request_timeout
    CONNECT_TIMEOUT = config.connection_timeout

    BASE_URL = config.base_url
    REQUEST_RETRY_TIMEOUTS = (0.1, 0.2, 0.4)

    class Endpoints(Enum):
        test: str = 'test'

    def __new__(cls, *args, **kwargs):
        cls.SERVICE = cls.__name__
        return super().__new__(cls)

    async def test(self):
        return await self.get('test', self.endpoint_url('test'))
