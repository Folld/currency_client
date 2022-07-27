from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, Optional

from aiohttp import TCPConnector
from dataclasses_json import dataclass_json, config as dc_config

from client.abstract_client import AbstractInteractionClient
from client.config import config
from client.schemas import Currency, CultureName, Payer


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector(verify_ssl=False)

    REQUEST_TIMEOUT = config.request_timeout
    CONNECT_TIMEOUT = config.connection_timeout

    BASE_URL = config.base_url

    class Endpoints(Enum):
        test = '/test'
        charge = '/payments/tokens/charge'

    def __new__(cls, *args, **kwargs):
        cls.SERVICE = cls.__name__
        return super().__new__(cls)

    async def test(self):
        return await self.get('test', self.endpoint_url(self.Endpoints.test.value))

    async def token_charge(self,
                           amount: float,
                           token: str,
                           account_id: str,
                           *,
                           ip_address: Optional[str] = None,
                           currency: Optional[str] = Currency.rub,
                           invoice_id: Optional[str] = None,
                           description: Optional[str] = None,
                           email: Optional[str] = None,
                           json_data: Optional[dict] = None) -> Dict[str, Any]:
        """
        :param amount: Сумма платежа
        :param token: Токен
        :param ip_address: IP-адрес плательщика
        :param currency: Валюта: RUB/USD/EUR/GBP. Если параметр не передан, то по умолчанию принимает значение RUB
        :param invoice_id: Номер счета или заказа
        :param description: Описание оплаты в свободной форме
        :param account_id: Обязательный идентификатор пользователя для создания подписки и получения токена
        :param email: E-mail плательщика, на который будет отправлена квитанция об оплате
        :param json_data: Любые другие данные, которые будут связаны с транзакцией, в том числе инструкции для создания подписки или формирования онлайн-чека должны обёртываться в объект cloudpayments.

        :return:
        """

        @dataclass_json
        @dataclass
        class InnerDTO:
            amount: float = field(metadata=dc_config(field_name="Amount"))
            token: str = field(metadata=dc_config(field_name="Token"))
            account_id: str = field(metadata=dc_config(field_name="AccountId"))
            ip_address: Optional[str] = field(metadata=dc_config(field_name="IpAddress"))
            currency: Optional[str] = field(metadata=dc_config(field_name="Currency"))
            invoice_id: Optional[str] = field(metadata=dc_config(field_name="InvoiceId"))
            description: Optional[str] = field(metadata=dc_config(field_name="Description"))
            email: Optional[str] = field(metadata=dc_config(field_name="Email"))
            json_data: Optional[dict] = field(metadata=dc_config(field_name="JsonData"))

        @dataclass_json
        @dataclass
        class OutDTO:
            Success: bool
            Message: Optional[str] = None
            Model: Optional[dict] = None

        data = InnerDTO(amount=amount, ip_address=ip_address, token=token, currency=Currency(currency).value,
                        invoice_id=invoice_id, description=description, account_id=account_id,
                        email=email, json_data=json_data)
        url = self.endpoint_url(self.Endpoints.charge.value)
        response = await self.post('charge', url, json=data.to_dict(), auth=config.auth)
        return OutDTO(**response).to_dict()
