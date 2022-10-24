from enum import Enum
from typing import Dict, Any, Optional

from aiohttp import TCPConnector
from pydantic import BaseModel, Field

from client.abstract_client import AbstractInteractionClient
from client.config import config
from client.schemas import Currency


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector()

    REQUEST_TIMEOUT = config.request_timeout
    CONNECT_TIMEOUT = config.connection_timeout

    BASE_URL = config.base_url

    class Endpoints(str, Enum):
        test = '/test'
        token_charge = '/payments/tokens/charge'

    def __new__(cls, *args, **kwargs):
        cls.SERVICE = cls.__name__
        return super().__new__(cls)

    async def test(self):
        """Test request"""
        return await self.get('test', self.endpoint_url(self.Endpoints.test.value), auth=config.auth)

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
        Pay by token.

        :param amount: Сумма платежа
        :param token: Токен
        :param ip_address: IP-адрес плательщика
        :param currency: Валюта: RUB/USD/EUR/GBP. Если параметр не передан, то по умолчанию принимает значение RUB
        :param invoice_id: Номер счета или заказа
        :param description: Описание оплаты в свободной форме
        :param account_id: Идентификатор пользователя
        :param email: E-mail плательщика, на который будет отправлена квитанция об оплате
        :param json_data: Любые другие данные, которые будут связаны с транзакцией

        :return:
        """

        class InnerDTO(BaseModel):
            amount: float = Field(alias="Amount")
            token: str = Field(alias="Token")
            account_id: str = Field(alias="AccountId")
            ip_address: Optional[str] = Field(alias="IpAddress")
            currency: Optional[str] = Field(alias="Currency")
            invoice_id: Optional[str] = Field(alias="InvoiceId")
            description: Optional[str] = Field(alias="Description")
            email: Optional[str] = Field(alias="Email")
            json_data: Optional[dict] = Field(alias="JsonData")

            def dict(self, *args, by_alias=True, **kwargs):
                return super().dict(*args, by_alias=by_alias, **kwargs)

        class OutDTO(BaseModel):
            Success: bool
            Message: Optional[str] = None
            Model: Optional[dict] = None

        data = InnerDTO(
            Amount=amount,
            IpAddress=ip_address,
            Token=token,
            Currency=Currency(currency),
            InvoiceId=invoice_id,
            Description=description,
            AccountId=account_id,
            Email=email,
            JsonData=json_data)
        url = self.endpoint_url(self.Endpoints.token_charge)
        response = await self.post('charge', url, json=data.dict(), auth=config.auth)
        return OutDTO(**response).dict()
